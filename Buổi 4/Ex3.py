print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x+3) ?")
ds = {
    '1.':35,
    '2.':36,
    '3.':40,
    '4.':44
}
tl = 4
for k,v in ds.items():
    print(k,'',v)
your_choice = int(input("Your choice:"))
if your_choice == tl:
    print("Bingo")
else:
    print(":(")

