import unittest
import json
from urllib import request
from urllib.error import HTTPError
from urllib.parse import quote
from config import test_config

# {server_name}/{API_ver}/regions?page_size=aa
# проверяет обработку не правильного запроса


class TestCase(unittest.TestCase):

    API_name = "regions"
    query_param = "?page_size="
    query_value = "aa"

    #def setUp(self):

    def test_case_27(self):

        URL = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + format(quote(self.query_value))
        #print(URL)
        res = request.urlopen(URL, timeout=test_config.response_timeout)
        body = json.loads(res.read().decode("utf8"))
        #print(body)
        assert body["error"]
        assert body["error"]["message"] == "Параметр 'page_size' длжен быть целым числом", f"\n{URL}\nIncorrect error message"
       
    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()