import unittest
import json
from urllib import request
from urllib.error import HTTPError
from urllib.parse import quote
from config import test_config

# {server_name}/{API_ver}/regions?page=1
# проверяет что page=1 по умолчанию


class TestCase(unittest.TestCase):

    API_name = "regions"
    query_param = "?page="
    query_value = "1"

    #def setUp(self):

    def test_case_19(self):

        URL_01 = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name
        #print(URL)
        res = request.urlopen(URL_01, timeout=test_config.response_timeout)
        body_01 = json.loads(res.read().decode("utf8"))

        URL_02 = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + format(quote(self.query_value))
        #print(URL)
        res = request.urlopen(URL_02, timeout=test_config.response_timeout)
        body_02 = json.loads(res.read().decode("utf8"))

        assert body_01 == body_02, f"\n{URL_01}\n{URL_02}\nРage 1 is not default"

    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()