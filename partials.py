
def devuelveCiudades(*ciudades):
    for i in ciudades:
        for j in i:
            yield j
ciudades = devuelveCiudades(["bogota", "cartagena", "pereira"])
print(next(ciudades))
print(next(ciudades))


def devuelve2(*ciudades):
    for element in ciudades:
        yield from element
ciudad2 = devuelve2(["bogota", "cartagena", "pereira"])
print(next(ciudad2))
print(next(ciudad2))

#funciones lambda 
valor_mayor = lambda x, y: x if x > y else y
print(valor_mayor(1,2))

fizz_buzz = lambda x: "FizzBuzz" if x % 3 == 0 and x%5 == 0 else "Buzz" if x%5==0 else "Fizz" if x%3 == 0 else str(x)
print(fizz_buzz(5))

#tuplas
mitula = ("miguel", 5,5)
print("miguel" in mitula)# retorna boolean

print(mitula.count(5))

#definir noombres a cada elemento de la tupla
nombre, dia, mes = mitula
print(nombre)
print(dia)
print(mes)

#las tuplas pueden imitar diccionarios así 
(x, y) = (4, "andres")
#evaluar tuplas
print((1,2,3) > (3,4,5))# devuelve un booleano

menu = "1. suma\n 2. resta\n 3. multiplicaion\n 4. división\n"
print(menu)
op = int(input("Digita la operación que realizarás"))
if(op > 5):
    print("no es posible")
else:
    op1 = int(input("DIgita el primer valor: "))
    op2 = int(input("DIgita el segundo valor: "))
    
    lst = ["+", "-", "*", "/", "**"]
    for i in range(op+1):
        if op2 == 0:
            print("no se puede dividir entre 0")
            break
        if i == op:
            print("el resultado es: ",eval(str(op1)+lst[op-1]+str(op2)))
            break

#serializacion
from ast import Num
import pickle

lst_nombre = ["pedro", "raul", "eduardo"]
ficehro = open("nombres.txt", "wb")

pickle.dump(lst_nombre, ficehro)
ficehro.close()

#poo
class coche:
    # atributos
    largochasis = 250
    anchochasis = 130
    ruedas = 4
    enmarcha = False

    #metodos
    def arrancar(self):
        self.enmarcha = True
    
    def estado(self):
        if self.enmarcha:
            return "En marcha"
        else:
            return "xd momento"
#instancia u objetos
elcarro = coche()
print("mi coche mide: ", elcarro.anchochasis)

#acceso a atributo
elcarro.arrancar()
print("el carro esta ", elcarro.estado()) # llamado de metodo


# uso del constructor y los metodos privados o encapsulados
class coche2:
    # atributos definidos para toda la clase
    def __init__(self):
        self.lenchasis = 200
        self.weightchasis = 100
        self.__wheels = 4 #atributo que solo puede ser accedido desde los metodos
        self.andando = False

    def encender(self, arrancamos):
        self.andando = arrancamos

        if self.andando == True:
            chequeo = self.__chequeointerno() # uso del metodo encapsulado
        if self.andando == True and chequeo == True:
            return "El carro está funcionando"
        elif self.andando and chequeo == False:
            return "Algo anda mal con el hijueputa carro"
        else:
            return "El carro está averiado"
    
    #encapsulamiento de metodo
    def __chequeointerno(self):
        print("Realizando chequeo")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False

    def estado(self):
        print("El carro tiene ", self.__wheels, "Ruedas y un ancho de ", self.lenchasis, "y un largo de ", self.weightchasis)

micoche2 = coche2()
print(micoche2.encender(True))
micoche2.estado()

micoche3 = coche2()
print(micoche3.encender(False))
micoche3.estado()


#setters n getter
class Cliente:
    def __init__(self):
        self.__codigo = 0
    
    def getCodigo(self):
        return self.__codigo #con esto podemos ver atributos privados
    
    def setCodigo(self, codigo):
        self.__codigo = codigo

persona = Cliente()
print(persona.getCodigo())
persona.setCodigo(1234)
print(persona.getCodigo())

#tambien se puede traer el atributo encapsulado asñi
print(persona._Cliente__codigo)

#polimorfismo
#objeto que puede cambiar de forma y de comportamiento
class Auto:
    rueda = 4
    def desplazamiento(self):
        print("El auto se desplaza en 4 ruedas")

class Moto:
    rueda = 2
    def desplazamiento(self):
        print("El auto se desplaza en 2 ruedas")

class Camion:
    rueda = 6
    def desplazamiento(self):
        print("El auto se desplaza en 4 ruedas")
#cuando llamemos al metodo desde una instancia pues adopta los atributos de la misma

#herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def tipoAnimal(self):
        return self.nombre + "Es un animal"

class Leon(Animal):
    #hereda los atributos y puede acceder a sus metodos
    def tipoAnimal(self):
        return self.nombre + "Es un animal salvaje"

nuevo_animal = Leon("eduardo")   
print(nuevo_animal.tipoAnimal()) # su estructura cambio según el tipo de clase

#pandas: machine learning y guardado agil de datos, numpy par algebra lineal
import numpy as np
import time
import sys

long = 1000000

print("Vector numpy")
t_vector = time.time()
vector_numpy = np.arange(long, dtype="int64")
suma_vector = vector_numpy.sum()
print("Tipo de objeto " + str(type(vector_numpy)))
print("suma " + str(suma_vector))
print("tiempo de ejecucion " + str(time.time()-t_vector))

