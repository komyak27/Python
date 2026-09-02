start = int(input("Hva er start "))
steg = int(input("Hva er steg "))
slutt = int(input("Hva er slutt"))
sum_number = 0

if steg > 0:
    for number in range(start, slutt+1, steg):
        print (number)
        sum_number = sum_number + number
else:
    for number in range(start, slutt-1, steg):
        print (number)
        sum_number = sum_number + number
print(sum_number)