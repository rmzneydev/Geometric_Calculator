from calculations import get_calculos, get_figuras, calculate

def menu_calculos(num_fig):
    calculos = get_calculos()
    calc_x_figura = []
    
    num_fig -=1

    if num_fig == 4: # CIRCLE CASE
        calc_x_figura.append(calculos[4])
        calc_x_figura.append(calculos[1])
        calc_x_figura.append(calculos[2])
    elif num_fig <=4: # 2D FIGURES
        calc_x_figura.append(calculos[0])
        calc_x_figura.append(calculos[1])
        calc_x_figura.append(calculos[2])
    else: # 3D FIGURES
        calc_x_figura.append(calculos[2])
        calc_x_figura.append(calculos[3])

    print("MENU [Lista de Calculos disponibles]")
    for i in range(0, len(calc_x_figura), 1):
        print(f"({i+1}) {calc_x_figura[i]}")
    
    return calc_x_figura
    
def menu_figuras(tipo_figuras):
    figuras = get_figuras(tipo_figuras)
    print(f"\nMENU [Lista de Figuras {tipo_figuras}] ")
    for i in range(0, len(figuras), 1):
        print(f"({i+1}) {figuras[i]}")
    return figuras

def menu__tipos_figuras():
    print("\nMENU [Tipos de Figuras]")
    print("(1) Figuras 2D\n(2) Figuras 3D\n(X) -> Salir")

menu = 0
num_fig = 0
num_calculo = 0
calc_disp = []
tipo_figura = ""

salir = False
while not salir:

    valid_sel = False
    while not valid_sel and menu == 0:
        menu__tipos_figuras()
        seleccion = input("Ingrese opcion: ").lower().strip()
        
        if seleccion == "1":
            valid_sel = True
            menu = 1
            tipo_figura ="2D"

        elif seleccion == "2":
            valid_sel = True
            menu = 1
            tipo_figura ="3D"

        elif seleccion == "x":
            valid_sel = True
            salir = True
        else:
            print("[ERROR] No ingreso una opcion valida!") 
            continue
        
    valid_sel = False
    while not valid_sel and menu == 1:
        figuras = menu_figuras(tipo_figura)
        try:
            print("(R) -> Volver al menu anterior\n(X) -> Salir")
            seleccion = input("Ingrese opcion: ").lower().strip()
            
            if seleccion == "x":
                valid_sel = True
                salir = True
            elif seleccion == "r":
                valid_sel = True
                menu = 0
            else:
                num_fig = int(seleccion)
                if (num_fig-1) in range(len(figuras)):
                    valid_sel = True
                    menu = 2           
                else:
                    print(f"[ERROR] No existe la figura # ({num_fig})")

        except ValueError:
            print("[ERROR] No ingreso una opcion valida!")
    
    valid_sel = False
    while not valid_sel and menu == 2:
        figura = figuras[num_fig-1]
        print("\n" + "=" *50)
        print(f"[Figura Seleccionada] -> (#{num_fig}. {figura})")
        print("=" *50)
        calc_disp = menu_calculos(num_fig)
        try:
            print("(R) -> Volver al menu anterior\n(X) -> Salir")
            seleccion = input("Ingrese opcion: ").lower().strip()
            if seleccion == "r":
                valid_sel = True
                menu = 1
            elif seleccion != "x":
                seleccion = int(seleccion)
                if (seleccion-1) in range(len(calc_disp)):
                    valid_sel = True
                    num_calculo = seleccion
                    menu = 3
                else:
                    print(f"[ERROR] No existe el calculo '{seleccion}' para la figura ({figura})")
            else:
                valid_sel = True
                salir = True
        except ValueError:
            print("[ERROR] No ingreso una opcion valida!")
    
    if menu == 3:
        nom_calculo = calc_disp[num_calculo-1]
        calculate(num_fig, nom_calculo)

        valid_sel = False
        while not valid_sel:
            
            print("\n-> OPCIONES <-")
            print("(1) Repetir el calculo")
            print("(R) Volver al menu anterior")
            print("(X) Salir")
            seleccion = input("Ingrese opcion: ").lower().strip()
            if seleccion == "1":
                valid_sel = True
                continue
            elif seleccion == "r":
                valid_sel = True
                menu=2
            elif seleccion == "x":
                valid_sel = True
                salir = True
            else:
                print("[ERROR] No ingreso una opcion valida!")          
