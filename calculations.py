def get_figuras():
    figuras = ["Triángulo",
        "Triángulo rectángulo",
        "Rectángulo",
        "Hexágono",
        "Círculo",
        "Cubo",
        "Esfera",
        "Cilindro",
        "Prisma rectangular"]
    return figuras

def get_input(message, data_type):
    valid_input = False
    while not valid_input:
        try:
            user_input = input(message).lower().strip()
            user_input = data_type(user_input)
            if user_input <=0:
                print(f"[ERROR] El dato no puede ser menor o igual a 0")
                continue
            
            value = user_input
            valid_input = True
                
        except ValueError:
            print(f"[ERROR] Entrada no válida. Por favor, ingrese un valor del tipo ({(data_type).__name__}).")
    return value

def get_calculos():
    calculos = ["Perimetro", "Ángulos", "Area", "Volumen", "Circunferencia"]
    return calculos

def calculate(num_figura, nombre_calculo):
    nombre_figura = get_figuras()[num_figura-1]
    print("=" *50)
    print(f"[FIGURA] -> ({nombre_figura})\n[CALCULAR] -> ({nombre_calculo}) ")
    print("=" *50)
    
    num_calculo = get_calculos().index(nombre_calculo)
    result = ""

    if num_calculo == 0:
        perimetro = get_perimetro(num_figura)
        result = f"El Perimetro es: {perimetro:.1f} cm"
    elif num_calculo == 1:
        angulos = get_angulo(num_figura)
        result = angulos
    elif num_calculo == 2:
        area = get_area(num_figura)
        result = f"El Area es: {area:.1f} cm"
    elif num_calculo == 3:
        volumen = get_volumen(num_figura)
        result = f"El Volumen es: {volumen:.1f} cm³"
    elif num_calculo == 4:
        circunferencia = get_circunferencia(num_figura)
        result = f"La Circunferencia es: {circunferencia:.1f}"

    print("=" *15, "RESULTADO", "=" *15)
    print(result)
    print("="*41)

def get_area(num_figura):
    
    PI = 3.14159

    if num_figura == 1 or num_figura == 2: # Triángulo / Triángulo rectángulo
        base = get_input("Ingrese la base (Float): ", float)
        altura = get_input("Ingrese la altura (Float): ", float)
        area = (base * altura) / 2
    
    elif num_figura == 3: # Rectangulo
        base = get_input("Ingrese la base (Float): ", float)
        altura = get_input("Ingrese la altura (Float): ", float)
        area = base * altura

    elif num_figura == 4: # Hexagono
        lado = get_input("Ingrese la longitud del lado (Float): ", float)
        raiz_3 = 3 ** 0.5
        area = ((3 * raiz_3) / 2) * (lado ** 2)
    
    elif num_figura == 5: # Circulo
        radio = get_input("Ingrese el radio del Circulo (Float): ", float)
        area = PI * (radio ** 2)

    elif num_figura == 6: # Cubo
        lado = get_input("Ingrese la longitud del lado del cubo (Float): ", float)
        area = 6 * (lado ** 2)

    elif num_figura == 7: # Esfera
        radio = get_input("Ingrese el radio de la Esfera (Float): ", float)
        
        area = 4 * PI * (radio ** 2)
    
    elif num_figura == 8: # Cilindro
        radio = get_input("Ingrese el radio del cilindro (Float): ", float)
        altura = get_input("Ingrese la altura del cilindro (Float): ", float)
        area = 2 * PI * radio * (radio + altura)
    
    elif num_figura == 9: # Prisma rectangular
        largo = get_input("Ingrese el largo del Prisma (Float): ", float)
        ancho = get_input("Ingrese el ancho del Prisma (Float): ", float)
        alto = get_input("Ingrese el alto del Prisma (Float): ", float)
        area = 2 * ((largo * ancho) + (largo * alto) + (ancho * alto))
    
    return area

