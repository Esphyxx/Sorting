'''
//Psuedocode of Bubble Sort using loops
DECLARE Array : arr[0:9] as Integer
arr = ['5','6','3','8','2','54','72','23','25','26']
C = 0
PROCEDURE Bubble_Sort():
   While Boundary > 0 Do
       Boundary = LEN(arr)-1
       For C = 0 to Boundary-1
           If arr[C] > arr[C+1] THEN
               Temp = arr[C]
               arr[C] = arr[C+1]
               arr[C+1] = Temp
           ENDIf
       END For
       Boundary = Boundary - 1
   ENDWhile
END PROCEDURE
'''

arr = ['5','6','3','8','2','54','72','23','25','26']
print("Array before sorting : ",arr)
C = 0
def Bubble_Sort():
    Boundary = len(arr)-1
    while Boundary > 0:
        for C in range(0,Boundary):
            if int(arr[C]) > int(arr[C+1]):
                Temp = arr[C]
                arr[C] = arr[C+1]
                arr[C+1] = Temp
        Boundary -= 1

Bubble_Sort()
print("Array after sorting : ",arr)    
