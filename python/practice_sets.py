# x = {1,2,3,4,5,6}
# print(x)

# x={1,2,3,4}
# x.add(25)
# print(x)

# x={1,3,5,7,9}
# y={'apple','mango'}
# x.update(y)
# print(x)

# x = {1, 3, 5, 7, 9, 'apple', 'mango'}
# x.discard('apple')
# print(x)

# x = {1, 3, 5, 7, 9, 'apple', 'mango'}
# x.pop()
# print(x)

# x = {1, 3, 5, 7, 9, 'apple', 'mango'}
# x.clear()
# print(x)

# fruits = {'apple','mango','orange','banana'}
# item = 'apple'
# if item in fruits:
#     print(f"item in fruits is {item}",)
# else:
#     print("item is not there")

# x = {1, 3, 5, 7, 9, 'apple', 'mango'}
# y = {2,4,7,0,4}
# z = x.union(y)
# print(z)

# x = {1, 3, 5, 7, 9, 'apple', 'mango'}
# y = {2,4,7,0,4}
# z = x.intersection(y)
# print(z)

# x = {1, 3, 5, 7, 9, 'apple', 'mango'}
# y = {2,4,7,'apple','mango'}
# z = x.difference(y)
# print(z)

# x = {1, 3, 5, 7, 9, 'apple', 'mango'}
# y = {2,4,7,0,4}
# z=x.symmetric_difference(y)
# print(z)

# s = {1,2,3,4,53,32,12}
# sub = {1,2,3,7,78,9}
# check_subset = s.issubset(sub)
# print(check_subset)

# set_a = {1,2,3,4}
# superset_b = {1,2,3,4}
# check_superset = set_a.issuperset(superset_b)
# print(check_superset)

# x = [1,2,3,4,3,4,2,6,8]
# y = set(x)
# print(y)

# x = {1,2,3,4,5}
# y = {i**2 for i in x}
# print(y)

# my_set={2,4,7,5,4}
# for item in my_set:
#     print(item)

# x = {2,4,7,5,4}
# y = x.copy()
# print(y)

# list = [1,2,3,4,4,5,6,3,2,9]
# remove_dep = set(list)
# print(remove_dep)

# string = "hello world"
# unique_char = set(string)
# print(unique_char)

# my_set = set()

# my_set.add(10)
# my_set.add(20)
# my_set.add(30)
# my_set.add(40)
# my_set.add(50)

# print(my_set)

# unique = [1,2,4,3,4,2,5,5,7,8]
# unique_set = set()
# for num in unique:
#     unique_set.add(num)
# print("Unique numbers:",unique_set)

# set1 = {1,2,3,4,5}
# set2 = {6,7,8,9}
# print(set1.isdisjoint(set2))


# mutable_set = {1,2,3}
# mutable_set.add(4)
# print(mutable_set)

# immutable_set = frozenset([1,2,3])
# immutable_set.add(6)
# print("Frozenset:", immutable_set)

# tuple = (1,3,5,3,2,6)
# print(set(tuple))

# set = {1, 3, 5, 7, 9, 'apple', 'mango'}
# print(list(set))

# set1 = {1,2,3}
# set2 = {4,5,6}
# set3 = {7,8,9}
# merge = set1.union(set2,set3)
# print(merge)

# x = [1, 3, 5, 7, 9, 'apple', 7,8,9,'mango']
# set_allowed = {'apple',3,5,7,'mango'}
# filtered = [i for i in x if i in set_allowed]
# print("Filtered list:", filtered)

# sentence = "python is easy and python is easy to code"
# words = sentence.split()
# unique_words = set(words)
# print("Unique Words:",unique_words)


# set = { i for i in range(1,51) if i%2==0}
# print(set)

string = "Hello world"
unique_code =set(string)
for i in unique_code:
    print(f"charcter:'{i} ->ASCII: {ord(i)}")