import unittest
import json
from urllib import request
from urllib.error import HTTPError
from urllib.parse import quote
from config import test_config

# {server_name}/{API_ver}/regions?page_size=5
# проверяет что количество элементов соответствует
# значению параметра

class TestCase(unittest.TestCase):

    API_name = "regions"
    query_param = "?page_size="
    query_value = "5"

    #def setUp(self):

    def test_case_20(self):

        URL = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + format(quote(self.query_value))
        res = request.urlopen(URL, timeout=test_config.response_timeout)
        body = json.loads(res.read().decode("utf8"))
        assert str(len(body["items"])) == self.query_value, f"\n{URL}\nThe number of elements is not {self.query_value}"
       
    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()