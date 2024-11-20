# Imprimir números de l’1 al 10 (amb for i amb while)

i = 1
while i < 11:
    print(i)
    i += 1

numlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
for x in numlist:
    print(x)

# Sumar els primers 10 números utilitzant for i range().

print(sum(range(10)))

# Imprimir els elements d'una llista amb for. 

fruits = ["poma","pera","raïm","plàtan"]

for f in fruits:
    print(f)

# Imprimir els números parells i els imparells continguts en la següent llista. Utilitzar for: 

num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
parells = []
imparells = []

for n in num:
    if n%2 == 0:
        parells.append(n)
    else:
        imparells.append(n)

print('Els nombres parells són: '  f"{parells}" )
print('Els nombres imparells són: ' f"{imparells}")



# Copiar exercici anterior i modificar-lo per a que mostri la suma dels números parells i la suma dels números imparells.


num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
parells = []
imparells = []

for n in num:
    if n%2 == 0:
        parells.append(n)
    else:
        imparells.append(n)

print('Els nombres parells són: '  f"{sum(parells)}" )
print('Els nombres imparells són: ' f"{sum(imparells)}")

# Sumar números fins a arribar a 100 amb while. Caldrà sumar els números que estan inclosos entre 0 i 100. El programa deixarà d’executar-se quan s’arribi al número 100.
nums = 1
sumn = 0

while nums < 101:
    sumn += nums
    nums += 1

print(sumn)


# Amb while indicar si el número guardat a una variable està entre 100 i 400.
