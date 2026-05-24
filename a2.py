numberLargest = int(input("enter Largest number: "))
numberSmallest = int(input("enter Smallest number: "))

while (numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is ",numberLargest)