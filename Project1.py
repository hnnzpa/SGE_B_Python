#1. Comparar 2 números
#Crear dues variables i comparar-les indicant quina és més gran, quina és més petita o si son iguals

var1 = 3
var2 = 1

if var1 > var2:
    print(var1, "és més gran que", var2)
elif var1 < var2:
    print(var1, "és més petit que", var2)

else:
    print(var1, "i", var2, "són iguals")




#2. Dia de la setmana
#Crear un arxiu nou per a que retorni per pantalla la resposta adeqüada. 
# Crear 1 variable per dia de la setmana. Exemple: dia_setmana = “dilluns”
#Si dia_setmana és dilluns, haurà de sortir un print indicant “Avui és dilluns”. 
# Si dia_setmana és dimarts, haurà de sortir per pantalla el text Avui és dimarts, etc. 
# Per tant, caldrà utilitzar l’expressió if de manera que si la variable dia_setmana es modifica indiqui el dia adeqüat.

dia = "uno"

uno = 'dilluns'
dos = 'dimarts'
tres = 'dimecres'
quatre = 'dijous'
cinc = 'divendres'
sis = 'dissabte'
set = 'diumenge'

if dia == 'uno':
    print("Avui és", uno)
if dia == 'dos':
    print("Avui és", dos)
if dia == 'tres':
    print("Avui és", tres)
if dia == 'quatre':
    print("Avui és", quatre)
if dia == 'cinc':
    print("Avui és", cinc)
if dia == 'sis':
    print("Avui és", sis)
if dia == 'set':
    print("Avui és", set)
else:
    print('Introdueix un dia vàlid (uno-set)')



#Nota Mòdul
#En aquest exercici caldrà modificar la nota en número i mostrar-la en text. 
# Es crearà una variable on es guardarà la nota numèrica i amb condicionals es mirarà la nota i segons la nota numèrica sortirà per pantalla 
# la nota (S - suspès, A - aprovat, N - notable, E - excel·lent)

nota = 10

if nota >= 0 and nota <=4.99:
    sortida = 'Has suspés'
elif nota > 4.99 and nota <= 6.5:
    sortida = "Has aprovat"
elif nota >= 6.6 and nota <= 8:
    sortida = "Tens un notable"
if nota > 8 and nota <= 10:
    sortida = "Ben fet! Tens un exel·lent"
else:
    sortida = "Introdueix una nota vàlida (0-10)"

print(sortida)



#Aplicar IVA segons el salari
#En aquest exercici, s’aplicarà un IVA (0, 10, 21) segons el salari que s’indiqui.
#Crear una variable de nom salari. Si el salari és menor de 15.000, s’aplica un 0% d’IVA. 
# Si el salari és menor de 30.000 s’aplica un 10% de l’iva. 
# Si el salari és menor a 60.000 s’aplica un IVA del 21%.

salari = 29000

if salari >= 0 and salari <= 15000:
    print('No tens IVA')
if salari > 15000 and salari <= 30000:
    print("Tu iva és d'un 10%, per tant el slari s'et queda en", ((salari/10)*100))
if salari > 30000 and salari <= 60000:
    print("Tu iva és d'un 21%, per tant el slari s'et queda en", ((salari/21)*100))
