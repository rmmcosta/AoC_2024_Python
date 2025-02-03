from unittest import TestCase

from day2RedNosedReports import is_safe, Report


class Test(TestCase):
    def test_is_safe(self):
        report = Report([1, 2, 3, 4, 5])
        assert (is_safe(report))

    def test_is_not_safe(self):
        report = Report([10, 11, 13, 16, 15])
        assert (not is_safe(report))
        report = Report([43, 46, 49, 52, 54, 58])
        assert (not is_safe(report))

