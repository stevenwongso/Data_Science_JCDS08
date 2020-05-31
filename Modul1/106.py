# set / himpunan

# x = {1, 2, 3} 
# # print(x[0]) Error karena set sifatnya tidak punya index
# # x.sort tidak bisa 
# print(x)

# # elemen harus unik
# x = {1, 2, 3, 3, 2, 1, "andi"}
# print(x)
# print(type(x))

# x = [1,2,3,4,1,2,3]
# y = tuple(x)
# za = set(x)
# zb = set(y)
# print (za)
# print (zb)

# Set itu Mutable
# y = {1, 2, [5, 6]} 
# print (y) # Error karena elemennya harus immutable 
# y = {(5,6), 1, 2}
# print (y)
# print (1 in y)
# print (1 not in y)
# print (len(y))

# a U b
# {1,2,3,4,5,6}
# a n b
# {3}
# a-b (hanya ada di a)
# {1, 2}
# symmetric diff
# {1,2,4,5,6}

# a = {1,2,3}
# b = {3,4,5,6}

# #  union (U)
# print (a | b)
# print (a.union(b))

# # intersection (n)
# print (a & b)
# print (a.intersection(b))

# # difference
# print (a - b)
# print (a.difference(b))

# # symmetric difference
# print (a ^ b)
# print (a.symmetric_difference(b))

# A = {2, 4, 6, 8, 10, 12, 14, 16, 18}
# B = {3, 5, 7, 9, 11, 13, 15, 17, 19}
# C = {-9, -8, -7, -6, -5, -4, -3, -2, -1}
# D = {2, 3, 5, 7, 11, 13, 17, 19}
# E = {4, 6, 8, 9 , 10, 12, 14, 15, 16, 18}

# print (A | B | C | D | E)
# print ((A & B) | (D & E))
# print ((A | B) & ( D | E))
# print ((A | B) - (D | E))
# print ((A | B | C) - (A & E))

# A = {1,2,3}

# A.add("Budi") #add bener-bener satu elemen
# A.add(('a','b','c'))
# print(A)

# A.update((5, 6)) #update beberapa elemen yang iterable
# A.update("Caca") #kehitung 4 elemen
# A.update([8,9,7]) #kehitung 3 elemen, listnya hilang
# print(A)

# A.remove(1)
# A.discard(('a','b','c'))
# A.clear()
# print (A)

#frozenset

# x = {1,2,3}
# y= frozenset(x)
# print(y)
# print(type(y))