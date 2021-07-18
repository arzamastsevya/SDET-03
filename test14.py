import unittest
import json
from urllib import request
from urllib.parse import quote
from config import test_config

# {server_name}/{API_ver}/regions?page=1
# проверяет что города в выдаче на разных
# страницах не дублируются

class TestCase(unittest.TestCase):

    API_name = "regions"
    query_param = "?page="
    query_value = "1"

    #def setUp(self):

    def test_case_14(self):

        page = 1
        body_2 = {"items":""}

        while body_2["items"]!=[] or page>5:

            URL_1 = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + str(page)
            res = request.urlopen(URL_1, timeout=test_config.response_timeout)
            body_1 = json.loads(res.read().decode("utf8"))
            #print(URL_1)
            #print(body_1, "\n")

            URL_2 = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name + self.query_param + str(page+1)
            res = request.urlopen(URL_2, timeout=test_config.response_timeout)
            body_2 = json.loads(res.read().decode("utf8"))
            #print(URL_2)
            #print(body_2, "\n")

            if body_2["items"]!=[]:
                for i in body_1["items"]:        
                    #print(i, (i not in body_2["items"]))
                    assert i not in body_2["items"], f"\n{URL_1}\n{URL_2}\nDuplicated value\n{i}"
            #print("\n")
            page += 1
      
    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()