pris = int(input("Skriv prisen" ))
antall = int(input("Skriv antall" ))
rabat_prossent = int(input("Skriv rabat"))
totalpris = pris * antall
rabat_kroner = totalpris * rabat_prossent / 100
ny_pris = totalpris - rabat_kroner

print("Rabat prossent er", rabat_prossent )
print("Totalpris er", totalpris )
print("Rabat kroner er", rabat_kroner )
print("Ny prisen er", ny_pris )
