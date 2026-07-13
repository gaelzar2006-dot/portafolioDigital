#ARREGLOS DE VENDEDORES/VENTAS
productos=['fiat cronos', 'fiat toro', 'fiat pulse', 'fiat mobi', 'fiat fastback'] ; salir=["0"]; continuar=["1"]
stockInicial=[100, 200, 300, 400, 500] ; totalDeCochesVendidos=[]; precioProd=[1000, 2000, 3000, 4000, 5000] ; 
gananciasGael=0 ; gananciasEdu=0 ; cochesVendidosG=0 ; cochesVendidosE=0 ; mayor=0 ; mayorganancia=0 ; bonoE=[]; bonoG=[]; bonoM=[]; bonoT=[]
gananciasMadeline=0 ; gananciasTomas=0 ; cochesVendidosM=0 ; cochesVendidosT=0; sueldoNetoE=0 ; sueldoNetoG=0 ; sueldoNetoM=0 ; sueldoNetoT=0 ; bono=0
while True: #LOGIN
    nombre=[]
    contraseña=[]
    sucursales=["N", "S"] ; print(f"ID de las {sucursales}")
    print("RECUEDE SEGUIR LAS INSTRUCCIONES AL PIE DE LA LETRA DE LO CONTRARIO EL PROGRAMA NO LO DEJARÁ AVANZAR")
    terminar="NO"
    s=str(input("¿DESEA SALIR DE LA PÁGINA(EN CASO DE SI, OPRIMIR 0, SINO OPRIMA 1)?: "))
    if s in salir: #CIERRE ABSOLUTO
        break
    elif s in continuar:
        print("DEBIDO AL PROTOCOLO DE SEGURIDAD DE LA COMPAÑIA")
        print("A LOS EMPLEADOS SE LES PEDIRÁ QUE HAGAN LOGIN DESDE CERO TODO EL TIEMPO")
        usuario=str(input("INGRESE EL NOMBRE DE USUARIO: ")).upper()
        nombre.append(usuario) 
        ingresoContraseña=str(input("INGRESE LA CONTRASEÑA: "))
        contraseña.append(ingresoContraseña)
        usuario=str(input("VUELVA A INGRESAR EL NOMBRE DE USUARIO: ")).upper()
        ingresoContraseña=str(input("VUELVA A INGRESAR LA CONTRASEÑA: "))
        while usuario not in nombre or ingresoContraseña not in contraseña:#VALIDACIÓN DE INICIO DE SESIÓN
            print("ERROR DE USUARIO O CONTRASEÑA")
            usuario=str(input("INGRESE EL NOMBRE DE USUARIO: ")).upper()
            ingresoContraseña=int(input("INGRESE LA CONTRASEÑA: "))
        idSucursal=str(input("Por último para terminarnos de asegurar, ingrese el ID de la sucursal para la que trabaja: ")).upper()
        if idSucursal not in sucursales:
            print("EN UNOS DÍAS NOS ESTAMOS COMUNICANDO CON USTED PARA HABLAR DEL TEMA :)")
            break
        else: #ACCESO AL PROGRAMA
            if usuario in nombre and ingresoContraseña in contraseña and idSucursal in sucursales:
                while True: #MENÚ PRINCIPAL DEL PROGRAMA
                    ingreso_opciones=int(input("""BIENVENIDO A FIAT
                    0. CERRRAR SESIÓN                        
                    1. SUCURSALES-VENTAS                
                    2. VENDEDORES-VENTAS
                    3. AREA DE RECURSOS HUMANOS
            
                    A CONTINUACIÓN INGRESE ALGUNA DE LAS SIGUIENTES OPCIONES
                    POR FAVOR ESCRIBA EN NÚMEROS DE LO CONTRARIO EL PROGRAMA NO LO DEJARÁ AVANZAR: """))
                    if ingreso_opciones==1: #MENÚ DE SUCURSALES VENTAS
                        while True:
                            opciones_SV=int(input("""SUCURSALES VENTAS
                            0. CERRAR MENÚ
                            1. SUCURSAL Norte
                            2. SUCURSAL Sur
                            INGRESE ALGUNA DE LAS SIGUIENTES OPCIONES: """))
                            if opciones_SV==0: #SALIDA DEL MENÚ DE LOS DATOS DE LAS SUCURSALES
                                desea_terminar=str(input("¿DESEA CERRAR EL MENÚ SI O NO?: ")).upper()
                                if desea_terminar=="SI":
                                    cierre=str(input("¿Esta seguro SI o NO?: ")).lower()
                                    if cierre=="si":
                                        break
                                    else:
                                        print("Ok entonces continue")
                            elif opciones_SV==1: #DATOS DE LA SUCURSAL NORTE
                                print("DATOS DE LA SUCURSAL NORTE")
                                mes=[1,2,3,4,5,6,7,8,9,10,11,12]
                                totalProdXmes2024=[10,20,30,40,50,60,70,80,90,100,110,120]
                                importeVentasXMes2024=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000]
                                totalProdXmes2025=[11,21,31,41,51,61,71,81,91,101,111,121]
                                importeVentasXMes2025=[1001,2001,3001,4001,5001,6001,7001,8001,9001,10001,11001,12001]
                                for x in range(len(mes)):
                                    verVentas=int(input("¿Desea ver la venta mensual (1) para si y (0) para no?: "))
                                    if verVentas==1:
                                        print(f"Meses= {mes}")
                                        mesN=int(input("¿De que mes desea ver el importe de venta?: "))
                                        while mesN not in mes:
                                            mesN=int(input("ERROR, mes no existente...¿De que mes desea ver el importe de venta?: "))
                                        if mesN in mes:
                                            añoN=int(input(f"¿Del mes {mesN} de que año desea ver (1) para 2024 y (2) para 2025?: "))
                                            if añoN==1:
                                                posMes=mes.index(mesN)
                                                print("IMPORTE DE VENTAS DEL 2024")
                                                print(f"MES {mes[posMes]}")
                                                print(f"IMPORTE TOTAL DE LAS VENTAS DE ESE MES: {importeVentasXMes2024[posMes]}")
                                                prodVendidos=int(input("¿Desea ver la cantidad de productos vendidos de ese mes (1) para si y (0) para no?:"))
                                                if prodVendidos==1:
                                                    print(f"CANTIDAD DE PRODUCTOS VENDIDOS DE ESE MES: {totalProdXmes2024[posMes]}")
                                                elif prodVendidos==0:
                                                    break
                                                maximo_minimo=int(input("¿Desea saber el máximo y el mínimo de cada importe (0) para no y (1) para si?: "))
                                                if maximo_minimo==1:
                                                    mayorImporteVenta=max(importeVentasXMes2024)
                                                    minimoImporteVenta=min(importeVentasXMes2024)
                                                    posMax=importeVentasXMes2024.index(mayorImporteVenta)
                                                    posMin=importeVentasXMes2024.index(minimoImporteVenta)
                                                    print(f"El mes que más facturo fue {mes[posMax]} con un TOTAL DE: {mayorImporteVenta}")
                                                    print(f"El mes que menos facturo fue {mes[posMin]} con un TOTAL DE: {minimoImporteVenta}")
                                                    break
                                                elif maximo_minimo==0:
                                                    break
                                            elif añoN==2:
                                                posMes=mes.index(mesN)
                                                print("IMPORTE DE VENTAS DEL 2025")
                                                print(f"MES {mes[posMes]}")
                                                print(f"IMPORTE TOTAL DE LAS VENTAS DE ESE MES: {importeVentasXMes2025[posMes]}")
                                                prodVendidos1=int(input("¿Desea ver la cantidad de productos vendidos de ese mes (1) para si y (0) para no?:"))
                                                if prodVendidos1==1:
                                                    print(f"CANTIDAD DE PRODUCTOS VENDIDOS DE ESE MES: {totalProdXmes2025[posMes]}")
                                                elif prodVendidos1==0:
                                                    break
                                                maximo_minimo=int(input("¿Desea saber cuel fue el mayor importe de venta y el menor importe de venta (0) para no y (1) para si?: "))
                                                if maximo_minimo==1:
                                                    mayorImporteVenta1=max(importeVentasXMes2025)
                                                    minimoImporteVenta1=min(importeVentasXMes2025)
                                                    posMax1=importeVentasXMes2025.index(mayorImporteVenta1)
                                                    posMin1=importeVentasXMes2025.index(minimoImporteVenta1)
                                                    print(f"El mes que más facturo fue {mes[posMax1]} con un TOTAL DE: {mayorImporteVenta1}")
                                                    print(f"El mes que menos facturo fue {mes[posMin1]} con un TOTAL DE: {minimoImporteVenta1}")
                                                    break
                                                elif maximo_minimo==0:
                                                    break
                                    elif verVentas==0:
                                        break
                            elif opciones_SV==2: #DATOS DE LA SUCURSAL SUR
                                print("DATOS DE LA SUCURSAL SUR")
                                mes=[1,2,3,4,5,6,7,8,9,10,11,12]
                                totalProdXmes2024=[12,24,36,48,60,72,84,96,108,120,132,144]
                                importeVentasXMes2024=[1003,2003,3003,4003,5003,6003,7003,8003,9003,10003,11003,12003]
                                totalProdXmes2025=[13,26,39,52,65,78,91,104,117,130,143,156]
                                importeVentasXMes2025=[1005,2005,3005,4005,5005,6005,7005,8005,9005,10005,11005,12005]
                                for x in range(len(mes)):
                                    verVentas=int(input("¿Desea ver la venta mensual (1) para si y (0) para no?: "))
                                    if verVentas==1:
                                        print(f"Meses= {mes}")
                                        mesN=int(input("¿De que mes desea ver el importe de venta?: "))
                                        while mesN not in mes:
                                            mesN=int(input("ERROR, mes no existente...¿De que mes desea ver el importe de venta?: "))
                                        if mesN in mes:
                                            añoN=int(input(f"¿Del mes {mesN} de que año desea ver (1) para 2024 y (2) para 2025?: "))
                                            if añoN==1:
                                                posMes=mes.index(mesN)
                                                print("IMPORTE DE VENTAS DEL 2024")
                                                print(f"MES {mes[posMes]}")
                                                print(f"IMPORTE TOTAL DE LAS VENTAS DE ESE MES: {importeVentasXMes2024[posMes]}")
                                                prodVendidos=int(input("¿Desea ver la cantidad de productos vendidos de ese mes (1) para si y (0) para no?:"))
                                                if prodVendidos==1:
                                                    print(f"CANTIDAD DE PRODUCTOS VENDIDOS DE ESE MES: {totalProdXmes2024[posMes]}")
                                                elif prodVendidos==0:
                                                    break
                                                maximo_minimo=int(input("¿Desea saber cual fue el mayor importe de venta y el menor importe de venta (0) para no y (1) para si?: "))
                                                if maximo_minimo==1:
                                                    mayorImporteVenta=max(importeVentasXMes2024)
                                                    minimoImporteVenta=min(importeVentasXMes2024)
                                                    posMax=importeVentasXMes2024.index(mayorImporteVenta)
                                                    posMin=importeVentasXMes2024.index(minimoImporteVenta)
                                                    print(f"El mes que más facturo fue {mes[posMax]} con un TOTAL DE: {mayorImporteVenta}")
                                                    print(f"El mes que menos facturo fue {mes[posMin]} con un TOTAL DE: {minimoImporteVenta}")
                                                    break
                                                elif maximo_minimo==0:
                                                    break
                                            elif añoN==2:
                                                posMes=mes.index(mesN)
                                                print("IMPORTE DE VENTAS DEL 2025")
                                                print(f"MES {mes[posMes]}")
                                                print(f"IMPORTE TOTAL DE LAS VENTAS DE ESE MES: {importeVentasXMes2025[posMes]}")
                                                prodVendidos1=int(input("¿Desea ver la cantidad de productos vendidos de ese mes (1) para si y (0) para no?:"))
                                                if prodVendidos1==1:
                                                    print(f"CANTIDAD DE PRODUCTOS VENDIDOS DE ESE MES: {totalProdXmes2025[posMes]}")
                                                elif prodVendidos1==0:
                                                    break
                                                maximo_minimo=int(input("¿Desea saber el máximo y el mínimo de cada importe (0) para no y (1) para si?: "))
                                                if maximo_minimo==1:
                                                    mayorImporteVenta1=max(importeVentasXMes2025)
                                                    minimoImporteVenta1=min(importeVentasXMes2025)
                                                    posMax1=importeVentasXMes2025.index(mayorImporteVenta1)
                                                    posMin1=importeVentasXMes2025.index(minimoImporteVenta1)
                                                    print(f"El mes que más facturo fue {mes[posMax1]} con un TOTAL DE: {mayorImporteVenta1}")
                                                    print(f"El mes que menos facturo fue {mes[posMin1]} con un TOTAL DE: {minimoImporteVenta1}")
                                                    break
                                                elif maximo_minimo==0:
                                                    break
                                    elif verVentas==0:
                                        break
                    elif ingreso_opciones==2: #MENÚ DE VENDEDORES-VENTAS
                        while True:
                            opciones_VV=int(input("""VENDEDORES/ VENTAS
                            0. CERRAR MENÚ
                            1. SUCURSAL NORTE
                            2. SUCURSAL SUR
                            3. DATOS DE LOS VENDEDORES
                            INGRESE ALGUNAS DE LAS SIGUIENTES OPCIONES: """))
                            if opciones_VV==0: #CIERRE DE VENDEDORES/ VENTAS
                                desea_terminar=str(input("¿DESEA CERRAR EL MENÚ SI O NO?: ")).upper()
                                if desea_terminar=="SI":
                                    cierre=str(input("¿Esta seguro SI o NO?: ")).lower()
                                    if cierre=="si":
                                        break
                                    else:
                                        print("Ok que tenga buen día")
                            elif opciones_VV==1:
                                vendedores=int(input("""
                                LISTA DE VENDEDORES SUCURSAL NORTE
                            
                                0. SALIR DEL MENÚ DE VENTAS                   
                                1. VENDEDOR EDUARDO PSATHAKIS                   
                                2. VENDEDOR GAEL PONTIERI                   
                            
                                INGRESE ALGUNA DE LAS SIGUIENTES OPCIONES: """))
                                if vendedores==0:
                                    break
                                elif vendedores==1: #VENDEDOR EDUARDO
                                    for x in range (len(productos)):
                                        print(f"CANTIDAD DE STOCK= {stockInicial} PRODUCTOS= {productos}")
                                        s=str(input("IGRESE 0 SI DESEA SALIR (para continuar oprima 1): "))
                                        if s in salir:
                                            break
                                        elif s in continuar:
                                            consultaProd=str(input("INGRESE EL NOMBRE DEL PRODUCTO QUE VENDIO: ")).lower()
                                            while consultaProd not in productos:
                                                consultaProd=str(input("PRODUCTO INEXISTENTE, POR FAVOR INGRESE EL NOMBRE DEL PRODUCTO QUE VENDIO: ")).lower()
                                            if consultaProd in productos:
                                                pos=productos.index(consultaProd)
                                                cantidadVendida=int(input(f"INGRESE LA CANTIDAD VENDIDA DEL {consultaProd}: "))
                                                while cantidadVendida<0 or cantidadVendida>stockInicial[pos]:
                                                    cantidadVendida=int(input(f"ERROR. cantidad IMPOSIBLE del {consultaProd} ingrese una cantidad DISPONIBLE: "))#VALIDACIÓN DEL PRODUCTO
                                                stockInicial[pos]=stockInicial[pos]-cantidadVendida
                                                gananciasEdu=gananciasEdu+precioProd[pos]*cantidadVendida
                                                cochesVendidosE=cochesVendidosE+cantidadVendida
                                                if stockInicial[pos]<100: #AVISO DE STOCK
                                                    print(f"Quedan menos de de 100 unidades de {productos[pos]}. CANTIDAD RESTANTE: {stockInicial[pos]}")
                                                    agregarStock=int(input("¿Desea agregar STOCK (0) para NO y (1) para SI?: "))
                                                    if agregarStock==0:
                                                        print("OK")
                                                    elif agregarStock==1:
                                                        añadir=int(input(f"INGRESE LA CANTIDAD QUE DESEA AÑADIRLE A {productos[pos]}: "))
                                                        stockInicial[pos]=stockInicial[pos]+añadir
                                                        s=str(input("IGRESE 0 SI DESEA SALIR, 1 PARA CONTINUAR: "))
                                                        print(stockInicial)
                                                        if s in salir:
                                                            break
                                                        elif s in continuar:
                                                            print("siga añadiendo stock entoneces")
                                elif vendedores==2: #VENDEDOR GAEL PONTIERI
                                    for x in range (len(productos)):
                                        print(f"CANTIDAD DE STOCK= {stockInicial} PRODUCTOS= {productos}")
                                        s=str(input("IGRESE 0 SI DESEA SALIR (para continuar oprima 1 para continuar): "))
                                        if s in salir:
                                            break
                                        elif s in continuar:
                                            consultaProd=str(input("INGRESE EL NOMBRE DEL PRODUCTO QUE VENDIO: ")).lower()
                                            while consultaProd not in productos:
                                                consultaProd=str(input("PRODUCTO INEXISTENTE, POR FAVOR INGRESE EL NOMBRE DEL PRODUCTO QUE VENDIO: ")).lower()
                                            if consultaProd in productos:
                                                pos=productos.index(consultaProd)
                                                cantidadVendida=int(input(f"INGRESE LA CANTIDAD VENDIDA DEL {consultaProd}: "))
                                                while cantidadVendida<0 or cantidadVendida>stockInicial[pos]:
                                                    cantidadVendida=int(input(f"ERROR. cantidad IMPOSIBLE del {consultaProd} ingrese una cantidad DISPONIBLE: "))
                                                pos=productos.index(consultaProd)
                                                stockInicial[pos]=stockInicial[pos]-cantidadVendida
                                                gananciasGael=gananciasGael+precioProd[pos]*cantidadVendida
                                                cochesVendidosG=cochesVendidosG+cantidadVendida
                                                if stockInicial[pos]<100: #AVISO DE STOCK
                                                    print(f"Quedan menos de de 100 unidades de {productos[pos]}. CANTIDAD RESTANTE: {stockInicial[pos]}")
                                                    agregarStock=int(input("¿Desea agregar STOCK (0) para NO y (1) para SI?: "))
                                                    if agregarStock==0:
                                                        print("OK")
                                                    elif agregarStock==1:
                                                        añadir=int(input(f"INGRESE LA CANTIDAD QUE DESEA AÑADIRLE A {productos[pos]}: "))
                                                        stockInicial[pos]=stockInicial[pos]+añadir
                                                        s=str(input("IGRESE 0 SI DESEA SALIR: "))
                                                        print(stockInicial)
                                                        if s in salir:
                                                            break 
                                                        elif s in continuar:
                                                            print("SIGA AÑADIENDO STOCK ENTONCES")
                            elif opciones_VV==2:
                                vendedores=int(input("""
                                LISTA DE VENDEDORES SUCURSAL SUR
                            
                                0. SALIR DEL MENÚ DE VENTAS                   
                                1. VENDEDORA MADELINE VILLALBA                   
                                2. TOMAS MONTENEGRO                   
                            
                                INGRESE ALGUNA DE LAS SIGUIENTES OPCIONES: """))
                                if vendedores==0:
                                    break
                                elif vendedores==1: #MADELINE VILLALBA
                                    for x in range (len(productos)):
                                        print(f"CANTIDAD DE STOCK= {stockInicial} PRODUCTOS= {productos}")
                                        s=str(input("INGRESE 0 SI DESEA SALIR (para continuar oprima 1): "))
                                        if s in salir:
                                            break
                                        elif s in continuar:
                                            consultaProd=str(input("INGRESE EL NOMBRE DEL PRODUCTO QUE VENDIO: ")).lower()
                                            while consultaProd not in productos:
                                                consultaProd=str(input("PRODUCTO INEXISTENTE, POR FAVOR INGRESE EL NOMBRE DEL PRODUCTO QUE VENDIO: ")).lower()
                                            if consultaProd in productos:
                                                pos=productos.index(consultaProd)
                                                cantidadVendida=int(input(f"INGRESE LA CANTIDAD VENDIDA DEL {consultaProd}: "))
                                                while cantidadVendida<0 or cantidadVendida>stockInicial[pos]:
                                                    cantidadVendida=int(input(f"ERROR. cantidad IMPOSIBLE del {consultaProd} ingrese una cantidad DISPONIBLE: "))
                                                stockInicial[pos]=stockInicial[pos]-cantidadVendida
                                                gananciasMadeline=gananciasMadeline+precioProd[pos]*cantidadVendida
                                                cochesVendidosM=cochesVendidosM+cantidadVendida
                                                if stockInicial[pos]<100: #AVISO DE STOCK
                                                    print(f"Quedan menos de de 100 unidades de {productos[pos]}. CANTIDAD RESTANTE: {stockInicial[pos]}")
                                                    agregarStock=int(input("¿Desea agregar STOCK (0) para NO y (1) para SI?: "))
                                                    if agregarStock==0:
                                                        print("OK")
                                                    elif agregarStock==1:
                                                        añadir=int(input(f"INGRESE LA CANTIDAD QUE DESEA AÑADIRLE A {productos[pos]}: "))
                                                        stockInicial[pos]=stockInicial[pos]+añadir
                                                        s=int(input("IGRESE 0 SI DESEA SALIR: "))
                                                        print(stockInicial)
                                                        if s in salir:
                                                            break
                                                        while s not in salir or continuar:
                                                            s=str(input("ERROR INGRESE 0 SI DESEA SALIR (para continuar oprima cualquier 1): "))
                                elif vendedores==2:#TOMAS MONTENEGRO
                                    for x in range (len(productos)):
                                        print(f"CANTIDAD DE STOCK= {stockInicial} PRODUCTOS= {productos}")
                                        s=str(input("INGRESE 0 SI DESEA SALIR (para continuar oprima 1): "))
                                        if s in salir:
                                            break
                                        elif s in continuar:
                                            consultaProd=str(input("INGRESE EL NOMBRE DEL PRODUCTO QUE VENDIO: ")).lower()
                                            while consultaProd not in productos:
                                                consultaProd=str(input("PRODUCTO INEXISTENTE, POR FAVOR INGRESE EL NOMBRE DEL PRODUCTO QUE VENDIO: ")).lower()
                                            if consultaProd in productos:
                                                pos=productos.index(consultaProd)
                                                cantidadVendida=int(input(f"INGRESE LA CANTIDAD VENDIDA DEL {consultaProd}: "))
                                                while cantidadVendida<0 or cantidadVendida>stockInicial[pos]:
                                                    cantidadVendida=int(input(f"ERROR. cantidad IMPOSIBLE DEL {consultaProd} ingrese una cantidad DISPONIBLE: "))
                                                stockInicial[pos]=stockInicial[pos]-cantidadVendida
                                                gananciasTomas=gananciasTomas+precioProd[pos]*cantidadVendida
                                                cochesVendidosT=cochesVendidosT+cantidadVendida
                                                if stockInicial[pos]<100:
                                                    print(f"Quedan menos de de 100 unidades de {productos[pos]} CANTIDAD RESTANTE: {stockInicial[pos]}")
                                                    agregarStock=int(input("¿Desea agregar STOCK (0) para NO y (1) para SI?: "))
                                                    if agregarStock==0:
                                                        print("OK")
                                                    elif agregarStock==1:
                                                        añadir=int(input(f"INGRESE LA CANTIDAD QUE DESEA AÑADIRLE A {productos[pos]}: "))
                                                        stockInicial[pos]=stockInicial[pos]+añadir
                                                        salir=int(input("IGRESE 0 SI DESEA SALIR: "))
                                                        print(stockInicial)
                                                        while s not in salir or continuar:
                                                            s=str(input("ERROR INGRESE 0 SI DESEA SALIR (para continuar oprima cualquier 1): "))
                                                        if salir in salir:
                                                            break
                                                        elif salir in continuar:
                                                            print("OK continue añadiendo")    
                            elif opciones_VV==3:
                                print("COMPARACIÓN DE VENDEDORES POR BIMESTRE (20 POR CIENTO DE BONIFICACIÓN EN LAS GANANCIAS AL QUE MAS VENTAS OBTUVO)")
                                print(f"CANTIDAD VENDIDA POR EDU: {cochesVendidosE}                GANANCIAS DE EDU: {gananciasEdu}")
                                print(f"CANTIDAD VENDIDA POR GAEL: {cochesVendidosG}               GANANCIAS DE GAEL: {gananciasGael}")
                                print(f"CANTIDAD VENDIDA POR MADELINE: {cochesVendidosM}           GANANCIAS DE MADELINE: {gananciasMadeline}")
                                print(f"CANTIDAD VENDIDA POR TOMAS: {cochesVendidosT}              GANANCIAS DE TOMAS: {gananciasTomas}")
                                terminarCarga=str(input("Ingrese (0) si desea continuar con la carga de ventas y (1) para terminar: "))
                                if terminarCarga=="0":
                                    break
                                elif terminarCarga=="1":
                                    gananciasTodos=[cochesVendidosE,cochesVendidosG,cochesVendidosM,cochesVendidosT]
                                    salesMans=['EDUARDO','GAEL','MADELINE','TOMAS']
                                    maxima = max(gananciasTodos)
                                    posMax2 = gananciasTodos.index(maxima)
                                    repetidos=0
                                    for x in range(len(gananciasTodos)):
                                        if gananciasTodos[x]==maxima:
                                            repetidos=repetidos+1
                                    if repetidos>1:
                                        print(f"NINGUNO OBTIENE UNA BONFICACIÓN")
                                        bonoE.append("NO") ; bonoG.append("NO") ; bonoM.append("NO") ; bonoT.append("NO")
                                    else:
                                        sueldoDeTodos=[gananciasEdu,gananciasGael,gananciasMadeline,gananciasTomas]
                                        bono=sueldoDeTodos[posMax2]*(1+0.2)
                                        print(f"EL QUE MAS VENDIO FUE {salesMans[posMax2]} CON {maxima} VENTAS Y OBTIENE UN BONO DE= {bono}") #bonificación
                                        if posMax2==0:
                                            bonoE.append("SI") ; bonoG.append("NO") ; bonoM.append("NO") ; bonoT.append("NO")
                                            gananciasEdu=bono
                                        if posMax2==1:
                                            bonoG.append("SI") ; bonoE.append("NO") ; bonoM.append("NO") ; bonoT.append("NO")
                                            gananciasGael=bono
                                        if posMax2==2:
                                            bonoM.append("SI") ; bonoE.append("NO") ; bonoG.append("NO") ; bonoT.append("NO")
                                            gananciasMadeline=bono
                                        if posMax2==3:
                                            bonoT.append("SI") ; bonoM.append("NO") ; bonoG.append("NO") ; bonoE.append("NO")
                                            gananciasTomas=bono
                    elif ingreso_opciones==3: #MENÚ DE AREA DE RR.HH
                        while True:
                            opciones_AS=int(input("""AREA DE RECURSOS HUMANOS
                            0. CERRAR MENÚ
                            1. LIQUIDACIÓN DE SUELDOS
                            INGRESE ALGUNAS DE LAS SIGUIENTES OPCIONES: """))
                            if opciones_AS==0:
                                desea_terminar=str(input("¿DESEA TERMINAR CON LA OPERACIÓN SI O NO?: ")).upper()
                                if desea_terminar=="SI":
                                    cierre=str(input("¿Esta seguro SI o NO?: ")).lower()
                                    if cierre=="si":
                                        break
                                    else:
                                        print("Ok que tenga buen dia")
                            elif opciones_AS==1:
                                print("LIQUIDACIÓN DE SUELDOS (SI EL EMPLEADO OBTUVO BONO SE LE SUMARA EN EL SUELDO NETO Y SE LE SUMA PORCENTAJE DE ANTIGUEDAD AL SUELDO)")
                                empleados=['EDUARDO', 'GAEL', 'MADELINE', 'TOMÁS'] ; antiguedad=[10, 20, 30, 40]; sueldoBase=1000000 ; porcentajeEmpresa=0.3
                                sueldoNetoE=sueldoBase+gananciasEdu+gananciasEdu*(1-0.3)+gananciasEdu*(1+0.1) ; sueldoNetoG=sueldoBase+gananciasGael+gananciasGael*(1-0.3)+gananciasGael*(1+0.2)
                                sueldoNetoM=sueldoBase+gananciasMadeline+gananciasMadeline*(1-0.3)+gananciasMadeline*(1+0.3) ; sueldoNetoT=sueldoBase+gananciasTomas+gananciasTomas*(1-0.3)+ gananciasTomas*(1+0.4)
                                print("{:^20}" "{:^20}" "{:^20}" "{:^29}" "{:^20}" "{:^20}""{:^20}" .format("EMPLEADOS", "SUELDO BASE", "ANTIGUEDAD", "RECAUDADO DE LAS VENTAS", "BONO","PORCENTAJE DE LA EMPRESA", "SUELDO NETO"))       
                                print("{:^20}" "{:^20}" "{:^20}" "{:^29}" "{:^20}" "{:^20}""{:^20}".format(f"{empleados[0]}", f"{sueldoBase}", f"{antiguedad[0]}", f"{gananciasEdu}", f"{bonoE}", f"{porcentajeEmpresa}", f"{sueldoNetoE}"))
                                print("{:^20}" "{:^20}" "{:^20}" "{:^29}" "{:^20}" "{:^20}""{:^20}".format(f"{empleados[1]}", f"{sueldoBase}", f"{antiguedad[1]}", f"{gananciasGael}", f"{bonoG}", f"{porcentajeEmpresa}", f"{sueldoNetoG}"))
                                print("{:^20}" "{:^20}" "{:^20}" "{:^29}" "{:^20}" "{:^20}""{:^20}".format(f"{empleados[2]}", f"{sueldoBase}", f"{antiguedad[2]}", f"{gananciasMadeline}", f"{bonoM}", f"{porcentajeEmpresa}", f"{sueldoNetoM}"))
                                print("{:^20}" "{:^20}" "{:^20}" "{:^29}" "{:^20}" "{:^20}""{:^20}".format(f"{empleados[3]}", f"{sueldoBase}", f"{antiguedad[3]}", f"{gananciasTomas}", f"{bonoT}", f"{porcentajeEmpresa}", f"{sueldoNetoT}"))
                    elif ingreso_opciones==0: #CIERRE DE SESIÓN
                        s=str(input("¿DESEA TERMINAR CON LA SESIÓN (0) SI  (1) NO?: "))
                        if s in salir:
                            break
                        elif s in continuar:
                            print("Ok Entonces siga con lo que le corresponda hacer")