from hashtable_self import HashTable,BLANK

sample_data = HashTable(capacity=3)
sample_data["hola"] = "hello"
sample_data[98.6] = 37
sample_data[False] = True
print(sample_data.values)
print(sample_data["missing"])