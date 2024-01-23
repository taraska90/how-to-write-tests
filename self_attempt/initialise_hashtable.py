from self_attempt.hashtable_self import HashTable

def main():
    sample_table = HashTable(capacity=20)
    sample_table["hola"] = "hello"
    sample_table[98.6] = 37
    sample_table[False] = True
    return sample_table

if __name__ == "__main__":
    print("pass")
