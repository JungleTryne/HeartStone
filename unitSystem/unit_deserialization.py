from unitSystem.units import UnitOne, UnitTwo, UnitThree, UnitFour
from unitSystem.unit_base import Unit
from unitSystem.unit_fabrics import UnitFourFabric, UnitThreeFabric, UnitTwoFabric, UnitOneFabric


class UnitDeserializer:
    @staticmethod
    def deserialize(card_name: str):
        router = {
            'one': UnitOne,
            'two': UnitTwo,
            'three': UnitThree,
            'four': UnitFour,
            'player': None
        }
        return router[card_name]


class UnitCreatorDeserializer:
    @staticmethod
    def deserialize(card_name: str):
        router = {
            'one': UnitOneFabric,
            'two': UnitTwoFabric,
            'three': UnitThreeFabric,
            'four': UnitFourFabric,
            'player': None
        }
        return router[card_name]
