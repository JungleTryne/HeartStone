from unitSystem.units import UnitOne, UnitTwo, UnitThree, UnitFour
from unitSystem.unit_base import Unit


class UnitDeserializer:
    @staticmethod
    def deserialize(card_name: str):
        router = {
            'one': UnitOne,
            'two': UnitTwo,
            'three': UnitThree,
            'four': UnitFour
        }
        return router[card_name]
