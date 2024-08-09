# Tuples are immutable and ordered
tuple1 = (1, 4, 6, 7)
tuple2 = (2, 3, 9, "aabsb")

tuple3 = tuple1 + tuple2
tuple4 = (tuple1, tuple2)

# print(type(tuple4))
# print(tuple3)

my_tuple = ("DS_III",)
n = 6
for i in range(6):
    my_tuple = (my_tuple,)
    print(my_tuple)