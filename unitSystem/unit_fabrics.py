from unitSystem.fraction_one import UnitFractionOneFabric
from unitSystem.fraction_two import UnitFractionTwoFabric
from unitSystem.units import UnitOne, UnitTwo, UnitThree, UnitFour

from heartstoneUtils.id_generator import IDGenerator


class UnitOneFabric(UnitFractionOneFabric):
    def __init__(self):
        super().__init__()

    def get_card(self) -> UnitOne:
        cardID = IDGenerator().generate_id()
        unit = UnitOne(card_id=cardID)
        return unit


class UnitTwoFabric(UnitFractionOneFabric):
    def __init__(self):
        super().__init__()

    def get_card(self) -> UnitTwo:
        cardID = IDGenerator().generate_id()
        unit = UnitTwo(card_id=cardID)
        return unit


class UnitThreeFabric(UnitFractionTwoFabric):
    def __init__(self):
        super().__init__()

    def get_card(self) -> UnitThree:
        cardID = IDGenerator().generate_id()
        unit = UnitThree(card_id=cardID)
        return unit


class UnitFourFabric(UnitFractionTwoFabric):
    def __init__(self):
        super().__init__()

    def get_card(self) -> UnitFour:
        cardID = IDGenerator().generate_id()
        unit = UnitFour(card_id=cardID)
        return unit
