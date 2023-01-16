import numpy as np

numeroUno = float(input("Ingresa el numero 1 : "))

numeroDos = float(input("Ingresa el numero 2 : "))


operacion = 0

while True :
        print("""
        
        Escoge
        
        1- Suma
        
        2.- Resta
        
        3.- Multiplicacion
        
        4.- Division
        
        5.- Raiz
        
        6.- Exponencial
        
        7.- Coseno
        
        8.- Salir
        
        """)


        opci = int (input (" Escoga la opcion deseada "))



        if opci == 1:
            print( " ")
            print( " Resultado : ")

            print(numeroUno + numeroDos )


        if opci == 2:
            print( " ")
            print( " Resultado : ")

            print(numeroUno - numeroDos )

        if opci == 3:
                print(" ")
                print(" Resultado : ")

                print(numeroUno * numeroDos)

        if opci == 4:
                    print(" ")
                    print(" Resultado : ")

                    print(numeroUno / numeroDos)

        if opci == 5:
                            print(" ")
                            print(" Resultado : ")

                            print(np.sqrt(numeroUno + numeroDos))

        if opci == 6:
                                print(" ")
                                print(" Resultado : ")

                                print(pow(numeroUno,3))

        if opci == 7:
                                    print(" ")
                                    print(" Resultado : ")

                                    print(np.cos(numeroUno))
        if opci == 8:
                                    print(" ")
                                    print(" Saliendo de la calculadora. ")
                                    break















