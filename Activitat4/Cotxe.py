class Cotxe: 
    #Constructor
    def __init__(self, matricula, marca, model, color, km ):
        #Atributs
        self.matricula = matricula
        self.marca = marca
        self.model = model 
        self.color = color
        self.km = km

#Getterrs i Setters: serveixen per crear clases amb característiques úniques (Setters) i la informació que volem que ens proporcioni la classe. 
def getMartricula(self):
    return self.matricula #mostrarà el valor de matricula
def setMatricula(self, new_matricula):
    self.matricula = new_matricula #per poder modificar la matricula 

def getMarca(self):
    return self.marca
def setMarca(self, new_marca):
    self.marca = new_marca

def getModel(self):
    return self.model
def setModel(self, new_model):
    self.model = new_model

def getColor(self):
    return self.color
def setColor(self, new_color):
    self.color = new_color

def getKm(self):
    return self.km
def setKm(self, new_km):
    self.km = new_km 
