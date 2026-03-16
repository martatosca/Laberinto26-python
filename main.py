"""
Main - Archivo para probar el funcionamiento del proyecto Laberinto
"""

from Laberinto import Laberinto
from Habitacion import Habitacion
from Pared import Pared
from Puerta import Puerta
from ParedBomba import ParedBomba
from Juego_arreglar import Juego
from JuegoBomba import JuegoBomba
from Decorator import Decorator
from Bomba import Bomba
from Hechizo import Hechizo
# Strategy imports
from Bicho import Bicho
from Modo import Modo
from Agresivo import Agresivo
from Perezoso import Perezoso
from Orientacion import Orientacion
from Orientaciones import Norte, Sur, Este, Oeste

def crear_laberinto_simple():
    """
    Crea un laberinto simple con 2 habitaciones conectadas por una puerta.
    """
    print("=" * 50)
    print("CREANDO LABERINTO SIMPLE (2 habitaciones)")
    print("=" * 50)
    
    # Crear el laberinto
    laberinto = Laberinto()
    
    # Crear habitaciones
    hab1 = Habitacion(1)
    hab2 = Habitacion(2)
    
    # Crear puerta entre las habitaciones
    puerta = Puerta(hab1, hab2)
    
    # Configurar habitación 1
    hab1.setNorte(Pared())
    hab1.setSur(puerta)
    hab1.setEste(Pared())
    hab1.setOeste(Pared())
    
    # Configurar habitación 2
    hab2.setNorte(puerta)
    hab2.setSur(Pared())
    hab2.setEste(Pared())
    hab2.setOeste(Pared())
    
    # Agregar habitaciones al laberinto
    laberinto.agregar_Habitacion(hab1)
    laberinto.agregar_Habitacion(hab2)
    
    return laberinto

def probar_estructura(laberinto):
    """
    Prueba la estructura del laberinto mostrando información.
    """
    print("\n" + "=" * 50)
    print("PROBANDO ESTRUCTURA DEL LABERINTO")
    print("=" * 50)
    
    print(f"\n{laberinto}")
    
    # Obtener habitaciones
    hab1 = laberinto.obtener_habitaciones(1)
    hab2 = laberinto.obtener_habitaciones(2)
    
    if hab1:
        print(f"\nHabitación 1: {hab1}")
    if hab2:
        print(f"Habitación 2: {hab2}")

def probar_entrar(laberinto):
    """
    Prueba los métodos entrar() de diferentes elementos.
    """
    print("\n" + "=" * 50)
    print("PROBANDO MÉTODO ENTRAR()")
    print("=" * 50)
    
    print("\n-- Entrando al laberinto:")
    laberinto.entrar()
    
    hab1 = laberinto.obtener_habitaciones(1)
    if hab1:
        print("\n-- Entrando a la habitación 1:")
        hab1.entrar()
        
        print("\n-- Intentando entrar por el norte (pared):")
        hab1.norte.entrar()
        
        print("\n-- Intentando entrar por el sur (puerta cerrada):")
        hab1.sur.entrar()
        
        print("\n-- Abriendo la puerta y entrando:")
        hab1.sur.abrir()
        hab1.sur.entrar()

def probar_iterador(laberinto):
    """
    Prueba el iterador (patrón Iterator) del laberinto.
    """
    print("\n" + "=" * 50)
    print("PROBANDO ITERADOR (RECORRIDO)")
    print("=" * 50)
    
    print("\nRecorriendo todos los elementos del laberinto:")
    for i, elemento in enumerate(laberinto, 1):
        print(f"  {i}. {elemento}")

def probar_pared_bomba():
    """
    Prueba la ParedBomba.
    """
    print("\n" + "=" * 50)
    print("PROBANDO PAREDBOMBA")
    print("=" * 50)
    
    pared_bomba_activa = ParedBomba(activa=True)
    pared_bomba_inactiva = ParedBomba(activa=False)
    
    print(f"\n{pared_bomba_activa}")
    print("-- Entrando en pared bomba activa:")
    pared_bomba_activa.entrar()
    
    print(f"\n{pared_bomba_inactiva}")
    print("-- Entrando en pared bomba desactivada:")
    pared_bomba_inactiva.entrar()

