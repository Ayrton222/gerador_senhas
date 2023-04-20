senha = 0
fila = []

while True:
    print("----------------------------------------------------------------------")
    print("Digite 1 para retirar sua senha")
    print("Digite 2 para verificar qual senha foi chamada")
    print("Digite 3 para sair")
    print("----------------------------------------------------------------------")
    menu = input("Digite um valor:  ")

    if(int(menu) == 1):
        senha += 1
        print(f"Numero da senha gerada:  {senha}")
        fila.append(senha)
    elif(int(menu) == 2):
        if(len(fila) == 0):
          print("Nao possui senhas")  
        else: 
            senhaSaida = fila.pop(0)
            print(f"Senha chamada:  {senhaSaida}")
    elif(int(menu) == 3):
        break
   
print("Senhas restantes: ")
print(fila)