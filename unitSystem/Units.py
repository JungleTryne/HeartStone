from unitSystem.FractionOne import UnitFractionOne
from unitSystem.FractionTwo import UnitFractionTwo


class UnitOne(UnitFractionOne):
    """
    Юнит UnitOne
    Характеристики: 10 здоровья, 3 маны, 5 аттаки
    """
    def __init__(self, cardID: int):
        super().__init__(hpRate=10, manaRate=3, attackRate=5, cardID=cardID)


class UnitTwo(UnitFractionOne):
    """
    Юнит UnitOne
    Характеристики: 5 здоровья, 3 маны, 10 аттаки
    """
    def __init__(self, cardID: int):
        super().__init__(hpRate=5, manaRate=3, attackRate=10, cardID=cardID)


class UnitThree(UnitFractionTwo):
    """
    Юнит UnitOne
    Характеристики: 8 здоровья, 2 маны, 4 аттаки
    """
    def __init__(self, cardID: int):
        super().__init__(hpRate=4, manaRate=2, attackRate=8, cardID=cardID)


class UnitFour(UnitFractionTwo):
    """
    Юнит UnitOne
    Характеристики: 4 здоровья, 2 маны, 10 аттаки
    """
    def __init__(self, cardID: int):
        super().__init__(hpRate=8, manaRate=2, attackRate=4, cardID=cardID)
