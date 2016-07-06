from unittest import TestCase
from source.accounting.salariedemployee import SalariedEmployee

class TestSalariedEmployee(TestCase):
    def test_makeSale(self):
        s = SalariedEmployee
        self.assertRaises(Exception, s.makeSale, [-6, -5, -2102], -10)

    def test_getList(self):
        pass

    def test_pay(self):
        s = SalariedEmployee
        self.assertRaises(Exception, s.pay, [8, 7, 2016], [6 / 7 / 2016])