def probar_composite():
    """
    Prueba el patrón Composite verificando la relación padre-hijo.
    """
    print("\n" + "=" * 50)
    print("PROBANDO PATRÓN COMPOSITE (PADRE-HIJO)")
    print("=" * 50)
    
    laberinto = Laberinto()
    hab = Habitacion(1)
    pared = Pared()
    
    laberinto.agregar_Habitacion(hab)
    hab.setNorte(pared)
    
    print(f"\n¿El padre de la habitación es el laberinto? {hab.padre == laberinto}")
    print(f"¿El padre de la pared es la habitación? {pared.padre == hab}")
    
    hijos_laberinto = laberinto.obtener_hijos()
    print(f"\nHijos del laberinto: {len(hijos_laberinto)}")
    
    hijos_habitacion = hab.obtener_hijos()
    print(f"Hijos de la habitación 1: {len(hijos_habitacion)}")

def probar_factory_method():
    """
    Prueba el patrón Factory Method con la clase Juego.
    """
    print("\n" + "=" * 50)
    print("PROBANDO FACTORY METHOD (JUEGO)")
    print("=" * 50)
    
    juego = Juego()
    laberinto = juego.fabricarLab2HabFM()
    
    print(f"\n{laberinto}")
    
    hab1 = laberinto.obtener_habitaciones(1)
    hab2 = laberinto.obtener_habitaciones(2)
    
    if hab1:
        print(f"Habitación 1: {hab1}")
    if hab2:
        print(f"Habitación 2: {hab2}")
    
    print("\nRecorriendo laberinto creado con Factory Method:")
    for i, elemento in enumerate(laberinto, 1):
        print(f"  {i}. {elemento}")

def probar_juego_bomba():
    """
    Prueba JuegoBomba (Factory Method con ParedBomba).
    """
    print("\n" + "=" * 50)
    print("PROBANDO JUEGOBOMBA (FACTORY METHOD)")
    print("=" * 50)
    
    juego_bomba = JuegoBomba()
    laberinto = juego_bomba.fabricarLab2HabFM()
    
    print(f"\n{laberinto}")
    
    hab1 = laberinto.obtener_habitaciones(1)
    if hab1:
        print(f"\nHabitación 1: {hab1}")
        print("\n-- Entrando por el norte (ParedBomba):")
        hab1.norte.entrar()

def probar_decorator():
    """
    Prueba el patrón Decorator con Bomba y Hechizo.
    """
    print("\n" + "=" * 50)
    print("PROBANDO PATRÓN DECORATOR")
    print("=" * 50)
    
    # Crear elementos base
    pared = Pared()
    puerta = Puerta(None, None)
    
    print("\n-- 1. Pared normal:")
    pared.entrar()
    
    print("\n-- 2. Pared con Bomba (decorada):")
    pared_bomba = Bomba(Pared())
    print(f"   {pared_bomba}")
    pared_bomba.entrar()
    
    print("\n-- 3. Puerta con Hechizo (decorada):")
    puerta_hechizada = Hechizo(Puerta(None, None), "de hielo")
    print(f"   {puerta_hechizada}")
    puerta_hechizada.entrar()
    
    print("\n-- 4. Pared con Bomba Y Hechizo (doble decorador):")
    pared_bomba_hechizada = Hechizo(Bomba(Pared()), "de fuego")
    print(f"   {pared_bomba_hechizada}")
    pared_bomba_hechizada.entrar()
    
    print("\n-- 5. Habitación con Bomba (decorada):")
    hab_bomba = Bomba(Habitacion(99))
    print(f"   {hab_bomba}")
    hab_bomba.entrar()
    
    print("\n-- 6. Verificar que la bomba se desactiva tras explotar:")
    bomba = Bomba(Pared())
    print(f"   Primera entrada:")
    bomba.entrar()
    print(f"   Segunda entrada:")
    bomba.entrar()