print("-------------------------------------------------")

# metodos de cadena
mieamil = input("Introduce tu correo")

arroba = mieamil.count("@")

if arroba != 1 or mieamil.rfind("@") == len(mieamil)-1 or mieamil.find("@") == 0:
    print("El emial es incorecto")
else:
    print("El email es correcto")

# uso de raise y excepciones
import math 

def calculoRaiz(number):
    if number < 0:
        raise ValueError("El numero no puede ser negativo") # en este especificamos el tipo de error
    else:
        return math.sqrt(number)

operation = int(input("Digita el numero: "))

try:
    print(calculoRaiz(operation))
except ValueError as mari:
    print(mari)

#datos permanentes

#clases creadoras
class Personas():
    #con este creamos a la persona
    def __init__(self, name, genero, age):
        self.name = name
        self.genero = genero
        self.age = age 
        print("En el metodo se agrego el nombre:", self.name)
    
    def __str__(self) -> str:
        return "{} {} {}".format(self.name, self.age, self.genero)

class Lista():
    personaje = []

    def __init__(self):
        lista_personas = open("fichero", "ab+")
        lista_personas.seek(0) #puntero que modifica su ubicacion

        try:
            self.personaje = pickle.load(lista_personas) #metemos en la lista los datos del fichero
            print("Se cargaron {} personas".format(len(self.personaje)))
        except:
            print("no hay nadie en el fichero")

    def agregar(self, person):
        self.personaje.append(person)
        self.guardado_personas()

    def mostrar(self):
        for i in self.personaje:
            print(i)

    def guardado_personas(self):
        lista_persona = open("fichero", "wb")
        pickle.dump(self.personaje, lista_persona) #hacemos el bolcado de datos lo guardamos en el fichero

    def informacion(self):
        lista = []
        print("lo que se encuentra dentro del fichero es: ")
        for i in self.personaje:
            lista.append(str(i))
        print(lista)

milista = Lista()
persona5 = Personas("miuguel", "masculino", 36)
milista.agregar(persona5)
milista.informacion()
'''
# herencia
class Vehiculo():
    #atributos
    lista = ["Furgoneta", "Electrico", "Motocicleta"]

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelerar = False
        self.frena = False
    
    def arrancar(self):
        self.enmarcha = True
        
    
    def aceleracion(self):
        self.acelerar = True
    
    def frenado(self):
        self.frena = True

    #encapsulamiento
    def funcionamiento(self, tipo_auto):
        if self.enmarcha == True:
            if self.acelerar == True:
                print("El/La ", tipo_auto, " con modelo", self.modelo, "Está andando")
            else:
                if self.frena == True:
                    print("El auto se ha detenido")
        else:
            print("el vehiculo no ha realizado ninguna accion")

    def estado(self):
        if issubclass(Furgoneta, Vehiculo) == True:
            print(self.funcionamiento("Furgoneta"))
            
        
            
class Furgoneta(Vehiculo):
    def __init__(self, marca, modelo):
        self.cargado = 0
        super().__init__(marca, modelo)
    
    def equipamiento(self, carga):
        self.cargado = carga
        if self.cargado > 0 and self.cargado <= 1000:
            print("la furgoneta de marca y modelo ", self.marca, self.modelo, "Carga con ", self.cargado)
        else:
            print("la furgoneta no maneja esa carga")

class Electrico(Vehiculo):
    def __init__(self, marca, modelo, bateria):
        super().__init__(marca, modelo)
        self.bateria = bateria
    
    def porcentajeDeCarga(self):
        if self.bateria > 50:
            print("La carga actual permite viajar por 100km")
        elif self.bateria < 0 or isinstance(self.bateria, int) != True: #con este verificamos si el tipo de dato es entero
            print("Valor no especifico numericamente")
        elif self.bateria == 0:
            print("El auto está apagado, por favor llevar a un punto de recarga")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, capacidad):
        super().__init__(marca, modelo)
        self.capacidad = capacidad
    
    # polimorfismo
    def estado(self, tipo= None):
        if self.capacidad == "Carreras":
            print("La motocicleta es de carreras")
        elif self.capacidad == "Común":
            print("La motocicleta es de transporte únicamente")
        else:
            print("No se especifica el tipo de moto")

furgon = Furgoneta("chevrolet", "XY123")
furgon.arrancar()
furgon.equipamiento(1000)
furgon.estado()

autoElectrico = Electrico("Tesla", "model s", 100)
autoElectrico.arrancar()
autoElectrico.porcentajeDeCarga()
autoElectrico.estado()'''

# generadores
def generator(limite):
    num = 1
    milista = []
    while num < limite:
        milista.append(num*2)
        num += 1
    return milista
print(generator(10))

# useo de yield
def generapares(limite):
    num = 1
    while num < limite:
        yield num*2
        num += 1
devuelvepares = generapares(11)


# decoradores
'''funciones que a su vez añaden funcionalidades a otras funciones
añaden mas funciones a funciones ya definidas

generalmente es una funcion a que recibe una funcion b y devuelve una funcion c'''
# funcion decoradora, estructura
def funcion_decoradora(funcionParametro):

    def funcion_interior():
        print("realizando calculo")
        funcionParametro()
        print("Fin del calculo")

    return funcion_interior

@funcion_decoradora # con esto le decimo a esta funcion que sea decorada con la funcion decoradora
def suma():
    print(20+50)

def resta():
    print(403-66)

suma()
resta()

