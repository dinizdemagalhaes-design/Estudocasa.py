numbers = ["Texto", True, 10, 5, 7, 2, 1]
print(f"Valor:, {numbers [4]}")
numbers[4] = 8
print(f"Valor:, {numbers[4]}")
numbers[4] ='Agora texto'
print(f"Valor:, {numbers[4]}")
print(f"Valor:, {numbers}")
print("Tamanho", len(numbers))
del numbers [1]
print (numbers)
print (numbers[-1])
numbers.insert(3, "Outro")
numbers.append("Mais um")
print(f"Valor: {numbers}")
