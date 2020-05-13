import unittest
import time
import random

from unitSystem.unit_fabrics import UnitOneFabric, UnitTwoFabric,\
    UnitThreeFabric, UnitFourFabric
from unitSystem.fraction_one import UnitFractionOne
from unitSystem.fraction_two import UnitFractionTwo
from heartstoneUtils.id_generator import IDGenerator

from botCore.message_handler import MessageHandler
from dataBase.database import DataBaseProxy


class TestFabricSystem(unittest.TestCase):

    def testFabricOne(self):
        unit_fabric = UnitOneFabric()
        unit = unit_fabric.get_card()
        self.assertEqual(10, unit.hp_rate)
        self.assertEqual(3, unit.mana_rate)
        self.assertEqual(5, unit.attack_rate)
        self.assertTrue(0 <= unit.card_id <= 2 ** 128)

    def testFabricTwo(self):
        unit_fabric = UnitTwoFabric()
        unit = unit_fabric.get_card()
        self.assertEqual(5, unit.hp_rate)
        self.assertEqual(3, unit.mana_rate)
        self.assertEqual(10, unit.attack_rate)
        self.assertTrue(0 <= unit.card_id <= 2 ** 128)

    def testFabricThree(self):
        unit_fabric = UnitThreeFabric()
        unit = unit_fabric.get_card()
        self.assertEqual(4, unit.hp_rate)
        self.assertEqual(2, unit.mana_rate)
        self.assertEqual(8, unit.attack_rate)
        self.assertTrue(0 <= unit.card_id <= 2 ** 128)

    def testFabricFour(self):
        unit_fabric = UnitFourFabric()
        unit = unit_fabric.get_card()
        self.assertEqual(8, unit.hp_rate)
        self.assertEqual(2, unit.mana_rate)
        self.assertEqual(4, unit.attack_rate)
        self.assertTrue(0 <= unit.card_id <= 2 ** 128)


class TestUnitSystem(unittest.TestCase):
    def testAttackOne(self):
        unit_fabric_one = UnitOneFabric()
        unit_fabric_three = UnitThreeFabric()
        left = unit_fabric_one.get_card()
        right = unit_fabric_three.get_card()
        left.attack(right)
        self.assertTrue(left.is_alive())
        left.attack(right)
        self.assertTrue(not left.is_alive())
        self.assertTrue(right.is_alive())

    def testAttackTwo(self):
        unit_fabric_two = UnitTwoFabric()
        unit_fabric_four = UnitFourFabric()
        left = unit_fabric_two.get_card()
        right = unit_fabric_four.get_card()
        left.attack(right)
        self.assertTrue(left.is_alive())
        left.attack(right)
        self.assertTrue(not left.is_alive())
        self.assertTrue(right.is_alive())


class TestUnitSystemStress(unittest.TestCase):
    def testAttackOne(self):
        unit_fabric = UnitOneFabric()
        _units = list()
        for i in range(0, 1000000):
            _units.append(unit_fabric.get_card())

        time_start = time.time()

        unit_fabric_one = UnitOneFabric()
        unit_fabric_three = UnitThreeFabric()
        left = unit_fabric_one.get_card()
        right = unit_fabric_three.get_card()
        left.attack(right)
        self.assertTrue(left.is_alive())
        left.attack(right)
        self.assertTrue(not left.is_alive())
        self.assertTrue(right.is_alive())

        time_finish = time.time()
        print("TestUnitSystemStress.TestUnitSystem."
              "testAttackOne time: {0} ms"
              .format((time_finish - time_start) * 1e3))


class TestIDSystem(unittest.TestCase):
    def testIDGeneration(self):
        unit_fabric = UnitOneFabric()
        unit = unit_fabric.get_card()
        card_id = unit.card_id
        assert (card_id in IDGenerator()._generated_ids)
        del unit
        assert (card_id not in IDGenerator()._generated_ids)


class TestStressFactory(unittest.TestCase):
    def testStressFactory(self):
        unit_fabric = UnitOneFabric()
        units = list()
        for i in range(0, 1000000):
            units.append(unit_fabric.get_card())
        random.shuffle(units)
        assert (len(IDGenerator()._generated_ids) == 1000000)
        del units
        assert (len(IDGenerator()._generated_ids) == 0)


class TestMenuCommands(unittest.TestCase):
    def testMenuCommands(self):
        MessageHandler.handle_request('/pick_card two', '123')
        player_one = MessageHandler.handle_request('/pick_card one', '123')[0].user
        MessageHandler.handle_request('hello', '456')
        MessageHandler.handle_request('/change_fraction two', '456')
        MessageHandler.handle_request('/pick_card three', '456')
        player_two = MessageHandler.handle_request('/pick_card four', '456')[0].user
        assert (player_one.card_set_selected == [UnitTwoFabric, UnitOneFabric])
        assert (player_two.card_set_selected == [UnitThreeFabric, UnitFourFabric])
        assert (player_one.fraction == UnitFractionOne)
        assert (player_two.fraction == UnitFractionTwo)
        MessageHandler.handle_request('/create_game 456', '123')
        db = DataBaseProxy()
        user_1 = db.get_user_by_vk_id('123')
        user_2 = db.get_user_by_vk_id('456')
        message = MessageHandler.handle_request('/pick_card two', '123')[0]
        assert ('Нельзя изменять игрока во время игры' == message.message)


class TestGameCommands(unittest.TestCase):
    def testGameCommands(self):
        MessageHandler.handle_request('hello', '456')
        MessageHandler.handle_request('hello', '123')

        MessageHandler.handle_request('/pick_card one', '123')

        MessageHandler.handle_request('/change_fraction two', '456')
        MessageHandler.handle_request('/pick_card three', '456')

        MessageHandler.handle_request('/create_game 456', '123')[0].message

        #testing that the players can't do anything if it is not his turn
        self.assertEqual(MessageHandler.handle_request('/put one', '456')[0].message, 'Не ваш ход!')
        self.assertEqual(MessageHandler.handle_request('/attack one one', '456')[0].message, 'Не ваш ход!')
        self.assertEqual(MessageHandler.handle_request('/next', '456')[0].message, 'Не ваш ход!')

        messages = MessageHandler.handle_request('/next', '123')
        self.assertEqual(messages[0].message, 'Ход перешел другому игроку')
        self.assertEqual(len(messages), 2)

        self.assertEqual(MessageHandler.handle_request('/put one', '123')[0].message, 'Не ваш ход!')

        self.assertEqual(MessageHandler.handle_request('/put three', '456')[0].message, 'Вы положили карту на стол')
        self.assertEqual(MessageHandler.handle_request('/put one', '456')[0].message, 'Не ваш ход!')

        self.assertEqual(MessageHandler.handle_request('/attack player', '123')[0].message, '')



if __name__ == '__main__':
    unittest.main()
