Arr = ['A','B','C','D','E','F','G','H','I','J']
lb = 0
ub = len(Arr)-1
def RecursiveBinarySearching(LB,UB,Value):
    Mid = int((UB +LB)/2)
    if LB > UB:
        return -1
    elif Arr[Mid] == Value:
        return Mid
    elif Arr[Mid] < Value:
        return RecursiveBinarySearching(Mid + 1,UB,Value)
    else:
        return RecursiveBinarySearching(LB,Mid-1,Value)

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
       Ans = RecursiveBinarySearching(lb,ub,SearchValue)
       if Ans == -1:
           print("Value not Found")
       else:
           print("The position where the value is : ",Ans)
    elif choice == 3:
        print("Exitting.....")
    else:
        print("Invalid Option")
