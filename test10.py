import unittest
import json
from urllib import request
from urllib.parse import quote
from config import test_config

# {server_name}/{API_ver}/regions?country_code=ru
# параметр country_code=ru

class TestCase(unittest.TestCase):

    API_name = "regions"
    query_param = "?country_code="
    query_value = "kg"

    #def setUp(self):

    def test_case_10(self):

        page = 1
        body={"items": ""}
        while body["items"]!=[] or page > 5:
            URL = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + format(quote(self.query_value)) + "&page=" + str(page)
            res = request.urlopen(URL, timeout=test_config.response_timeout)
            body = json.loads(res.read().decode("utf8"))
            page += 1
            #print(URL)
            #print(body, "\n")
            for i in body["items"]:
                #print(i["country"]["code"])
                assert self.query_value.lower() == i["country"]["code"], f"Not found {self.query_value} \n {URL}"
            
    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()