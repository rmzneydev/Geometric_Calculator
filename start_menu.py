from calculations import get_calculos, get_figuras, calculate

figuras = get_figuras()

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

    print("MENU -> Lista de Calculos disponibles <-")
    for i in range(0, len(calc_x_figura), 1):
        print(f"{i+1}. {calc_x_figura[i]}")
    
    return calc_x_figura
    
def menu_figuras(figuras):
    print("\nMENU -> Lista de Figuras <-")
    for i in range(0, len(figuras), 1):
        print(f"{i+1}. {figuras[i]}")

menu = 1
num_fig = 0
num_calculo = 0
calc_disp = []

salir = False
while not salir:
    
    valid_sel = False
    while not valid_sel and menu == 1:
        menu_figuras(figuras)
        try:
            seleccion = input("Ingrese: (#) Numero de figura / (X) Salir: ")
            seleccion = seleccion.lower().strip()
            if seleccion != "x":
                num_fig = int(seleccion)
                if (num_fig-1) in range(len(figuras)):
                    valid_sel = True
                    menu+=1                    
                else:
                    print(f"[ERROR] No existe la figura # ({num_fig})")
            else:
                valid_sel = True
                salir = True
            
        except ValueError:
            print("[ERROR] No ingreso un dato valido")
    
    valid_sel = False
    while not valid_sel and menu == 2:
        figura = figuras[num_fig-1]
        print("\n" + "=" *50)
        print(f"[Figura Seleccionada] -> (#{num_fig}. {figura})")
        print("=" *50)
        calc_disp = menu_calculos(num_fig)
        try:
            seleccion = input("Ingrese: (#) Numero de calculo / (R) Volver al menu de figuras / (X) Salir: ")
            seleccion = seleccion.lower().strip()
            if seleccion == "r":
                valid_sel = True
                menu-=1
            elif seleccion != "x":
                seleccion = int(seleccion)
                if (seleccion-1) in range(len(calc_disp)):
                    valid_sel = True
                    num_calculo = seleccion
                    menu += 1
                else:
                    print(f"[ERROR] No existe el calculo '{seleccion}' para la figura ({figura})")
            else:
                valid_sel = True
                salir = True
        except ValueError:
            print("[ERROR] No ingreso un dato valido")
    
    if menu == 3:
        nom_calculo = calc_disp[num_calculo-1]
        calculate(num_fig, nom_calculo)

        valid_sel = False
        while not valid_sel:
            
            print("\n-> OPCIONES <-")
            print("1. Repetir el calculo")
            print("2. Volver al menu de calculos (Misma Figura)")
            print("3. Volver al menu de figuras")
            print("X. Salir")
            seleccion = input("Ingrese opcion: ")
            seleccion = seleccion.lower().strip()
            if seleccion == "1":
                valid_sel = True
                continue
            elif seleccion == "2":
                valid_sel = True
                menu=2
            elif seleccion == "3":
                valid_sel = True
                menu=1
            elif seleccion == "x":
                valid_sel = True
                menu=0
                salir = True
            else:
                print(f"[ERROR] No ingreso una opcion valida")          
