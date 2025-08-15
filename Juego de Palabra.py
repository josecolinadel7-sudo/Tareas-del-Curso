print("Bienvenido !!! Estas listo para comenzar esta historia dentro de los bosques Venezolanos")
respuesta1 = (input("Estas listo ??"))
if respuesta1 == "Si":
     print(f"{respuesta1} ""Perfecto, Comencemos !!""Estás caminando por un bosque oscuro y encuentras dos objetos: un fósforo y una Linterna.")
     respuesta2 = (input("Cual elegirias??"))
     if respuesta2 == "Fosforo":
          print(F"Eliges el {respuesta2} (Coges el fósforo y lo enciendes. Por un instante, el bosque se ilumina... ¡y ves un gran oso grizzly! El fósforo se apaga. !!")
          respuesta3 = (input("¿Quieres CORRER o ESCONDERTE detrás de un árbol?"))
          if respuesta3 == "Esconderte":
               print(f"Decides {respuesta3} detras de un Arbol pero el Arbol esta encantado")
               respuesta9 = (input("El Arbol comienza atacarte, Que haces ?? Correr o Enfrentarlo ??"))
               if respuesta9 == "Correr":
                    print(f"Corres directo al oso sin darte cuenta y te mata\n")
                    print( "GAME OVER")
               elif respuesta9 == "Enfrentarlo":
                    print(f"Al {respuesta9} te das cuenta que te quiere ayudar y te guia en el camino para regresar a casa")
               else:
                    print("¡¡ Respuesta Invalida !!")
                    respuesta10 = (input("Te dejas a ayudar, Si o No ??"))
                    if respuesta10 == "Si":
                         print(f"Te guia a casa y cuentas tu historia")
                    elif respuesta10 == "No":
                         print(f"Te alejas y el Oso te mata\n")
                         print("GAME OVER")
                    else:
                         print("¡¡ Respuesta Invalida !!")
          elif respuesta3 == "Correr":
               print(f"Encuentras una cabaña a pocos metros")
          else:
               print("¡¡ Respuesta Invalida !!")
               respuesta4 = (input("Decides entrar ??"))
               if respuesta4 == "No":
                    print("Siges corriendo hasta caer en un hueco y el Oso te mata\n")
                    print("GAME OVER")
               elif respuesta4 == "Si":
                    print(f"Encuentras una escopeta cargada")
                    respuesta5 = (input("Quieres disparar al Oso"))
                    if respuesta5 == "No":
                         print("El te mata por no disparar\n")
                         print("GAME OVER")
                    elif respuesta5 == "Si":
                         print(f"Disparas y luego regresas a casa a contar tu historia")
                         print("¡¡¡ FELICIDADES HAZ GANADO EL JUEGO !!!")
     elif respuesta2 == "Linterna":
          print(f"Eliges la {respuesta2} (Enciendes la linterna y ves un camino iluminado. De pronto, oyes algo entre los árboles")
          respuesta6 = (input("¿Quieres SEGUIR el camino o BUSCAR entre los árboles lo que hizo el ruido?"))
          if respuesta6 == "Buscar":
               print(f"Encontraras un oso grizzly y te matara\n")
               print("GAME OVER")
          elif respuesta6 == "Seguir":
               print(f"Alejandote del ruido a pocos pasos adelante encuentras un DRAGON escupe fuego")
          else:
               print("¡¡ Respuesta Invalida !!")
               respuesta7 = (input("Que haras ??, Correr o Pelear ??"))
               if respuesta7 == "Correr":
                    print("Te alcanzaran las llamas y te quemaras\n")
                    print("GAME OVER")
               elif respuesta7 == "Pelear":
                    print(f"Te das cuenta que magicamente la linterna se convierte en un sable de luz y te lanzas al DRAGON")
               else:
                    print("¡¡ Respuesta Invalida !!")
                    respuesta8 = (input("Donde atacas, Cola o Cabeza ??"))
                    if respuesta8 == "Cola":
                         print("Te golpea con la cola y luego te quema con sus llamas ardientes\n")
                         print("GAME OVER")
                    elif respuesta8 == "Cabeza":
                         print(f"Cortas la cabeza y la llevas a la ciudad a contar tu historia\n")
                         print("¡¡¡ FELICIDADES HAZ GANADO EL JUEGO !!!")
                    else:
                         print("¡¡ Respuesta Invalida !!")
     else:
          print("¡¡ Respuesta Invalida !!")
elif respuesta1 == "No":
     print(f"{respuesta1} " " Bueno, Otro dia sera")
else:
     print("Responde con un Si o No")



