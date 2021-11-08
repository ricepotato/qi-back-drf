import os
import unittest
import dotenv
from backend.dartapi import DartAPI
from xml.etree.ElementTree import parse


class DartAPITestCase(unittest.TestCase):
    def tearDown(self):
        pass

    def setUp(self):
        os.environ["DART_API_KEY"] = "6f4e65b37682ae4903523e64457c96888e601585"
        self.api = DartAPI()

    def _test_parse_corpcode(self):
        corp_list = self.api.get_corp_code()
        assert corp_list
        corp_map = {}
        for corp in corp_list:
            corp_map[corp["corp_code"]] = corp

        assert corp_map["00434003"]["name"] == "다코"

    def test_parse_xml(self):
        corp_list = self.api._parse_corp_file("src/tests/CORPCODE.xml")
        assert corp_list
        corp_map = {}
        for corp in corp_list:
            corp_map[corp["corp_code"]] = corp

        assert corp_map["00434003"]["corp_name"] == "다코"
        assert corp_map["00415053"]["corp_name"] == "화진코스메틱"
        assert corp_map["00427429"]["corp_name"] == "산은굿밸류제일차유동화전문유한회사"
        assert corp_map["00669274"]["corp_name"] == "동성이앤지"
