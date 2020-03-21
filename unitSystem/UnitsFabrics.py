from unitSystem.FractionOne import UnitFractionOneFabric
from unitSystem.FractionTwo import UnitFractionTwoFabric
from unitSystem.Units import UnitOne, UnitTwo, UnitThree, UnitFour

from random import randint


class UnitOneFabric(UnitFractionOneFabric):
    def __init__(self):
        super().__init__()

    def getCard(self) -> UnitOne:
        cardID = randint(0, 2**128)
        unit = UnitOne(cardID=cardID)
        return unit


class UnitTwoFabric(UnitFractionOneFabric):
    def __init__(self):
        super().__init__()

    def getCard(self) -> UnitTwo:
        cardID = randint(0, 2**128)
        unit = UnitTwo(cardID=cardID)
        return unit


class UnitThreeFabric(UnitFractionTwoFabric):
    def __init__(self):
        super().__init__()

    def getCard(self) -> UnitThree:
        cardID = randint(0, 2**128)
        unit = UnitThree(cardID=cardID)
        return unit


class UnitFourFabric(UnitFractionTwoFabric):
    def __init__(self):
        super().__init__()

    def getCard(self) -> UnitFour:
        cardID = randint(0, 2**128)
        unit = UnitFour(cardID=cardID)
        return unit
