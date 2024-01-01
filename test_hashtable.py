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