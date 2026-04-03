from main import get_most_active_cookies

def test_basic():
    result = get_most_active_cookies("test_cases/test1.csv", "2018-12-09")
    assert result == ["AtY0laUfhglK3lC7"]

def test_tie():
    result = get_most_active_cookies("test_cases/test2.csv", "2018-12-09")
    assert set(result) == {"A", "B"}

def test_no_data():
    result = get_most_active_cookies("test_cases/test3.csv", "2018-12-09")
    assert result == []

def test_empty_file():
    result = get_most_active_cookies("test_cases/test4.csv", "2018-12-09")
    assert result == []
    
def test_single():
    result = get_most_active_cookies("test_cases/test5.csv", "2018-12-09")
    assert result == ["A"]