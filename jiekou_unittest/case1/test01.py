# coding:utf-8
import requests
import unittest
import csv
import ddt
import xlrd


def csv_redeFile():
    bid_info = csv.DictReader(open('E:\\PL-Discover\\jiekou_unittest\\case1\\jiangxi.csv', 'r', encoding='utf-8'))
    dict_data = []
    for lines in bid_info:
        if bid_info.line_num == 1:
            continue
        else:
            dict_data.append(lines)
    return dict_data


@ddt.ddt
class Test_zytb(unittest.TestCase):

    def setUp(self):
        pass

    @ddt.data(*csv_redeFile())
    @ddt.unpack
    def test_01(self, pre, province, level, division):
        self.post_url = "http://47.111.174.105:8080/volunteer/unpaidPlan"

        self.post_params = {
            "area": "",
            "division": division,
            "excludeArea": "",
            "excludeCollege": "",
            "excludeMajor": "",
            "intentionCollege": "",
            "intentionMajor": "",
            "level": level,
            "nature": "",
            "other": 0,
            "precedence": pre,
            "province": province,
            "score": 0,
            "sex": "男",
            "subjects": 0}

        r = requests.post(self.post_url, json=self.post_params, verify=False)
        result = r.json()
        self.assertEqual('0', result['code'], msg=(self.post_params["division"], self.post_params["level"], self.post_params["precedence"], self.post_params["province"]))


if __name__ == "__main__":
    unittest.main()