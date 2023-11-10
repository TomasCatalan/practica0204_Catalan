x = {}
y = input("ingresa palabras en español y sus traducciones (español:inglés), para terminar, escribe 'terminar'.")

for z in y.split(","):
    if z != "terminar":
        a, b =  z.split(":")
        x[a] = b