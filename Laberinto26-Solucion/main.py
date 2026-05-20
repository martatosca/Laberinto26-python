"""
main.py — Juego del Laberinto por terminal
==========================================
Comandos disponibles:
  norte / sur / este / oeste   -> mover al personaje
  coger llave                  -> recoger la llave de la habitacion actual
  atacar                       -> atacar al bicho en tu habitacion
  mirar                        -> describe la habitacion actual
  inventario                   -> muestra tus objetos
  ayuda                        -> muestra esta lista
  salir                        -> abandona la partida
"""

import time
from Juego import Juego
from Bicho import Bicho
from BichoFuerte import BichoFuerte
from Agresivo import Agresivo
from Dormido import Dormido
from Trampa import Trampa
from Escalera import Escalera
from Llave import Llave
from PuertaSalida import PuertaSalida
from HabitacionSalida import HabitacionSalida
from ParedTransparente import ParedTransparente
from Orientaciones import Norte, Sur, Este, Oeste
from Cuadrado import Cuadrado


# -----------------------------------------------------------------------
# Construccion manual del laberinto de demo
# -----------------------------------------------------------------------

def construir_laberinto(juego):
    """
    Laberinto de 4 habitaciones:

        [Hab-1: Trampa]  --Sur/Norte--  [Hab-2: Llave + Escalera->Hab4]
               |                                      |
           Este/Oeste                             Este/Oeste
               |                                      |
        [Hab-3: Bicho Dormido]  --Sur/Norte--  [Hab-4: SALIDA (BichoFuerte)]

    La puerta entre Hab-2 y Hab-4 esta BLOQUEADA (necesita llave).
    La pared Sur de Hab-3 es transparente.
    """

    # -- Habitaciones --
    hab1 = juego.fabricar_habitacion(1)
    hab2 = juego.fabricar_habitacion(2)
    hab3 = juego.fabricar_habitacion(3)

    # Hab-4 es HabitacionSalida
    hab4 = HabitacionSalida(4)
    hab4.forma = Cuadrado()
    hab4.forma.num = 4
    juego._asignar_orientaciones(hab4)
    for or_ in hab4.forma.orientaciones:
        hab4.poner_en(or_, juego.fabricar_pared())

    # -- Hijos de habitaciones --
    trampa = Trampa(danio=10)
    hab1.agregar_hijo(trampa)

    llave = Llave()
    escalera = Escalera()
    escalera.destino = hab4
    hab2.agregar_hijo(llave)
    hab2.agregar_hijo(escalera)

    # -- Pared transparente en Hab-3 sur --
    pared_trans = ParedTransparente()
    pared_trans.descripcion_otro_lado = "una habitacion con una escalera y una llave brillante"
    hab3.poner_en(juego.fabricar_sur(), pared_trans)

    # -- Puertas normales --
    p12 = juego.fabricar_puerta_lado1_lado2(hab1, hab2)
    p12.abrir()
    hab1.poner_en(juego.fabricar_sur(), p12)
    hab2.poner_en(juego.fabricar_norte(), p12)

    p13 = juego.fabricar_puerta_lado1_lado2(hab1, hab3)
    p13.abrir()
    hab1.poner_en(juego.fabricar_este(), p13)
    hab3.poner_en(juego.fabricar_oeste(), p13)

    p34 = juego.fabricar_puerta_lado1_lado2(hab3, hab4)
    p34.abrir()
    hab3.poner_en(juego.fabricar_sur(), p34)
    hab4.poner_en(juego.fabricar_norte(), p34)

    # -- Puerta BLOQUEADA entre Hab-2 y Hab-4 --
    p24 = PuertaSalida()
    p24.lado1 = hab2
    p24.lado2 = hab4
    hab2.poner_en(juego.fabricar_este(), p24)
    hab4.poner_en(juego.fabricar_oeste(), p24)

    # -- Laberinto --
    juego.laberinto = juego.fabricar_laberinto()
    for h in [hab1, hab2, hab3, hab4]:
        juego.laberinto.agregar_habitacion(h)

    # -- Bichos --
    bicho_ag = Bicho()
    bicho_ag.modo = Agresivo()
    bicho_ag.juego = juego
    juego.agregar_bicho(bicho_ag)
    hab2.entrar(bicho_ag)

    bicho_dorm = Bicho()
    bicho_dorm.modo = Dormido()
    bicho_dorm.juego = juego
    juego.agregar_bicho(bicho_dorm)
    hab3.entrar(bicho_dorm)

    bicho_fuerte = BichoFuerte()
    bicho_fuerte.modo = Agresivo()
    bicho_fuerte.juego = juego
    juego.agregar_bicho(bicho_fuerte)
    hab4.entrar(bicho_fuerte)


