

#multiplying numbers
def multiply():
    try:
        num1 = int(input("enter num 1:"))
        num2 = int(input("enter num 2:"))
        print("the multiplication of {} * {} is " .format(num1, num2) ,num1*num2)
    except ValueError:
        print("the erroe is acuure")

multiply()


#string input 
def string():
    try:    
        print("string input")

        name = str(input("Enter name : "))

        print("Hello mrs:",name)
    except ValueError:
        print("the erroe is acuure")
    # under the finally will axcute if the error accur or not 
    finally:
        print("finaly good by")

string()