import unittest
import json
from urllib import request
from urllib.parse import quote
from config import test_config

# {server_name}/{API_ver}/regions?q=рск
# регистр не имеет значения
# ВЕРХНИЙ РЕГИСТР нижний регистр

class TestCase(unittest.TestCase):

    API_name = "regions"
    query_param = "?q="
    query_value = "РсК"

    #def setUp(self):

    def test_case_06(self):

        URL = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + format(quote(self.query_value))
        res = request.urlopen(URL, timeout=test_config.response_timeout)
        body = json.loads(res.read().decode("utf8"))
        #print(body)
        for i in body["items"]:
            assert self.query_value.lower() or self.query_value.lower()[0].upper() in i["name"], f"\n{URL}\nNot found {self.query_value}"

    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()