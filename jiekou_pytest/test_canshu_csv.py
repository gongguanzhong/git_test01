# coding:utf-8
import requests
import pytest
import csv
import ddt
import xlrd


def csv_redeFile():
    bid_info = csv.DictReader(open('jiangxi.csv', 'r', encoding='utf-8'))
    dict_data = []
    for lines in bid_info:
        if bid_info.line_num == 1:
            continue
        else:
            dict_data.append(lines)
    return dict_data


@pytest.fixture(scope="module")
def request_01(request):
    division = request.param["division"]
    level = request.param["level"]
    pre = request.param["pre"]
    province = request.param["province"]
    print("division为{0}".format(division))
    print("level为{0}".format(level))
    print("pre为{0}".format(pre))
    print("province为{0}".format(province))
    post_url = "http://47.111.174.105:8080/volunteer/unpaidPlan"

    post_params = {
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

    r = requests.post(post_url, json=post_params, verify=False)
    result = r.json()
    return result['code']


@pytest.mark.parametrize("request_01", csv_redeFile(), indirect=True)
def test_request(request_01):
    result = request_01
    assert result == '0'


if __name__ == "__main__":
    pytest.main(['-s', 'pytest_canshu_csv.py'])