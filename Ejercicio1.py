x = {"Euro":"€", 'Dollar':'$', 'Yen':'¥'}

y = input("¿Que divisa quieres?")

if y in x:
    z = x[y]
    print(z)