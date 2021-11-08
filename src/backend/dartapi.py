import os
import logging
import tempfile
import requests
import zipfile
import string
import random
from xml.etree.ElementTree import parse


log = logging.getLogger(f"app.{__name__}")


def make_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


CHUNK_SIZE = 1024 * 1024


class DartAPI:
    def __init__(self):
        self.API_KEY = os.environ.get("DART_API_KEY")

    def get_corp_code(self):
        params = {"crtfc_key": self.API_KEY}
        r = requests.get("https://opendart.fss.or.kr/api/corpCode.xml", params=params)
        r.raise_for_status()

        with tempfile.NamedTemporaryFile(prefix="tmp-", delete=False) as f:
            for chunk in r.iter_content(CHUNK_SIZE):
                f.write(chunk)
            corp_code = f.name
            log.debug("corp code downloaded. %s", corp_code)

        with zipfile.ZipFile(corp_code) as f:
            with tempfile.TemporaryDirectory() as tmpdirname:
                f.extractall(tmpdirname)
                corp_xml_file = os.path.join(tmpdirname, "CORPCODE.xml")
                # log.debug("corp xml file. %s", corp_xml_file)
                return self._parse_corp_file(corp_xml_file)

    def _parse_corp_file(self, corp_xml_file):
        tree = parse(corp_xml_file)
        root = tree.getroot()
        corp_list = root.findall("list")

        return [
            {
                "corp_code": corp.findtext("corp_code"),
                "corp_name": corp.findtext("corp_name"),
                "stock_code": corp.findtext("stock_code"),
                "modify_date": corp.findtext("modify_date"),
            }
            for corp in corp_list
        ]
