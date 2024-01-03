import pytest
from hashtable import HashTable

@pytest.fixture
def hash_table():
    sample_data = HashTable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data


def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

def test_should_create_empty_value_slots():
    # Given
    expected_values = [None, None, None]
    hashtable = HashTable(capacity=3)
    # When
    actual_values = hashtable.pairs
    # Then
    assert expected_values == actual_values

def test_should_insert_key_value_pairs():
    # Given
    hash_table = HashTable(capacity=100)

    #When
    hash_table['hola'] = 'hello'
    hash_table[98.6] = 37
    hash_table[False] = True

    #Then
    assert "hello" in hash_table.pairs
    assert 37 in hash_table.pairs
    assert True in hash_table.pairs
    assert len(hash_table) == 100

def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).pairs


def test_should_insert_none_values():
    #given
    hash_table = HashTable(capacity=100)
    #when
    hash_table['key'] = None
    #then
    assert None in hash_table.pairs

def test_should_find_value_by_key(hash_table):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True


def test_should_rise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

def test_should_find_key(hash_table):
    assert "hola" in hash_table

def test_should_not_find_key(hash_table):
    assert "missing_key" not in hash_table

def test_should_get_value(hash_table):
    assert hash_table.get("hola") == "hello"

def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get("missing_key") is None

def test_should_get_default_when_missing_key(hash_table):
    assert hash_table.get("missing_key", "default") == "default"

def test_should_get_value_with_default(hash_table):
    assert hash_table.get("hola", "default") == "hello"

def test_should_del_key_value_pair(hash_table):
    assert "hola" in hash_table
    assert "hello" in hash_table.pairs
    del hash_table['hola']
    assert 'hola' not in hash_table
    assert "hello" not in hash_table.pairs
    assert len(hash_table) == 100


def test_should_rise_error_when_del_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        del hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"

def test_should_update_value(hash_table):
    assert hash_table["hola"] == 'hello'

    hash_table["hola"] = "hallo"

    assert hash_table["hola"] == "hallo"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
    assert len(hash_table) == 100

def test_should_return_pairs(hash_table):
    assert ("hola", "hello") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs