Arr = ['A','B','C','D','E','F','G','H','I','J']

def BinarySearching(Value):
    LB = 0
    UB = len(Arr)-1
    while LB <= UB:
        Mid = int((UB + LB)/2)
        if Arr[Mid] == Value:
            return Mid
        elif Arr[Mid] < Value:
            LB = Mid + 1
        else:
            UB = Mid - 1
    return -1

#MENU
choice = 0
while choice != 3:
    print("1 : Print the Array")
    print("2 : Search Value")
    print("3 : Exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        print(Arr)
    elif choice == 2:
       SearchValue = str(input("Enter Search Value : "))
       Ans = BinarySearching(SearchValue)
       if Ans == -1:
           print("Value not Found")
       else:
           print("The position where the value is : ",Ans)
    elif choice == 3:
        print("Exitting.....")
    else:
        print("Invalid Option")


