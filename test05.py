import unittest
import json
from urllib import request
from urllib.parse import quote
from config import test_config

# {server_name}/{API_ver}/regions?q=рск
# проверка поиска по не валидной подстроке 2 символа

class TestCase(unittest.TestCase):

    API_name = "regions"
    query_param = "?q="
    query_value = "11"

    #def setUp(self):

    def test_case_05(self):

        URL = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + format(quote(self.query_value))
        res = request.urlopen(URL, timeout=test_config.response_timeout)
        body = json.loads(res.read().decode("utf8"))
        #print(body)
        assert body["error"], f"Incorrect error message{URL}"
        assert body["error"]["id"], f"Incorrect error message{URL}"
        assert body["error"]["message"]=="Параметр 'q' должен быть не менее 3 символов", f"Incorrect error message{URL}"
    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()