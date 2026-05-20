"""
Punto de entrada principal del laberinto — modo interactivo.

Comandos:
  norte / sur / este / oeste   -> mover al personaje
  coger llave                  -> recoger la llave de la habitacion actual
  atacar                       -> atacar al bicho en tu habitacion
  mirar                        -> describir la habitacion actual
  inventario                   -> mostrar tu inventario
  ayuda                        -> mostrar esta lista
  salir                        -> abandonar la partida
"""
import sys
import os
import io
import contextlib

_ROOT = os.path.dirname(os.path.abspath(__file__))
for _pkg in ['Laberinto26-Solucion', 'Laberinto26-Builder', 'Laberinto26-Visitor']:
    _d = os.path.join(_ROOT, _pkg)
    if _d not in sys.path:
        sys.path.insert(0, _d)

from Director import Director
from Orientaciones import Norte, Sur, Este, Oeste

_RUTA = os.path.join(_ROOT, 'laberintos', 'lab_modificaciones.json')

ORIENTACIONES = {
    "norte": Norte(),
    "sur":   Sur(),
    "este":  Este(),
    "oeste": Oeste(),
}


def describir_habitacion(personaje, juego):
    hab = personaje.posicion
    print(f"\n{'-'*50}")
    print(f"  Estas en: {hab}")
    print(f"  Vidas: {personaje.vidas}  |  Poder: {personaje.poder}")
    if personaje.inventario:
        print(f"  Inventario: {', '.join(str(i) for i in personaje.inventario)}")
    else:
        print(f"  Inventario: vacio")
    if hab.hijos:
        print(f"  Objetos en la habitacion:")
        for obj in hab.hijos:
            print(f"    - {obj}")
    bichos_aqui = [b for b in juego.bichos if b.esta_vivo() and b.posicion == hab]
    if bichos_aqui:
        print(f"  Enemigos:")
        for b in bichos_aqui:
            print(f"    - {b} (vidas: {b.vidas})")
    print(f"  Salidas:")
    for or_ in hab.forma.orientaciones:
        elem = hab.obtener_elemento(or_)
        if elem is None:
            print(f"    {or_}: nada")
        elif elem.es_puerta():
            if elem.es_puerta_salida() and not elem.esta_abierta():
                estado = "bloqueada (necesitas llave)"
            elif elem.esta_abierta():
                estado = "abierta"
            else:
                estado = "cerrada"
            print(f"    {or_}: puerta [{estado}]")
        else:
            desc = getattr(elem, 'descripcion_otro_lado', None)
            if desc:
                print(f"    {or_}: pared transparente - ves: {desc}")
            else:
                print(f"    {or_}: {elem}")
    print(f"{'-'*50}\n")


def turno_bichos(juego):
    """Los bichos en la misma habitacion que el personaje actuan segun su modo."""
    if juego.esta_terminado():
        return
    p = juego.person
    for bicho in list(juego.bichos):
        if juego.esta_terminado():
            break
        if bicho.esta_vivo() and bicho.posicion == p.posicion:
            print(f"  [{bicho} reacciona!]")
            bicho.modo.ataca(bicho)


def imprimir_ayuda():
    print("""
  Comandos disponibles:
    norte / sur / este / oeste   -> mover al personaje
    coger llave                  -> recoger la llave de la habitacion
    escalera                     -> usar la escalera de la habitacion
    atacar                       -> atacar al bicho en tu habitacion
    mirar                        -> describir la habitacion actual
    inventario                   -> mostrar tu inventario
    ayuda                        -> mostrar esta ayuda
    salir                        -> abandonar la partida
""")


if __name__ == '__main__':
    print("=" * 50)
    print("   JUEGO DEL LABERINTO")
    print("=" * 50)
    nombre = input("  Tu nombre: ").strip() or "Heroe"

    director = Director()
    with contextlib.redirect_stdout(io.StringIO()):
        director.procesar(_RUTA)
        juego = director.obtener_juego()
        juego.abrir_puertas()
        juego.agregar_personaje(nombre)
    personaje = juego.person

    print(f"\n  Bienvenido, {personaje}!")
    print("  Objetivo: coge la llave en Hab-2 y llega a la Hab-4 (salida).")
    print("  Cuidado con las trampas y los bichos.")
    imprimir_ayuda()

    describir_habitacion(personaje, juego)

    while not juego.esta_terminado():
        try:
            cmd = input("  > ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n  Partida interrumpida.")
            break

        if not cmd:
            print("  (escribe 'ayuda' para ver los comandos)")
            continue

        if cmd in ORIENTACIONES:
            print(f"  Te diriges hacia el {cmd}...")
            personaje.ir_a(ORIENTACIONES[cmd])
            if not juego.esta_terminado():
                turno_bichos(juego)
            if not juego.esta_terminado():
                describir_habitacion(personaje, juego)

        elif cmd == "coger llave":
            personaje.coger_llave()

        elif cmd == "escalera":
            hab = personaje.posicion
            escalera = next((h for h in hab.hijos if hasattr(h, 'es_escalera') and h.es_escalera()), None)
            if escalera:
                escalera.entrar(personaje)
                if not juego.esta_terminado():
                    describir_habitacion(personaje, juego)
            else:
                print("  No hay ninguna escalera en esta habitacion.")

        elif cmd == "atacar":
            bicho = juego.buscar_bicho()
            if bicho is None:
                print("  No hay ningun enemigo en esta habitacion.")
            else:
                personaje.atacar()
                if not juego.esta_terminado():
                    turno_bichos(juego)

        elif cmd == "mirar":
            describir_habitacion(personaje, juego)

        elif cmd == "inventario":
            if personaje.inventario:
                print("  Inventario:", ", ".join(str(i) for i in personaje.inventario))
            else:
                print("  Tu inventario esta vacio.")

        elif cmd == "ayuda":
            imprimir_ayuda()

        elif cmd == "salir":
            print("  Hasta la proxima.")
            break

        else:
            print(f"  No entiendo '{cmd}'. Escribe 'ayuda'.")

    if juego.esta_terminado():
        print("  Gracias por jugar.")

