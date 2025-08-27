'''
Archivo principal para la ejecución del programa
'''

if (__name__=='__main__'):
    #Importación modulos
    import modules.mensajes as msg
    import modules.customs as cu
    import modules.titles as t
    import modules.menus as me
    import modules.salir as sa
    import modules.funcionLineal as fl
    import modules.funcionCuadratica as fc
    import modules.funcionRacional as fr

    isActive = True
    while (isActive):
        try:
            cu.borrarPantalla()
            t.show_title()
            me.show_menu()
            opcMenu = int(input('Seleccione:__'))
            
            match opcMenu:
                case 1:
                    cu.borrarPantalla()
                    t.show_lineal()
                    m, b = fl.pedir_valores()
                    line = fl.LinealFunction(m, b)
                    line.plot()
                    cu.pausarPantalla()
                case 2:
                    cu.borrarPantalla()
                    t.show_quadratic()
                    a, b, c = fc.pedir_valores()
                    parabola = fc.QuadraticFunction(a, b, c)
                    parabola.plot()
                    cu.pausarPantalla()
                case 3: 
                    cu.borrarPantalla()
                    t.show_rational()
                    fr.pedir_valores()
                case 4:
                    isActive = sa.validateData(msg.msgInfo)
                case _:
                    print (msg.msgCase)
                    cu.pausarPantalla()
            
        except ValueError:
            print (msg.msgExcept)
            cu.pausarPantalla()
            continue