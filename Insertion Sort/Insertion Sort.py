Arr = [4,3,2,10,12,1,5,6]
print("Unsorted Array : ",Arr)

for blueP in range(1,len(Arr)):
    for blackP in range(0,blueP):
        if Arr[blueP] < Arr[blackP]:
            Temp = Arr[blueP]
            for redP in range(blueP,blackP,-1):
                Arr[redP] = Arr[redP-1]
            Arr[blackP] = Temp

print("Sorted Array : ",Arr)
