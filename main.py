'''
Archivo principal para la ejecución del programa
'''

if (__name__=='__main__'):

    import modules.mensajes as m
    import modules.customs as cu
    import modules.titles as t
    import modules.menus as me
    import modules.salir as sa
    import modules.funcionLineal as fl
    import modules.funcionCuadratica as fc

    isActive = True
    while (isActive):
        try:
            cu.borrarPantalla()
            print (t.title1)
            print (me.menu1)
            opcMenu = int(input('Seleccione:__'))
            
            match opcMenu:
                case 1:
                    print ("FUNCIÓN LINEAL")
                    m, b = fl.pedir_valores()
                    line = fl.LinealFunction(m, b)
                    line.plot()
                    cu.pausarPantalla()
                case 2:
                    print ("FUNCIÓN CUADRÁTICA")
                    a, b, c = fc.pedir_valores()
                    parabola = fc.QuadraticFunction(a, b, c)
                    parabola.plot()
                    cu.pausarPantalla()
                case 3: 
                    isActive = sa.validateData(m.msgInfo)
                case _:
                    print (m.msgCase)
                    cu.pausarPantalla()
            
        except ValueError:
            print (m.msgExcept)
            cu.pausarPantalla()
            continue