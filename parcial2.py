from io import open
import pickle

class trabajador:

    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return "{} => {} vida, {} ataque, {} defensa, {} alcance".format(
            self.nombre, self.vida, self.ataque, self.defensa, self.alcance)


class Gestor:

    trabajadoes = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self, p):
        for pTemp in self.trabajadores:
            if pTemp.nombre == p.nombre:
                return
        self.trabajadores.append(p)
        self.guardar()

    def borrar(self, nombre):
        for pTemp in self.trabajadores:
            if pTemp.nombre == nombre:
                self.trabajadores.remove(pTemp)
                self.guardar()
                print("\ntrabajador {} borrado".format(nombre))
                return

    def mostrar(self):
        if len(self.trabajadores) == 0:
            print("El gestor está vacío")
            return
        for p in self.trabajadores:
            print(p)

    def cargar(self):
        fichero = open('trabajadores.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.trabajadores = pickle.load(fichero)
        except:
            
            pass
        finally:
            fichero.close()
            print("Se han cargado {} trabajadores".format( 
                len(self.trabajadores)))

    def guardar(self):
        fichero = open('trabajadores.pckl', 'wb')
        pickle.dump(self.trabajadores, fichero)
        fichero.close()



G = Gestor()
G.agregar( trabajador("Caballero",4,2,4,2) )
G.agregar( trabajador("Guerrero",2,4,2,4) )
G.agregar( trabajador("Arquero",2,4,1,8) )
G.mostrar()
G.borrar("Arquero")
G.mostrar()
Resultado


