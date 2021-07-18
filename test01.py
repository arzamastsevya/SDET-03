import unittest
import json
from urllib import request
from config import test_config

# {server_name}/{API_ver}/regions
# проверка структуры данных в ответе
# проверка по умолчанию page_size=15
# проверка что "total" > 0

class TestCase(unittest.TestCase):

    API_name = "regions"

    #def setUp(self):

    def test_case_01(self):

        URL = test_config.server_name + "/" + test_config.API_ver + "/" + self.API_name
        res = request.urlopen(URL, timeout=test_config.response_timeout)
        body = json.loads(res.read())

        items = len(body["items"])

        assert items==15, f"\n{URL}\nNot correct number of items by default 15 but {items}"
        assert body["total"]>0 , f"\n{URL}\nNo \"total\" in response"
        
        assert "total" in body
        assert "items" in body
        assert "id" in body["items"][0]
        assert "name" in body["items"][0]
        assert "code" in body["items"][0]
        assert "name" in body["items"][0]["country"]
        assert "code" in body["items"][0]["country"]

    #def tearDown(self):

if __name__ == "__main__":
    unittest.main()