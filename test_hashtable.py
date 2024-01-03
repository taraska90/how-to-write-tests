import pytest
from hashtable import HashTable, BLANK

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
    expected_values = [BLANK, BLANK, BLANK]
    hashtable = HashTable(capacity=3)
    # When
    actual_values = hashtable.values
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
    assert "hello" in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values
    assert len(hash_table) == 100

def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values


def test_should_insert_none_values():
    #given
    hash_table = HashTable(capacity=100)
    #when
    hash_table['key'] = None
    #then
    assert None in hash_table.values

def test_should_find_value_by_key(hash_table):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True


@pytest.mark.skip
def test_should_not_shrink_when_removing_elemnts():
    pass