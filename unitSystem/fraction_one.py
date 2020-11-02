from unitSystem.unit_base import Unit, UnitFabric


class UnitFractionOne(Unit):
    """
    First fraction unit class
    :param: hp_rate - hp rate of the card
    :param: attack_rate - attack rate of the card
    :param: mana_rate - price of the card
    :param: card_id unique card id
    """
    def __init__(self, hp_rate: int, attack_rate: int,
                 mana_rate: int, card_id: int):
        super().__init__(hp_rate, attack_rate, mana_rate, card_id)


class UnitFractionOneFabric(UnitFabric):
    def __init__(self):
        super().__init__()