def probar_strategy():
    """
    Prueba el patrón Strategy con Bicho/Modo y Orientaciones.
    """
    print("\n" + "=" * 50)
    print("PROBANDO PATRÓN STRATEGY")
    print("=" * 50)
    
    # --- Strategy con Bicho y Modo ---
    print("\n-- 1. Crear bicho con modo Agresivo (por defecto):")
    bicho = Bicho("Goblin")
    print(f"   {bicho}")
    bicho.actuar()
    
    print("\n-- 2. Cambiar modo a Perezoso en tiempo de ejecución:")
    bicho.modo = Perezoso()
    bicho.actuar()
    
    print("\n-- 3. Crear bicho directamente con modo Perezoso:")
    bicho2 = Bicho("Troll", Perezoso())
    print(f"   {bicho2}")
    bicho2.actuar()
    
    print("\n-- 4. Cambiar el troll a modo Agresivo:")
    bicho2.modo = Agresivo()
    bicho2.actuar()
    
    # --- Probar nuevos métodos del diagrama ---
    print("\n-- 5. Probar métodos caminar, atacar, dormir:")
    print("   Goblin (Perezoso):")
    bicho.caminar()
    bicho.atacar()
    bicho.dormir()
    
    print("\n   Troll (Agresivo):")
    bicho2.caminar()
    bicho2.atacar()
    bicho2.dormir()
    
    # --- Probar vidas y poder ---
    print("\n-- 6. Probar vidas y poder:")
    bicho3 = Bicho("Orco", Agresivo(), vidas=5, poder=15)
    print(f"   {bicho3}")
    bicho3.recibir_dano(2)
    print(f"   ¿Está vivo? {bicho3.esta_vivo()}")
    bicho3.recibir_dano(5)
    print(f"   ¿Está vivo? {bicho3.esta_vivo()}")
    
    # --- Strategy con Orientaciones ---
    print("\n-- 7. Probar Orientaciones:")
    norte = Norte()
    sur = Sur()
    este = Este()
    oeste = Oeste()
    
    print(f"   Norte: {norte}, opuesta: {norte.obtener_opuesta()}")
    print(f"   Sur: {sur}, opuesta: {sur.obtener_opuesta()}")
    print(f"   Este: {este}, opuesta: {este.obtener_opuesta()}")
    print(f"   Oeste: {oeste}, opuesta: {oeste.obtener_opuesta()}")
    
    # --- Probar bichos en Juego ---
    print("\n-- 8. Probar lista de bichos en Juego:")
    juego = Juego()
    juego.fabricarLab2HabFM()
    
    goblin = Bicho("Goblin", Agresivo())
    troll = Bicho("Troll", Perezoso(), vidas=5, poder=20)
    
    juego.agregarBicho(goblin)
    juego.agregarBicho(troll)
    
    print(f"   Bichos en el juego: {len(juego.obtenerBichos())}")
    for b in juego.obtenerBichos():
        print(f"     - {b}")

def main():
    """
    Función principal que ejecuta todas las pruebas.
    """
    print("\n" + "#" * 60)
    print("#" + " " * 15 + "PRUEBAS DEL LABERINTO" + " " * 16 + "#")
    print("#" * 60)
    
    # 1. Crear laberinto simple
    laberinto = crear_laberinto_simple()
    
    # 2. Probar estructura
    probar_estructura(laberinto)
    
    # 3. Probar método entrar
    probar_entrar(laberinto)
    
    # 4. Probar iterador
    probar_iterador(laberinto)
    
    # 5. Probar ParedBomba
    probar_pared_bomba()
    
    # 6. Probar patrón Composite
    probar_composite()
    
    # 7. Probar Factory Method (Juego)
    probar_factory_method()
    
    # 8. Probar JuegoBomba
    probar_juego_bomba()
    
    # 9. Probar patrón Decorator
    probar_decorator()
    
    # 10. Probar patrón Strategy
    probar_strategy()
    
    print("\n" + "#" * 60)
    print("#" + " " * 12 + "TODAS LAS PRUEBAS COMPLETADAS" + " " * 12 + "#")
    print("#" * 60 + "\n")

if __name__ == "__main__":
    main()
