def calcular_masa(ingredientes):
  
    conversiones = {
        "harina pan": 192,
        "agua": 192,
        "sal": 4,
        "aceite": 12
    }

    masa_total = 0
  
    for ingrediente, cantidad in ingredientes.items():
        if ingrediente in conversiones:
            masa_total += cantidad * conversiones[ingrediente]

    return masa_total

def main():
    print("¡Vamos a hacer arepas!")
    print("Por favor, introduce la cantidad de cada ingrediente.")

    ingredientes = {}
    ingredientes["harina pan"] = float(input("Tázas de harina de pan: "))
    ingredientes["agua"] = float(input("Tázas de agua: "))
    ingredientes["sal"] = float(input("Cucharaditas de sal: "))
    ingredientes["aceite"] = float(input("Cucharadas de aceite: "))
   
    masa_total = calcular_masa(ingredientes)

    print("La masa total de las arepas en gramos es:")
    print(masa_total)

if __name__ == "__main__":
    main()
