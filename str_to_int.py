import unittest
from ddt import ddt, data

cases = [
    ('', '⾮int字符，不能转为int'),
    ('12345', 12345),
    ('abc', '⾮int字符，不能转为int'),
    ('3.14', '⾮int字符，不能转为int')
]


def str_to_int(str_param:str):

    if str_param.isdigit():
        results = int(str_param)
    else:
        results = '⾮int字符，不能转为int'
    return results


@ddt
class TestStrToInt(unittest.TestCase):
    @data(*cases)
    def test_str_to_int(self, item):
        self.assertEqual(item[1], str_to_int(item[0]))