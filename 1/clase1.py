import sys
argumentos=sys.argv

if len (argumentos)!=3:
    print("cosa")

else:
    palabra=argumentos[1]
    cantidad=int(argumentos[2])


    for i in range (cantidad):
        print(palabra)
        