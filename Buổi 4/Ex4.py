print("Answer the following algebra question:")
print("If x = 8, then what is the value of 4(x+3) ?")
ds = {
    '1.':35,
    '2.':36,
    '3.':40,
    '4.':44
}
tl = 4
dem_tl = 0
for k,v in ds.items():
    print(k,'',v)
your_choice = int(input("Your choice:"))
if your_choice == tl:
    print("Bingo")
    dem_tl +=1
else:
    print(":(")

print("Estimate this answer (exact calculation not needed):")
print("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?")
ds2 = {
    '1.': 'About 55',
    '2.': 'About 65',
    '3.': 'About 75',
    '4.': 'About 85'
}
tl2 = 2
for k,v in ds2.items():
    print(k,'',v)
your_choice2 = int(input("Your choice:"))
if your_choice2 == tl2:
    print("Bingo")
    dem_tl+=1
else:
    print(":(")
print("You correctly answer",dem_tl,"out of 2 questions")