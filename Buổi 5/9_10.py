def get_even_list(l):
    lc=[]
    for so in l:
        if so % 2==0:
            lc.append(so)
    return lc
# print(get_even_list([1, 4, 5, -1, 10]))

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
