import unittest
import json
from urllib import request
from urllib.parse import quote
from config import test_config

# {server_name}/{API_ver}/regions?q=111
# проверка поиска по не валидной подстроке 3 символа

class TestCase(unittest.TestCase):

    API_name = "regions"
    query_param = "?q="
    query_value = "111"

    #def setUp(self):

    def test_case_04(self):

        URL = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + format(quote(self.query_value))
        res = request.urlopen(URL, timeout=test_config.response_timeout)
        body = json.loads(res.read().decode("utf8"))
        #print(body)
        assert body["items"]==[], f"\n{URL}\nEmpty array nothing found"

    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()