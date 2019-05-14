items = ["T-Shirt", "Sweater"]
while True:
    print("Welcome to our shop, what do you want (C, R, U, D)?: ",end='')
    n = (input())
    if n == "R":
        print("Our item:",end=' ')
        print(*items,sep=', ')
    elif n == "C":
        new_item = input("Enter new item:")
        items.append(new_item)
        print("Our items:", end ="")
        print(*items, sep=",")
    elif n == "U":
        update_position = int(input("Update position?"))
        new__item = input("New item?")
        items[update_position] = new__item
        print("Our items:", end ="")
        print(*items, sep=",")
    elif n == "D":
        delete_position = int(input("Delete position?"))
        del items[delete_position]
        print("Our items:", end ="")
        print(*items, sep=",")
    else:
        print("Unknown data")
        break