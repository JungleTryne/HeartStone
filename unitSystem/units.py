from unitSystem.fraction_one import UnitFractionOne
from unitSystem.fraction_two import UnitFractionTwo
from unitSystem.unit_constants import *


class UnitOne(UnitFractionOne):
    """
    Юнит UnitOne
    Характеристики: 10 здоровья, 3 маны, 5 аттаки
    """
    def __init__(self, card_id: int):
        parameters = UNIT_ONE_PARAMETERS
        super().__init__(hp_rate=parameters['hp_rate'],
                         mana_rate=parameters['mana_rate'],
                         attack_rate=parameters['attack_rate'],
                         card_id=card_id)


class UnitTwo(UnitFractionOne):
    """
    Юнит UnitOne
    Характеристики: 5 здоровья, 3 маны, 10 аттаки
    """
    def __init__(self, card_id: int):
        parameters = UNIT_TWO_PARAMETERS
        super().__init__(hp_rate=parameters['hp_rate'],
                         mana_rate=parameters['mana_rate'],
                         attack_rate=parameters['attack_rate'],
                         card_id=card_id)


class UnitThree(UnitFractionTwo):
    """
    Юнит UnitOne
    Характеристики: 8 здоровья, 2 маны, 4 аттаки
    """
    def __init__(self, card_id: int):
        parameters = UNIT_THREE_PARAMETERS
        super().__init__(hp_rate=parameters['hp_rate'],
                         mana_rate=parameters['mana_rate'],
                         attack_rate=parameters['attack_rate'],
                         card_id=card_id)


class UnitFour(UnitFractionTwo):
    """
    Юнит UnitOne
    Характеристики: 4 здоровья, 2 маны, 10 аттаки
    """
    def __init__(self, card_id: int):
        parameters = UNIT_FOUR_PARAMETERS
        super().__init__(hp_rate=parameters['hp_rate'],
                         mana_rate=parameters['mana_rate'],
                         attack_rate=parameters['attack_rate'],
                         card_id=card_id)
