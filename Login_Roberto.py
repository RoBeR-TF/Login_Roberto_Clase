"""
Login.py

1)	Creamos una lista de usuarios:
a.	Usuario (lista)
i.	Id
ii.	Nombre
iii.	Password
2)	Inicializamos la lista pidiendo datos al usuario: no validamos type, el usuario siempre me lo que se pide
3)	Pedimos que inserte usuario y contraseña
a.	Si existe usuario pero la contraseña no coincide
i.	Inserta la contraseña correcta (hasta que atine)
b.	Si no existe el usuario:
i.	“Usuario no encontrado. ¿Quiere registarse?”
?	Sí: pedimos datos como en el primer punto
?	No: “Hasta luego Mari Carmen!!”

"""

#Admin usuarios
usuarios=[]
usuario=[]
insertarOtro=1
nombre=""
pss=""
P=0
iden=00000
while(insertarOtro==1):
    print("Inserta tu nombre, por favor")
    nombre=input()
    print("Inserta tu contrasena, por favor")
    pss=input()
    usuario.insert(0,pss)
    usuario.insert(0,nombre)
    usuario.insert(0,iden+1)   
    usuarios.append(usuario) 
    usuario=[]
    iden=iden+1
    print("Quiere insertar otro usuario? (1-Si  2-No)")   
    insertarOtro=int(input())


    #Mostrar lista de usuarios con for (es como tiene que ser ;) )
 
    for usuario1 in usuarios:
        print("Numero de alumno: ", usuario1[P])
        print("Nombre del alumno: ", usuario1[P+1])
        print("Pasword del alumno: ", usuario1[P+2])
        print("**************")

    
    i=0
    tam=len(usuarios)
    H=0
    while i<tam:
        print(" Numero: ", usuarios[H][0], "\n Nombre: ", usuarios[H][1], "\n Pasword: ", usuarios[H][2], "\n ******************")
        i=i+1
        H=H+1



