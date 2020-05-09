from botCore.command_executor import CommandExecutor
from botCore.message_answer import MessageAnswer
from dataBase.database import DataBaseProxy

from commandSystem.game_commands import *


class GameHandler(CommandExecutor):
    """
    Класс обработки команд, вызванных во время игры
    """

    @staticmethod
    def execute_command(command) -> list:
        pass


class AttackCommandExecutor(CommandExecutor):
    """
    Класс обработки команды атаки на карточку противника
    """

    @staticmethod
    def execute_command(command: AttackCommand) -> list:
        db = DataBaseProxy()

        game = command.game
        attacker = command.player
        defender = None

        if command.player is game.user_one:
            defender = game.user_two
        else:
            defender = game.user_one

        if not command.victim_card:
            # Атакуем игрока

            # Проверяем, что на столе нет карт
            if len(game.field) != 0:
                return [MessageAnswer(attacker, 'Вы не можете атаковать, если на столе есть карты!')]

            defender.hp_rate -= command.attacking_card.attack_rate
            messages = [MessageAnswer(defender, 'Вы были атакованы!'),
                        MessageAnswer(attacker, 'Противник успешно атакован')]

            game.turn = defender
            if defender.hp_rate < 0:
                messages.append(MessageAnswer(defender, 'Вы проиграли!'))
                messages.append(MessageAnswer(attacker, 'Вы выйграли'))

                defender.current_game = None
                attacker.current_game = None

                db.update_user(defender.vk_id, defender)
                db.update_user(attacker.vk_id, attacker)
            return messages

        if command.attacking_card not in attacker.card_set_current:
            return [MessageAnswer(attacker, 'Вы не можете атаковать картой, которой у вас нет!')]
        if command.victim_card not in game.field:
            return [MessageAnswer(attacker, 'Вы не можете атаковать карту, которой нет на столе')]

        for i in range(len(game.field)):
            if game.field[i] is command.victim_card:
                game.field[i].hp_rate -= command.attacking_card.attack_rate
                if game.field[i].hp_rate < 0:
                    del game.field[i]
                game.turn = defender
                return [MessageAnswer(attacker, 'Вы атаковали карту противника!'),
                        MessageAnswer(attacker, 'Вашу карту атаковали!')]


class PlaceCommandExecutor(CommandExecutor):
    """
    Класс обработки команды выставления карты на игровой стол
    """

    @staticmethod
    def execute_command(command) -> list:
        card_fabric = command.attacking_card

        if not card_fabric:
            return [MessageAnswer(command.player, 'Я не понял название карты')]

        if card_fabric not in command.player.card_set_selected:
            return [MessageAnswer(command.player, 'У вас нет такой карты в колоде!')]

        command.player.current_game.field.append(card_fabric.get_card())

        defender = None
        game = command.game

        if command.player is game.user_one:
            defender = game.user_two
        else:
            defender = game.user_one

        game.turn = defender

        return [MessageAnswer(command.player, 'Вы положили карту на стол'),
                MessageAnswer(defender, 'Противник положил карту на стол')]


class NextCommandExecutor(CommandExecutor):
    """
    Класс обработки команды передачи хода
    """

    @staticmethod
    def execute_command(command) -> list:
        game = command.game
        defender = None

        if command.player is game.user_one:
            defender = game.user_two
        else:
            defender = game.user_one

        game.turn = defender
        return [MessageAnswer(game.user_one, 'Ход перешел другому игроку'),
                MessageAnswer(game.user_two, 'Ход перешел другому игроку')]
