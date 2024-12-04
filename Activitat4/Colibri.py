class Colibri:
    def __init__ (self, nom, tamany_cos, color, localitat, estat_conservacio,):
        self.nom = nom
        self.tamany_cos = tamany_cos 
        self.color = color
        self.localitat = localitat
        self.estat_conservacio = estat_conservacio

    def getNom(self):
        return self.nom
    def setNom(self, new_nom):
        self.nom = new_nom

    def getTamany_cos(self):
        return self.tamany_cos
    def setTamany_cos(self, new_tamany_cos):
        self.tamany_cos = new_tamany_cos

    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.tamany_cola = new_color

    def getLocalitat(self):
        return self.localitat
    def setTamany_pico(self, new_localitat):
        self.tamany_pico = new_localitat

    def getEstat_conservacio(self):
        return self.estat_conservacio
    def setColor(self, new_estat_conservacio):
        self.color = new_estat_conservacio

