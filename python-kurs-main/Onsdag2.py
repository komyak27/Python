tall=int(input("Hvilken gangetabel? "))
grense=int(input("Hvor lenge skal telle?"))
for i in range(1,grense + 1):
    print(tall, "x", i, "=", tall * i)