# -----------------------------------------------------------------------
# Narrador
# -----------------------------------------------------------------------

def describir_habitacion(personaje):
    """Imprime una descripcion detallada de la habitacion actual."""
    hab = personaje.posicion
    print(f"\n{'─'*50}")
    print(f"  📍 Estás en: {hab}")
    print(f"  ❤️  Vidas: {personaje.vidas}  |  ⚔️  Poder: {personaje.poder}")

    # Inventario
    if personaje.inventario:
        items = ", ".join(str(i) for i in personaje.inventario)
        print(f"  🎒 Inventario: {items}")
    else:
        print(f"  🎒 Inventario: vacío")

    # Hijos (objetos en la habitacion)
    objetos = [h for h in hab.hijos]
    if objetos:
        print(f"  🏠 En esta habitación hay:")
        for obj in objetos:
            print(f"      - {obj}")

    # Bichos presentes
    bichos_aqui = []
    if hasattr(hab, 'juego') or True:
        # buscamos bichos via posicion
        pass
    # Puertas/paredes en cada orientacion
    print(f"  🚪 Salidas:")
    nombres_or = [Norte(), Sur(), Este(), Oeste()]
    iconos = {"Norte": "⬆️ Norte", "Sur": "⬇️ Sur",
              "Este": "➡️ Este", "Oeste": "⬅️ Oeste"}
    for or_ in hab.forma.orientaciones:
        elem = hab.obtener_elemento(or_)
        nombre_or = iconos.get(str(or_), str(or_))
        if elem is None:
            print(f"      {nombre_or}: nada")
        elif elem.es_puerta():
            estado = "abierta" if elem.esta_abierta() else ("bloqueada 🔒" if elem.esta_bloqueada() else "cerrada")
            print(f"      {nombre_or}: puerta [{estado}]")
        elif hasattr(elem, 'es_pared_transparente') and elem.es_pared_transparente():
            print(f"      {nombre_or}: pared transparente — ves: {elem.descripcion_otro_lado}")
        else:
            print(f"      {nombre_or}: {elem}")
    print(f"{'─'*50}\n")


# -----------------------------------------------------------------------
# Bucle principal
# -----------------------------------------------------------------------

ORIENTACIONES = {
    "norte": Norte(),
    "sur":   Sur(),
    "este":  Este(),
    "oeste": Oeste(),
}

def imprimir_ayuda():
    print("""
  Comandos disponibles:
    norte / sur / este / oeste   → mover al personaje
    coger llave                  → recoger la llave de la habitación
    atacar                       → atacar al bicho en tu habitación
    mirar                        → describir la habitación actual
    inventario                   → mostrar tu inventario
    ayuda                        → mostrar esta ayuda
    salir                        → abandonar la partida
""")

def main():
    print("="*50)
    print("   JUEGO DEL LABERINTO — Extensiones completas")
    print("="*50)
    nombre = input("  Introduce el nombre de tu personaje: ").strip() or "Héroe"

    juego = Juego()
    construir_laberinto(juego)
    juego.agregar_personaje(nombre)

    personaje = juego.person

    print(f"\n  ¡Bienvenido, {personaje}!")
    print("  Objetivo: encuentra la llave y llega a la Habitación de Salida.")
    print("  Cuidado con las trampas y los bichos.")
    print("  Escribe 'ayuda' para ver los comandos.\n")

    time.sleep(0.5)
    juego.lanzar_todos_los_bichos()
    time.sleep(0.3)

    describir_habitacion(personaje)

    while not juego.esta_terminado():
        try:
            cmd = input("  > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n  Partida interrumpida.")
            break

        if not cmd:
            continue

        if cmd in ORIENTACIONES:
            ORIENTACIONES[cmd].caminar(personaje)
            if not juego.esta_terminado():
                describir_habitacion(personaje)

        elif cmd == "coger llave":
            personaje.coger_llave()

        elif cmd == "atacar":
            personaje.atacar()

        elif cmd == "mirar":
            describir_habitacion(personaje)

        elif cmd == "inventario":
            if personaje.inventario:
                print("  🎒 Inventario:", ", ".join(str(i) for i in personaje.inventario))
            else:
                print("  🎒 Tu inventario está vacío.")

        elif cmd == "ayuda":
            imprimir_ayuda()

        elif cmd == "salir":
            print("  Hasta la próxima.")
            break

        else:
            print(f"  No entiendo '{cmd}'. Escribe 'ayuda' para ver los comandos.")

    if juego.esta_terminado():
        print("  Gracias por jugar.")


if __name__ == "__main__":
    main()
