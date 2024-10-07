fila = [5,2]
value_conjunto = int(input("Valor: "))
if value_conjunto not in fila:
    fila.append(value_conjunto)
else:
    print("Valor ja contido na fila")
print(fila)