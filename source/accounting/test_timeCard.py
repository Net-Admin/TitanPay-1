from unittest import TestCase
from source.accounting.timecard import TimeCard

class TestTimeCard(TestCase):
    def test_setDate(self):
        pass

    def test_setStart(self):
        pass

    def test_setEnd(self):
        pass

    def test_getDate(self):
        pass

    def test_calculate_daily_pay(self):
        s = TimeCard
        self.assertRaises(Exception, s.calculate_daily_pay, -10)
