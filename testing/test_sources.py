
import pytest
from debian_parser.parser import PackagesParser

@pytest.fixture
def packages_file():
    return open("testing/sample_files/Sources", 'r').read()


def test_expectation_number(packages_file):
    obj = PackagesParser(packages_file)
    assert obj._splitted_lines() == 4

def test_packages_parse_list(packages_file):
    obj = PackagesParser(packages_file)
    assert len(obj._parse_to_seperated_lists()) == 4
    assert len(obj._parse_to_seperated_lists()) == obj._splitted_lines()

    for sub_list in obj._parse_to_seperated_lists():
        assert sub_list != []
        assert len(sub_list) != 0
        for element in sub_list:
            assert element != ""


def test_packages_dict(packages_file):
    obj = PackagesParser(packages_file)
    parse_to_dict = obj._parse_to_dict()
    
    assert len(parse_to_dict) == len(obj._parse_to_seperated_lists())
    
    for list_test in parse_to_dict:
        for element in list_test:
            assert element.get("tag", False) != False
            assert element['tag'] != ""
            
            assert element.get("value", False) != False
            assert element['value'] != ""
