import pytest
from hashtable import HashTable

def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100

def test_should_create_empty_value_slots():
    # Given
    expected_values = [None, None, None]
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

@pytest.mark.skip
def test_should_not_shrink_when_removing_elemnts():
    pass