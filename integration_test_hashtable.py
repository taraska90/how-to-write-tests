from hashtable import *

def initialize_table():
    sample_data = HashTable(capacity=3)
    sample_data["test1"] = "test1"
    sample_data["test2"] = "test2"
    return sample_data

def check_pairs():
    table = initialize_table()
    print(table.pairs)


if __name__ == "__main__":
    check_pairs()