def get_angulo(num_figura):

    if num_figura == 1: # Triángulo
        tercer_angulo = 0
        valid_angulos = False
        while not valid_angulos:
            angulo1 = get_input("Ingrese un ángulo lado A (Float): ", float)
            
            if angulo1 >= 180:
                print("[ERROR] Un solo ángulo no puede ser igual o mayor a 180°.")
                continue

            angulo2 = get_input("Ingrese el ángulo lado B (Float): ", float)
            
            if (angulo1 + angulo2) >=180:
                print("La suma de los angulos A y B debe ser menor a 180")
                continue

            valid_angulos = True
            tercer_angulo = 180 - (angulo1 + angulo2)        
        return f"El Ángulo C = {tercer_angulo:.1f}°"
    
    elif num_figura == 2:

        valid_angulos = False
        while not valid_angulos:
            agudo_a = get_input("Ingrese angulo agudo A (Float): ", float)
            if agudo_a >=90:
                print("El ángulo agudo A no puede ser igual o mayor a 90")
                continue
            valid_angulos = True
            
        agudo_b = 90-agudo_a

        angulos = f"Ángulo lado A: {agudo_a:.1f}°\nÁngulo lado B: {agudo_b:.1f}°\nÁngulo lado C: 90°"
        return angulos
    
    elif num_figura == 3: # Rectangulo
        return "Los Ángulos son de: 90° cada lado"

    elif num_figura == 4: # Hexagono
        return "Los Ángulos son de: 120° cada lado"
    
    elif num_figura == 5: # Circulo
        return "El Ángulo es de: 360° en total"


def get_perimetro(num_figura):

    perimetro = None

    if num_figura == 1: # Triángulo
        lado1 = get_input("Ingrese longitud (cm) del lado 1 (Float): ", float)
        lado2 = get_input("Ingrese longitud (cm) del lado 2 (Float): ", float)
        lado3 = get_input("Ingrese longitud (cm) del lado 3 (Float): ", float)
        perimetro = lado1 + lado2 + lado3
    
    elif num_figura == 2: # Triángulo rectángulo
        cateto1 = get_input("Ingrese el primer cateto (Float): ", float)
        cateto2 = get_input("Ingrese el segundo cateto (Float): ", float)
        hipotenusa = (cateto1**2 + cateto2**2)**0.5
        perimetro = cateto1 + cateto2 + hipotenusa

    elif num_figura == 3: # Rectangulo
        base = get_input("Ingrese la base (cm) del rectángulo (Float): ", float)
        altura = get_input("Ingrese la altura (cm) del rectángulo (Float): ", float)
        perimetro = 2 * (base + altura)
    
    elif num_figura == 4: # Hexágono
        lado = get_input("Ingrese la medida del lado del hexágono (Float): ", float)
        perimetro = 6 * lado

    return perimetro

def get_volumen(num_figura):

    PI = 3.14159

    volumen = None
    
    if num_figura == 6: # Cubo
        lado = get_input("Ingrese la longitud (cm) del lado del cubo (Float): ", float)
        volumen = lado ** 3

    elif num_figura == 7: # Esfera
        radio = get_input("Ingrese el radio de la esfera (Float): ", float)
        volumen = (4/3) * PI * (radio ** 3)
    
    elif num_figura == 8: # Cilindro
        radio = get_input("Ingrese el radio del cilindro (Float): ", float)
        altura = get_input("Ingrese la altura del cilindro (Float): ", float)
        volumen = PI * (radio**2) * altura
    
    elif num_figura == 9: # Prisma rectangular
        largo = get_input("Ingrese el largo (cm) del Prisma (Float): ", float)
        ancho = get_input("Ingrese el ancho (cm) del Prisma (Float): ", float)
        alto = get_input("Ingrese el alto (cm) del Prisma (Float): ", float)
        volumen = largo * ancho * alto
    
    return volumen

def get_circunferencia(num_figura):
    PI = 3.14159

    if num_figura == 5: # Circulo
        radio = get_input("Ingrese el radio del circulo (Float): ", float)
        circunferencia = 2 * PI * radio
        return circunferencia