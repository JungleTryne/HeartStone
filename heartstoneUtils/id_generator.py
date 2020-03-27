from random import randint
from heartstoneUtils.utils_constants import ID_RANGE


class IDGenerator:
    class __IDGenerator:
        def __init__(self):
            self._generated_ids = dict()

        def generate_id(self) -> int:
            """
            Функция, генерирующая уникальный идентификатор для объектов игры
            :return: идентификатор в промежутке от 0 до ID_RANGE
            """
            new_id = randint(0, ID_RANGE)
            while new_id in self._generated_ids:
                new_id = randint(0, ID_RANGE)
            self._generated_ids[new_id] = True
            return new_id

        def remove_id(self, object_id) -> None:
            """
            Функция, убирающая из списка зарегеистрированных id существующий id
            :param object_id: Идентификатор игрового объекта
            """
            del self._generated_ids[object_id]

    instance = None

    def __new__(cls):
        if not IDGenerator.instance:
            IDGenerator.instance = IDGenerator.__IDGenerator()
        return IDGenerator.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
