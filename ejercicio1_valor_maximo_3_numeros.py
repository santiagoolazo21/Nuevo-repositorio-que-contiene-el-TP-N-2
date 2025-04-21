def ingresar_numeros():
    lista_numeros= []
    for i in range(3): 
        while True: 
            numero= input(f"Ingrese el número {i + 1}: ")
            try:
                entrada= float(numero)  
                lista_numeros.append(entrada)  
                break  
            except ValueError:
                print("Error: Ingresa un número válido.")  
    print("Lista de números ingresados:", lista_numeros)

    maximo= max(lista_numeros)
    print(f"El numero maximo es: {maximo} ")
ingresar_numeros()