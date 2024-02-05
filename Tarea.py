Nombre=input("Ingrese su nombre: ")
print("Hola",Nombre,"vengo a pedirte un favor")
Número=int(input("Ingresa un número: "))
if Número <=1:
    print("El número debe ser positivo")
else:
    Divisible=False
    N=2
    while N<9:
        if N==Número:
            N+=1
            continue
        R=Número%N
        if Número%N == 0:
            Divisible=True
            break
        N+=1
if not Divisible:
    print(f"{Número} es primo")
else:
    print(f"{Número} no es primo")