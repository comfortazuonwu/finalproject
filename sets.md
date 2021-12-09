**Sets**

**Introduction**
A set is a data structure that can store any number of unique values in any order you so wish. The difference is between a set and an array is that an array allows repeated values and a set allows only unique values. The python set() method is used to define a set.

``` python
array = [1,3,3,3,4,4,5,6,6]
my_set = set(array)
print(my_set)

{1, 3, 4, 5, 6}

``` 
**Chacteristics of sets**
- Sets are unordered
- Sets only allow unique elements




**Set Operations in Python**

|Set Operation| Explanation | Example | Performance|
|-------------|-------------|----------|-----------|
|add(value)|Adds a value to a set using the  python add() method| set.add(value)|O(1)|
|remove(value)|Removes a value from a set using the python remove() method| set.remove(value)|O(1)|
|size()| Used to find out the lenght of a set using the python len() method| size = len(set)|


Below is an example of how sets work in python

``` python
values = {1,2,3,4,5,6}

my_set = set(values)

my_set.add(2)
print (my_set)

my_set.remove(4)
print (my_set)

length = len(my_set)
print (length)

#code output

{1, 2, 3, 4, 5, 6}
{1, 2, 3, 5, 6}
5
```
We see that when 2 is added to the set, the set doesn't change because 2 was already in the set and it doesn't allow duplicates.



**Problem to solve**
Using a set, determine if there are duplicate letters in the text given

```python

def letters(text):
    """Using a set, determine if there are duplicate letters in the text given. Return true if there are no duplicates and false if there are duplicates"""

pass


test1 = "Pauline"  # Expect True because all letters unique
print(letters(test1))

test2 = "Comfort"  # Expect False because 'o' is repeated
print(letters(test2))

```
When you are done working on this problem, take a look at the [solution](setssolution.py) and compare it to yours.