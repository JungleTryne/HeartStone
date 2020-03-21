class Unit:
    """
    Unit Base class
    :param: hpRate - количество hp карточки
    :param: attackRate - урон карточки
    :param: manaRate - цена использования карточки
    :cardID: уникальный ID карточки
    """
    def __init__(self, hpRate: int, attackRate: int, manaRate: int, cardID: int):
        self.hpRate = hpRate
        self.attackRate = attackRate
        self.manaRate = manaRate
        self.cardID = cardID

    def is_alive(self) -> bool:
        """
        Функция, возвращает true, если юнит ещё жив
        :return: Жив ли юнит
        """
        return self.hpRate > 0

    def attack(self, anotherUnit) -> bool:
        """
        Функция атаки на юнит. Возвращает true, если юнит еще жив
        :param anotherUnit: Атакующий юнит
        :return: Жив ли юнит
        """
        self.hpRate -= anotherUnit.attackRate
        return self.hpRate > 0



class UnitFabric:
    def __init__(self):
        pass

    def getCard(self) -> Unit:
        """
        Функция получение карточки типа Unit
        """
        pass
