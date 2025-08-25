'''
Archivo principal para la ejecución del programa
'''

if (__name__=='__main__'):

    import modules.mensajes as m
    import modules.customs as c
    import modules.titles as t
    import modules.menus as me
    import modules.salir as sa
    import modules.funcionLineal as fl

    isActive = True
    while (isActive):
        try:
            c.borrarPantalla()
            print (t.title1)
            print (me.menu1)
            opcMenu = int(input('Seleccione:__'))
            
            match opcMenu:
                case 1:
                    print ("FUNCIÓN LINEAL")
                    m, b = fl.pedir_valores()
                    line = fl.LinealFunction(m, b)
                    line.plot()
                    c.pausarPantalla()
                case 2:
                    print ("FUNCIÓN CUADRÁTICA")
                    c.pausarPantalla()
                case 3: 
                    isActive = sa.validateData(m.msgInfo)
                case _:
                    print (m.msgCase)
                    c.pausarPantalla()
            
        except ValueError:
            print (m.msgExcept)
            c.pausarPantalla()
            continue