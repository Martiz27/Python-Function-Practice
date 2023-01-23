#Function 1
def hello():
    print("Hello, User!")

#Function 2
def pack(a, b, c):
    return [a, b, c]

#Function 3
def eat_lunch(my_list):
    if len(my_list) == 0:
        print("Lunch box is Empty!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")

hello()
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["Pizza"])
eat_lunch(["Peach","Cookie", "Steak"])