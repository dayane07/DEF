contador = 0

def incrementar ():
  global contador
  contador += 1
  print(f"O contador foi incrementado. novo valor: {contador}")

  print(f"Valor inicial do contador: {contador}")
  print("---")

incrementar()
incrementar()
incrementar()

print("---")
print(f"Valor final do contador: {contador}")