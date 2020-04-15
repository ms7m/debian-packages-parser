
import pytest
from debian_parser.parser import PackagesParser

@pytest.fixture
def packages_file():
    return open("testing/sample_files/Packages", 'r').read()

@pytest.fixture
def multi_line_packages_file():
    return open("testing/sample_files/Packages_Multi_Line", 'r').read()


def test_multiline_packages_expectation_number(multi_line_packages_file):
    obj = PackagesParser(multi_line_packages_file)
    assert obj._splitted_lines() == 3

def test_multiline_packages_parse_list(multi_line_packages_file):
    obj = PackagesParser(multi_line_packages_file)
    assert len(obj._parse_to_seperated_lists()) == 3
    assert len(obj._parse_to_seperated_lists()) == obj._splitted_lines()

    for sub_list in obj._parse_to_seperated_lists():
        assert sub_list != []
        assert len(sub_list) != 0
        for element in sub_list:
            assert element != ""


def test_multiline_packages_dict(multi_line_packages_file):
    obj = PackagesParser(multi_line_packages_file)
    parse_to_dict = obj._parse_to_dict()
    
    assert len(parse_to_dict) == len(obj._parse_to_seperated_lists())
    
    for list_test in parse_to_dict:
        for element in list_test:
            assert element.get("tag", False) != False
            assert element['tag'] != ""
            
            assert element.get("value", False) != False
            assert element['value'] != ""

def test_multiline_expectation_number(multi_line_packages_file):
    obj = PackagesParser(multi_line_packages_file)
    assert obj._splitted_lines() == 3

def test_expectation_number(packages_file):
    obj = PackagesParser(packages_file)
    assert obj._splitted_lines() == 3

def test_packages_parse_list(packages_file):
    obj = PackagesParser(packages_file)
    assert len(obj._parse_to_seperated_lists()) == 3
    assert len(obj._parse_to_seperated_lists()) == obj._splitted_lines()

    for sub_list in obj._parse_to_seperated_lists():
        assert sub_list != []
        assert len(sub_list) != 0
        for element in sub_list:
            assert element != ""
            assert ":" in element.split()[0]


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
