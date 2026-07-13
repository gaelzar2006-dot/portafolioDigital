#Contadores de asientos
capacidad_inicial_futuro=200; capacidad_inicial_padrino=100
capacidad_futuro_actual=200; capacidad_padrino_actual=100
entradas_vendidas_futuro=0; entradas_vendidas_padrino=0
total_facturado_sala1=0; total_facturado_sala2=0
terminar="NO"
Continuar="NO"
#Contadores y precio de las entradas de las salas
volver_al_futuro=3000
el_padrino=2000
venta_Futuro=0
venta_Padrino=0
#STOCK DE LAS GOLOSINAS Y BEBIDAS
pochoclo_venta=0 ; chocolate_venta=0 ; coca_venta=0 ; agua_venta=0 ; sprite_venta=0 ; pepsi_venta=0 ; fanta_venta=0 ; nachos_venta=0
pochoclos_stock=50 ; chocolate_stock=50 ; coca_stock=50 ; agua_stock=50 ; sprite_stock=50 ; pepsi_stock=50 ; fanta_stock=50 ; nachos_stock=50
pochoclos_inicial=50 ; chocolate_inicial=50 ; coca_inicial=50 ; agua_inicial=50 ; sprite_inicial=50 ; pepsi_inicial=50 ; fanta_inicial=50 ; nachos_inicial=50
pochoclos_vend=0 ; chocolate_vend=0 ; coca_vend=0 ; coca_vend=0 ; agua_vend=0 ; sprite_vend=0 ; pepsi_vend=0 ; fanta_vend=0 ; nachos_vend=0
#Continuar con las golosinas
continuar_candy="NO"
while True:
    opciones=int(input(f"""
    ------------------------------------------
    BIENVENIDO AL MENÚ PRINCIPAL 
    ------------------------------------------
    RECUERDE ESCRIBIR LAS OPCIONES DISPONIBLES
    DE LO CONTRARIO NO PODRÁ AVANZAR :)
    ACUERDESE DE NO EXCEDERSE CON EL STOCK NI PONER CANTIDADES EN NEGATIVO
    DE LO CONTRARIO SE LO ENVIARÁ DE VUELTA AL MENÚ
    RECUERDE DESLIZAR ARRIBA Y ABAJO PARA VER CIERTOS MENSAJES
    ---------------------------
               CINE
    ---------------------------
    PELICULAS DEL DIA- SALAS
    1. VOLVER AL FUTURO $3000 el boleto, {capacidad_futuro_actual} asientos disponibles
    2. EL PADRINO $2000 el boleto, {capacidad_padrino_actual} asientos disponibles
    3. CANDYBAR
    4. FINALIZAR CARGA
    ---------------------------
    Si dentro de la opción se arrepiente ponga 0 en la cantidad
    INGRESE UNA OPCIÓN: """))

    Continuar=str(input(f"¿Desea continuar con la opción {opciones} SI o NO?: ")).upper()
    while Continuar!="SI" and Continuar!="NO":
        print("ERROR por favor responda solamente con SI o con NO")
        Continuar=str(input(f"¿Desea continuar con la opción {opciones} SI o NO?: ")).upper()
    if Continuar=="NO":
        print("OK, tomese la libertad de elegir lo que quiera :)")
    else:
        if opciones==1 and Continuar=="SI":
            while True:
                venta_Futuro+=1
                print("Bienvenido a la sala de VOLVER AL FUTURO")
                if capacidad_futuro_actual>0:  
                    cant_entradas_VolverAlFuturo=int(input("¿Cuantas entradas desea?: "))
                    if cant_entradas_VolverAlFuturo>capacidad_inicial_futuro or cant_entradas_VolverAlFuturo<0:
                        print("NO puede excederse del STOCK disponible, ni poner cantidades en NEGATIVO")
                        break
                    else:
                        importeVolverAlFuturo=cant_entradas_VolverAlFuturo*volver_al_futuro
                        print(f"El importe de la {venta_Futuro} venta es de {importeVolverAlFuturo}")
                        capacidad_futuro_actual=capacidad_futuro_actual-cant_entradas_VolverAlFuturo
                        entradas_vendidas_futuro=capacidad_inicial_futuro-capacidad_futuro_actual
                        total_facturado_sala1=entradas_vendidas_futuro*volver_al_futuro
                        print(f"La capacidad inicial de la sala era {capacidad_inicial_futuro} mientras que la actual es de {capacidad_futuro_actual}")
                        terminar=str(input("¿Desea seguir con la compra de boletos SI o NO?: ")).upper()
                        while terminar!="SI" and terminar!="NO":
                            print("Por favor responda con SI o con NO")
                            terminar=str(input("¿Desea seguir la compra de boletos SI o NO?: ")).upper()
                        if terminar=="NO":
                            break
                        else:
                            print("OK, siga con la compra de boletos")
                else:
                    print("Se agotaron las entradas de volver al futuro :(")
                    break
        if opciones==2 and Continuar=="SI":
            while True:
                venta_Padrino+=1
                print ("Bienvenido a la sala de EL PADRINO")
                if capacidad_padrino_actual>0:
                    cant_entradas_padrino=int(input("¿Cuantas entradas desea?: "))
                    if cant_entradas_padrino>capacidad_inicial_padrino or cant_entradas_padrino<0:
                        print("NO puede excederse del STOCK disponible, ni poner cantidades en NEGATIVO")
                        break
                    else:
                        importePadrino=cant_entradas_padrino*el_padrino
                        print(f"El importe de la {venta_Padrino} venta es de {importePadrino}")
                        capacidad_padrino_actual=capacidad_padrino_actual-cant_entradas_padrino
                        entradas_vendidas_padrino=capacidad_inicial_padrino-capacidad_padrino_actual
                        total_facturado_sala2=entradas_vendidas_padrino*el_padrino
                        print(f"la capacidad inicial de la sala era {capacidad_inicial_padrino} mientras que la actual es de {capacidad_padrino_actual}")
                        terminar=str(input("¿Desea seguir con la compra de boletos SI o NO?: ")).upper()
                        while terminar!="SI" and terminar!="NO":
                            print("Por favor responda con SI o con NO")
                            terminar=str(input("¿Desea seguir con la compra de boletos SI o NO?: ")).upper()
                        if terminar=="NO":
                            break
                        else:
                            print("OK, siga con la compra de boletos")
                else:
                    print("Se agotaron las entradas de el padrino :(")
                    break
        if opciones==3 and Continuar=="SI":
            while True:
                print("--------------------------------------")
                print("Bienvenido a las opciones del CANDYBAR")
                print("--------------------------------------")
                print("--------------------------------------------------------------------------------------------")
                print("Recuerde que si no ingresa ninguno de los números disponibles el programa no lo dejará avanzar")
                print("--------------------------------------------------------------------------------------------")
                opciones_Candy=int(input(f"""
                --------------------------------------------
                                CANDYBAR
                --------------------------------------------
                SNACKS- BEBIDAS
                0. VOLVER AL MENÚ PRINCIPAL 
                1. POCHOCLOS $2200 {pochoclos_stock} Stock
                2. CHOCOLATE BLOCK $1500 {chocolate_stock} Stock
                3. COCA COLA $1200 {coca_stock} stock
                4. AGUA $1000 {agua_stock} stock
                5. SPRITE $1300 {sprite_stock} stock
                6. PEPSI $1250 {pepsi_stock} stock
                7. FANTA $1310 {fanta_stock} stock
                8. NACHOS $3200 {nachos_stock} stock
                9. FINALIZAR COMPRA DEL CANDYBAR
                ---------------------------------------------------------------------
                RECUERDE NO EXCEDERSE CON EL STOCK DE LO CONTRARIO SE LO DEVOLVERÁ AL
                MENÚ DEL CANDYBAR :) (TAMPOCO PONER CANTIDADES EN NEGATIVO)
                EN CASO DE QUE LOS SNACKS SE HALLAN AGOTADO SE LE INFORMARÁ 
                (DESLICE ARRIBA Y ABAJO PARA VER CIERTOS MENSAJES)
                UNA VEZ QUE TERMINÉ DE COMPRAR LO QUE DESEA EN EL CANDYBAR 
                VUELVA AL MENÚ PRINCIPAL PARA FINALIZAR LA CARGA
                ---------------------------------------------------------------------
                (Si dentro de la opción se arrepiente ponga 0 en la cantidad)
                INGRESE UNA OPCIÓN: """))
                if opciones_Candy==0:
                    break
                else:
                    continuar_candy=str(input(f"Desea continuar con la opción {opciones_Candy} SI o NO: ")).upper()
                    while continuar_candy!="SI" and continuar_candy!="NO":
                        print("ERROR por favor responda solamente con SI o con NO")
                        continuar_candy=str(input(f"Desea continuar con la opción {opciones_Candy} SI o NO: ")).upper()
                    if continuar_candy=="NO":
                        print("------------------------------------------------------------------------")
                        print("OK, puede pensar mejor sus opciones o sino regresar al menú principal :)")
                        print("------------------------------------------------------------------------")
                    else:
                        if opciones_Candy==1 and continuar_candy=="SI":
                            while True:
                                if pochoclos_stock>0:
                                    cantidad_pochoclos=int(input("Ingrese la cantidad de cubetas de POCHOCLOS que desee llevar: "))
                                    if cantidad_pochoclos>pochoclos_stock or cantidad_pochoclos<0:
                                        print("No puede exceder la cantidad disponible de stock, ni poner cantidades en NEGATIVO")
                                        break
                                    else:
                                        pochoclo_venta+=1
                                        print(f"El precio total de las cubetas de pochoclos es {cantidad_pochoclos*2200}")
                                        pochoclos_stock=pochoclos_stock-cantidad_pochoclos
                                        pochoclos_vend=pochoclos_inicial-pochoclos_stock
                                        print(f"La cantidad de pochoclos que quedan disponibles después de la {pochoclo_venta} venta es de: {pochoclos_stock} pochoclos")
                                        terminar=str(input("Desea terminar con la compra de pochoclos SI o NO: ")).upper()
                                        while terminar!="SI" and terminar!="NO":
                                            print("Por favor responda con SI o con NO")
                                            terminar=str(input("¿Desea terminar con la compra de pochoclos SI o NO?: ")).upper()
                                        if terminar=="SI":
                                            break
                                        else:
                                            print("OK, A continuación siga llevando mas cubetas")
                                else:
                                    print("Ya no quedan mas pochoclos")
                                    break
                        elif opciones_Candy==2 and continuar_candy=="SI":
                            while True:
                                if chocolate_stock>0:
                                    cantidad_chocolate=int(input("Ingrese la cantidad de barras de CHOCOLATE que desee llevar: "))
                                    if cantidad_chocolate>chocolate_stock or cantidad_chocolate<0:
                                        print("No puede exceder la cantidad disponible de stock, ni poner cantidades en NEGATIVO")
                                        break
                                    else:
                                        chocolate_venta+=1
                                        print(f"El precio total de las barras de chocolate es {cantidad_chocolate*1500}")
                                        chocolate_stock=chocolate_stock-cantidad_chocolate
                                        chocolate_vend=chocolate_inicial-chocolate_stock
                                        print(f"La cantidad de chocolates que quedan disponibles después de la {chocolate_venta} venta es de: {chocolate_stock} chocolates")
                                        terminar=str(input("Desea terminar con la compra de chocolates SI o NO: ")).upper()
                                        while terminar!="SI" and terminar!="NO":
                                            print("Por favor responda con SI o con NO")
                                            terminar=str(input("¿Desea terminar con la compra de chocolates SI o NO?: ")).upper()
                                        if terminar=="SI":
                                            break
                                        else:
                                            print("OK, A continuación siga llevando mas barras")
                                else:
                                    print("Ya no quedan mas chocolates")
                                    break
                        elif opciones_Candy==3 and continuar_candy=="SI":
                            while True:
                                if coca_stock>0:
                                    cantidad_coca=int(input("Ingrese la cantidad de latas de COCA que desee llevar: "))
                                    if cantidad_coca>coca_stock or cantidad_coca<0:
                                        print("No puede exceder la cantidad de stock disponible, ni poner cantidades en NEGATIVO")
                                        break
                                    else:
                                        coca_venta+=1
                                        print(f"El precio total de las latas de coca es {cantidad_coca*1200}")
                                        coca_stock=coca_stock-cantidad_coca
                                        coca_vend=coca_inicial-coca_stock
                                        print(f"La cantidad de latas de coca que quedan disponibles despues de la {coca_venta} venta es de: {coca_stock} latas de coca")
                                        terminar=str(input("Desea terminar con la compra de latas de COCA SI o NO: ")).upper()
                                        while terminar!="SI" and terminar!="NO":
                                            print("Por favor responda con SI o con NO")
                                            terminar=str(input("¿Desea terminar con la compra de latas de coca SI o NO?: ")).upper()
                                        if terminar=="SI":
                                            break
                                        else:
                                            print("OK, A continuación siga llevando mas latas de coca")
                                else:
                                    print("Ya no quedan mas latas de coca")
                                    break
                        elif opciones_Candy==4 and continuar_candy=="SI":
                            while True:
                                if agua_stock>0:
                                    cantidad_agua=int(input("Ingrese la cantidad de botellas de AGUA que desee llevar: "))
                                    if cantidad_agua>agua_stock or cantidad_agua<0:
                                        print("No puede exceder la cantidad de stock disponible, ni poner cantidades en NEGATIVO")
                                        break
                                    else:
                                        agua_venta+=1
                                        print(f"El precio total de las botellas de agua es {cantidad_agua*1000}")
                                        agua_stock=agua_stock-cantidad_agua
                                        agua_vend=agua_inicial-agua_stock
                                        print(f"La cantidad de botellas de agua que quedan disponibles despues de la {agua_venta} venta es de: {agua_stock} botellas de agua")
                                        terminar=str(input("Desea terminar con la compra de botellas de agua SI o NO: ")).upper()
                                        while terminar!="SI" and terminar!="NO":
                                            print("Por favor responda con SI o con NO")
                                            terminar=str(input("¿Desea terminar con la compra de botellas de agua SI o NO?: ")).upper()
                                        if terminar=="SI":
                                            break
                                        else:
                                            print("OK, A continuación siga llevando mas botellas")
                                else:
                                    print("Ya no quedan mas botellas")
                                    break
                        elif opciones_Candy==5 and continuar_candy=="SI":
                            while True:
                                if sprite_stock>0:
                                    cantidad_sprite=int(input("Ingrese la cantidad de latas de SPRITE que desee llevar: "))
                                    if cantidad_sprite>sprite_stock or cantidad_sprite<0:
                                        print("No puede exceder el stock disponible, ni poner cantidades en NEGATIVO")
                                        break
                                    else:
                                        sprite_venta+=1
                                        print(f"El precio total de las latas de sprite es {cantidad_sprite*1300}")
                                        sprite_stock=sprite_stock-cantidad_sprite
                                        sprite_vend=sprite_inicial-sprite_stock
                                        print(f"La cantidad de latas de sprite que quedan disponibles despues de la {sprite_venta} venta es de: {sprite_stock} latas de sprite")
                                        terminar=str(input("Desea terminar con la compra de latas de sprite SI o NO: ")).upper()
                                        while terminar!="SI" and terminar!="NO":
                                            print("Por favor responda con SI o con NO")
                                            terminar=str(input("¿Desea terminar con la compra de latas de sprite SI o NO?: ")).upper()
                                        if terminar=="SI":
                                            break
                                        else:
                                            print("OK, A continuación siga llevando mas latas de sprite")
                                else:
                                    print("Ya no quedan mas latas de sprite")
                                    break
                        elif opciones_Candy==6 and continuar_candy=="SI":
                            while True:
                                if pepsi_stock>0:
                                    cantidad_pepsi=int(input("Ingrese la cantidad de latas de PEPSI que desee llevar: "))
                                    if cantidad_pepsi>pepsi_stock or cantidad_pepsi<0:
                                        print("No puede exceder el stock disponible, ni poner cantidades en NEGATIVO")
                                        break
                                    else:
                                        pepsi_venta+=1
                                        print(f"El precio total de las latas de PEPSI es {cantidad_pepsi*1250}")
                                        pepsi_stock=pepsi_stock-cantidad_pepsi
                                        pepsi_vend=pepsi_inicial-pepsi_stock
                                        print(f"La cantidad de latas de pepsi que quedan disponibles despues de la {pepsi_venta} venta es de: {pepsi_stock} latas de pepsi")
                                        terminar=str(input("Desea terminar con la compra de latas de pepsi SI o NO: ")).upper()
                                        while terminar!="SI" and terminar!="NO":
                                            print("Por favor responda con SI o con NO")
                                            terminar=str(input("¿Desea terminar con la compra de latas de pepsi SI o NO?: ")).upper()
                                        if terminar=="SI":
                                            break
                                        else:
                                            print("OK, A continuación siga llevando mas latas de pepsi")
                                else:
                                    print("Ya no quedan mas latas de pepsi")
                                    break
                        elif opciones_Candy==7 and continuar_candy=="SI":
                            while True:
                                if fanta_stock>0:
                                    cantidad_fanta=int(input("Ingrese la cantidad de latas de FANTA que desee llevar: "))
                                    if cantidad_fanta>fanta_stock or cantidad_fanta<0:
                                        print("No puede exceder el stock disponible, ni poner cantidades en NEGATIVO")
                                        break
                                    else:
                                        fanta_venta+=1
                                        print(f"El precio total de las latas de fanta es {cantidad_fanta*1310}")
                                        fanta_stock=fanta_stock-cantidad_fanta
                                        fanta_vend=fanta_inicial-fanta_stock
                                        print(f"La cantidad de latas de fanta que quedan disponibles después de la {fanta_venta} venta es de: {fanta_stock} latas de fanta")
                                        terminar=str(input("Desea terminar con la compra de latas de fanta SI o NO: ")).upper()
                                        while terminar!="SI" and terminar!="NO":
                                            print("Por favor responda con SI o con NO")
                                            terminar=str(input("¿Desea terminar con la compra de latas de fanta SI o NO?: ")).upper()
                                        if terminar=="SI":
                                            break
                                        else:
                                            print("OK, A continuación siga llevando mas latas de fanta")
                                else:
                                    print("Ya no quedan mas latas de fanta")
                                    break
                        elif opciones_Candy==8 and continuar_candy=="SI":
                            while True:
                                if nachos_stock>0:
                                    cantidad_nachos=int(input("Ingrese la cantidad de bandejas de NACHOS que desee llevar: "))
                                    if cantidad_nachos>nachos_stock or cantidad_nachos<0:
                                        print("No puede exceder el stock, ni poner cantidades en NEGATIVO")
                                        break
                                    else:
                                        nachos_venta+=1
                                        print(f"El precio total de las bandejas de nachos es {cantidad_nachos*3200}")
                                        nachos_stock=nachos_stock-cantidad_nachos
                                        nachos_vend=nachos_inicial-nachos_stock
                                        print(f"La cantidad de bandejas de nachos que quedan disponibles despues de {nachos_venta} venta es de: {nachos_stock} bandejas")
                                        terminar=str(input("Desea terminar con la compra de nachos SI o NO: ")).upper()
                                        while terminar!="SI" and terminar!="NO":
                                            print("Por favor responda con SI o con NO")
                                            terminar=str(input("¿Desea terminar con la compra de bandejas de nachos SI o NO?: ")).upper()
                                        if terminar=="SI":
                                            break
                                        else:
                                            print("OK, A continuación siga llevando mas bandejas de nachos")
                                else:
                                    print("Ya no quedan mas nachos")
                                    break
                        elif opciones_Candy==9:
                            while True:
                                print("/// CARGA FINALIZADA - TICKET CANDYBAR ///")
                                print(f"POCHOCLOS: {pochoclos_vend}-------------${pochoclos_vend*2200}")
                                print(f"CHOCOLATE BLOCK: {chocolate_vend}-------------${chocolate_vend*1500}")
                                print(f"COCA COLA: {coca_vend}-------------${coca_vend*1200}")
                                print(f"AGUA: {agua_vend}-------------${agua_vend*1000}")
                                print(f"SPRITE: {sprite_vend}-------------${sprite_vend*1300}")
                                print(f"PEPSI: {pepsi_vend}-------------${pepsi_vend*1250}")
                                print(f"FANTA: {fanta_vend}-------------${fanta_vend*1310}")
                                print(f"NACHOS: {nachos_vend}-------------${nachos_vend*3200}")
                                print("-----------------------------------------")
                                print(f"Total del CANDYBAR: {pochoclos_vend*2200+chocolate_vend*1500+coca_vend*1200+agua_vend*1000+sprite_vend*1300+pepsi_vend*1250+fanta_vend*1310+nachos_vend*3200}$")
                                terminar=str(input("Desea cerrar el menú de ticket SI o NO: ")).upper()
                                while terminar!="SI" and terminar!="NO":
                                    print("Por favor responda con SI o con NO")
                                    terminar=str(input("¿Desea seguir con la compra de bandejas de nachos SI o NO?: ")).upper()
                                if terminar=="SI":
                                    break
                                else:
                                    print("OK, revise tranquilo el ticket, ante cualquier consulta no dude en acercarse a la sede :)")
    if opciones==4 and Continuar=="SI":
        break
print("/// CARGA FINALIZADA - RELEVAMIENTO DEL DIA ///")
print("SALA 1 – VOLVER AL FUTURO")
print(f"Entradas Vendidas: {entradas_vendidas_futuro}")
print(f"Entradas sin vender: {capacidad_futuro_actual}")
print(f"Total facturado Sala1: {total_facturado_sala1}$")
print("SALA 2 – EL PADRINO")
print(f"Entradas Vendidas: {entradas_vendidas_padrino}")
print(f"Entradas sin vender: {capacidad_padrino_actual}")
print(f"Total facturado Sala2: {total_facturado_sala2}$")
print("CANDY BAR")
print(f"Total Facturado:{pochoclos_vend*2200+chocolate_vend*1500+coca_vend*1200+agua_vend*1000+sprite_vend*1300+pepsi_vend*1250+fanta_vend*1310+nachos_vend*3200} $")
print("-----------------------------------------")
print(f"Facturación total del día: {total_facturado_sala1+total_facturado_sala2+pochoclos_vend*2200+chocolate_vend*1500+coca_vend*1200+agua_vend*1000+sprite_vend*1300+pepsi_vend*1250+fanta_vend*1310+nachos_vend*3200} $")