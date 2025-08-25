'''
Archivo principal para la ejecución del programa
'''

if (__name__=='__main__'):

    import modules.mensajes as m
    import modules.customs as c
    import modules.titles as t

    isActive = True
    while (isActive):
        try:
            c.borrarPantalla()
            print (t.title1)
            #Menú Principal
            
        except ValueError:
            print (m.msgExcept)
            c.pausarPantalla()
            continue