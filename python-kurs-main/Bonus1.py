student = input("Er du student (ja/nei) ")

if student == "ja": 
    print ("30kr")
else:
    alder = int(input("Skriv din alder"))
    if alder <= 12:
        print ("25kr")
    elif alder <= 55:
        print ("50kr")
    else:
        print ("30kr")