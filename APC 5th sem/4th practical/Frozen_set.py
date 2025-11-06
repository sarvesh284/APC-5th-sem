conso=frozenset[('f','B','C','D')]
vow=frozenset(['a','e','i','o','u'])
a=frozenset([1,4,9,16,25,36])
num=frozenset([1,2,3,4,5,6])
print(conso)#frozenset['f', 'B', 'C', 'D']
print(a.union(num))#frozenset({1, 2, 3, 4, 36, 5, 6, 9, 16, 25})
# to use union operation the datatype of element in both sets should be same
print(conso.union(vow))#frozenset({'a', 'o', 'i', 'e', 'u'})

print(a.intersection(num))#frozenset({1, 4})
print(a.difference(num))#frozenset({16, 9, 36, 25})
print(a.issubset(num))#False
print(a.issuperset(num))
