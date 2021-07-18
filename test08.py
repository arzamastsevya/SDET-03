import unittest
import json
from urllib import request
from urllib.parse import quote
from config import test_config

# {server_name}/{API_ver}/regions?q=рск
# если передан этот параметр, все остальные игнорируются

class TestCase(unittest.TestCase):

    API_name = "regions"
    query_param = "?q="
    query_value = "рск"

    #def setUp(self):

    def test_case_08(self):

        URL = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + \
        format(quote(self.query_value)) + "&country_code=ru&page=1&page_size=5"
        #print(URL)
        res = request.urlopen(URL, timeout=test_config.response_timeout)
        body = json.loads(res.read().decode("utf8"))
        #print(body)
        for i in body["items"]:
            assert self.query_value.lower() or self.query_value.lower()[0].upper() in i["name"], f"\n{URL}\nNot found {self.query_value}"

    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()