from unittest import TestCase
from source.accounting.hourlyemployee import HourlyEmployee

class TestHourlyEmployee(TestCase):
    def test_clockIn(self):
        s = HourlyEmployee
        self.assertRaises(Exception,s.clockIn,[-6,-5,-2102],-10)

    def test_clockOut(self):
        s = HourlyEmployee
        self.assertRaises(Exception, s.clockIn, [-6, -5, -2102], -10)

    def test_getList(self):
        pass

    def test_pay(self):
        s = HourlyEmployee
        self.assertRaises(Exception, s.pay, [8,7,2016],[6/7/2016])
