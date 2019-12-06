#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    #enumerate(iterable, start=0)
    for i,w in enumerate(weights):
        hash_table_insert(ht,w,i)
    
    for i,w in enumerate(weights):
        f = hash_table_retrieve(ht, limit - w)
        if f is not None:
            if f>i:
                return (f,i)
            else:
                return(i,f)
    """
    Given a package with a weight limit `limit` and a list `weights` of item weights, implement a function 
    `get_indices_of_item_weights` that finds two items whose sum of weights equals
     the weight limit `limit`. Your function will return an instance of an `Answer` tuple that has the following form:
```
(zero, one)
```
where each element represents the item weights of the two packages. _**
The higher valued index should be placed in the `zeroth` index and the smaller index should be placed in the `first` index.**_
 If such a pair doesn’t exist for the given inputs, your function should return `None`.

_NOTE:_ When calling `hash_table_retrieve` with a key that doesn't exist in the hash table, `hash_table_retrieve` will return `None`. 

Your solution should run in linear time.
    """

    


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
