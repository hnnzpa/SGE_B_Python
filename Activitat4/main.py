from Cotxe import Cotxe
from Colibri import Colibri

ibiza = Cotxe("3456 zzz", "seat", "ibiza", "negre", "3000")
leon = Cotxe("9876 zzz", "seat", "leon", "vermell", "800")
arona = Cotxe("1256 zzz", "seat", "arona", "blau", "1000")

colibri_d_anna = Colibri("Colibrí d'Anna", "10cm", "marró", "costa oest d'Amèrica del Nord", "preocupació mínima")
colibri_d_allen = Colibri("Colibrí d'Allen", "8cm", "verd", "centre Colúmbia", "preocupació mínima" )
colibri_cal·liope = Colibri("Colibrí cal·liope", "7cm", "verd", "costa sud-oest d'Oregon i Califòrnia", "preocupació mínima")

print(f'El cotxe més económic de la marca {ibiza.getMarca()} és {ibiza.getModel()} de color {ibiza.getColor()}')
print(f"El colibrí més conegut a {colibri_d_anna.getLocalitat()} és {colibri_d_anna.getNom()}, el seu color principal és el {colibri_d_anna.getColor()}, ens podem trobar-ne d'un a {colibri_d_anna.getLocalitat()}.")

print("Modifiquem els color i els kilometres del cotxe ibiza")

ibiza.setColor("gris")
ibiza.setKm("5000")
print(f"El color de l'ibiza ara és {ibiza.getColor()} i els seus kilomentres han augmentat fins a {ibiza.getKm()}" )

print("Modifiquem el tamany del colibri d'anna i el color d'aquest")

colibri_d_anna.setTamany_cos("9cm")
colibri_d_anna.setColor("rosa")
print(f"El colibrí d'Anna ara és més petit: {colibri_d_anna.getTamany_cos()} i el seu color ara és {colibri_d_anna.getColor()}")