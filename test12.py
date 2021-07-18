import unittest
import json
from urllib import request
from urllib.parse import quote
from config import test_config

# {server_name}/{API_ver}/regions?country_code=ru
# параметр country_code=11 сообщение об ошибке

class TestCase(unittest.TestCase):

    API_name = "regions"
    query_param = "?country_code="
    query_value = "11"

    #def setUp(self):

    def test_case_12(self):

        URL = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + format(quote(self.query_value))
        res = request.urlopen(URL, timeout=test_config.response_timeout)
        body = json.loads(res.read().decode("utf8"))
        #print(URL)
        #print(body, "\n")
        assert body["error"], "Incorrect error message"
        assert body["error"]["id"], "Incorrect error message"
        assert body["error"]["message"]=="Параметр 'country_code' может быть одним из следующих значений: ru, kg, kz, cz"
            
    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()