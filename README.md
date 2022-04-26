# Hash-table
The program implements a hash table, and use it to answer queries about word frequencies in the input text.

The class HashMap that implements a map (i.e. dictionary) using a hash table. It provides the following methods:

m.set(key, value) - adds the mapping (key -> value) to a hash table, replacing any previous value for the given key

m.get(key) - looks up a key and returns its value, or None if it is not present

m.remove(key) - removes a key from the hash table if present

Whenever the hash table's load factor exceeds 4, the program doubles the number of hash buckets. (Recall that the load factor is the number of keys in the table divided by the number of buckets, i.e. the average length of a hash chain.)

Each time the number of buckets increases, print a message like this:
"resizing to 10 buckets"
