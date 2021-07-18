import unittest
import json
from urllib import request
from urllib.error import HTTPError
from urllib.parse import quote
from config import test_config

# {server_name}/{API_ver}/regions?page=
# проверяет что нормально обрабатывается ошибка

class TestCase(unittest.TestCase):

    API_name = "regions"
    query_param = "?page="
    query_value = "-1"

    #def setUp(self):

    def test_case_17(self):

        URL = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + format(quote(self.query_value))
        #print(URL)
        res = request.urlopen(URL, timeout=test_config.response_timeout)
        body = json.loads(res.read().decode("utf8"))
        #print(body)
        assert body["error"], f"\n{URL}\Incorrect error message"
        assert body["error"]["message"]=="Параметр 'page' должен быть больше 0", f"\n{URL}\Incorrect error message"
    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()