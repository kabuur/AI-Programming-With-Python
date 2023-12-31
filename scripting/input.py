#multiplying numbers
def multiplying():
    num1 = int(input("enter num 1:"))
    num2 = int(input("enter num 2:"))

    print("the multiplication of {} * {} is " .format(num1, num2) ,num1*num2)



#string input 
def string_input():
    print("string input")

    name = str(input("Enter name : "))

    print(name)


# List Input
def list_input():
    List_sum = 0
    List_num = []

    for i in range(5):
        # or use userInput instead of i 
        userInput = int(input("Enter any number: "))
        try:
            List_num.append(i)
            if i % 2 == 0:
                List_sum += i
        except ValueError:
            print("Incorrect value. That's not an int!")
    print("user_list: {}".format(List_num))
    print("The sum of the even numbers in user_list is: {}.".format(List_sum))





   



list_input()
