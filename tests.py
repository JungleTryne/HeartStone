import unittest

from unitSystem.UnitsFabrics import UnitOneFabric, UnitTwoFabric, UnitThreeFabric, UnitFourFabric


class TestFabricSystem(unittest.TestCase):

    def testFabricOne(self):
        unitFabric = UnitOneFabric()
        unit = unitFabric.getCard()
        self.assertEqual(10, unit.hpRate)
        self.assertEqual(3, unit.manaRate)
        self.assertEqual(5, unit.attackRate)
        self.assertTrue(0 <= unit.cardID <= 2 ** 128)

    def testFabricTwo(self):
        unitFabric = UnitTwoFabric()
        unit = unitFabric.getCard()
        self.assertEqual(5, unit.hpRate)
        self.assertEqual(3, unit.manaRate)
        self.assertEqual(10, unit.attackRate)
        self.assertTrue(0 <= unit.cardID <= 2 ** 128)

    def testFabricThree(self):
        unitFabric = UnitThreeFabric()
        unit = unitFabric.getCard()
        self.assertEqual(4, unit.hpRate)
        self.assertEqual(2, unit.manaRate)
        self.assertEqual(8, unit.attackRate)
        self.assertTrue(0 <= unit.cardID <= 2 ** 128)

    def testFabricFour(self):
        unitFabric = UnitFourFabric()
        unit = unitFabric.getCard()
        self.assertEqual(8, unit.hpRate)
        self.assertEqual(2, unit.manaRate)
        self.assertEqual(4, unit.attackRate)
        self.assertTrue(0 <= unit.cardID <= 2 ** 128)


class TestUnitSystem(unittest.TestCase):
    def testAttackOne(self):
        unitFabricOne = UnitOneFabric()
        unitFabricThree = UnitThreeFabric()
        left = unitFabricOne.getCard()
        right = unitFabricThree.getCard()
        left.attack(right)
        self.assertTrue(left.is_alive())
        left.attack(right)
        self.assertTrue(not left.is_alive())
        self.assertTrue(right.is_alive())

    def testAttackTwo(self):
        unitFabricTwo = UnitTwoFabric()
        unitFabricFour = UnitFourFabric()
        left = unitFabricTwo.getCard()
        right = unitFabricFour.getCard()
        left.attack(right)
        self.assertTrue(left.is_alive())
        left.attack(right)
        self.assertTrue(not left.is_alive())
        self.assertTrue(right.is_alive())


if __name__ == '__main__':
    unittest.main()