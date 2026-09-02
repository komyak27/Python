alder = int(input("Skriv din alder: "))
if alder < 6:
    print("Gratis")
elif alder <= 17:
    print("50kr")
elif alder <= 67:
    print("100kr")
else:
    print("50kr")