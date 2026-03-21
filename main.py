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
# Abstract Factory imports
from LaberintoFactory import LaberintoFactory
from LaberintoBombasFactory import LaberintoBombasFactory
from LaberintoFuegoFactory import LaberintoFuegoFactory
from ParedFuego import ParedFuego
from PuertaBomba import PuertaBomba
from PuertaFuego import PuertaFuego
# Builder imports
from Director import Director
from LaberintoBuilder import LaberintoBuilder
from Builder import Builder
from Armario import Armario

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

def probar_template_method():
    """
    Prueba el patrón Template Method con Bicho/Modo.
    El Template Method está en Modo.actua() que llama a atacar() y duerme().
    """
    print("\n" + "=" * 50)
    print("PROBANDO PATRÓN TEMPLATE METHOD")
    print("=" * 50)
    
    # --- Template Method: actua() define el esqueleto ---
    print("\n-- 1. Bicho Agresivo ejecuta TEMPLATE METHOD actua():")
    print("   (El algoritmo: atacar -> duerme está definido en Modo)")
    goblin = Bicho("Goblin", Agresivo(), poder=15)
    goblin.actua()  # Template Method: llama atacar() y duerme() en orden
    
    print("\n-- 2. Bicho Perezoso ejecuta TEMPLATE METHOD actua():")
    print("   (Mismo algoritmo, pero comportamiento diferente)")
    troll = Bicho("Troll", Perezoso(), poder=20)
    troll.actua()  # Mismo esqueleto, diferentes implementaciones
    
    print("\n-- 3. Cambiar modo en tiempo de ejecución y ejecutar Template:")
    goblin.modo = Perezoso()
    goblin.actua()
    
    print("\n-- 4. Llamar operaciones primitivas individualmente:")
    print("   Atacar (Agresivo):")
    orco = Bicho("Orco", Agresivo(), poder=25)
    orco.atacar()
    print("   Duerme (Perezoso):")
    orco.modo = Perezoso()
    orco.duerme()


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
    bicho.actua()
    
    print("\n-- 2. Cambiar modo a Perezoso en tiempo de ejecución:")
    bicho.modo = Perezoso()
    bicho.actua()
    
    print("\n-- 3. Crear bicho directamente con modo Perezoso:")
    bicho2 = Bicho("Troll", Perezoso())
    print(f"   {bicho2}")
    bicho2.actua()
    
    print("\n-- 4. Cambiar el troll a modo Agresivo:")
    bicho2.modo = Agresivo()
    bicho2.actua()
    
    # --- Probar nuevos métodos del diagrama ---
    print("\n-- 5. Probar métodos caminar, atacar, duerme:")
    print("   Goblin (Perezoso):")
    bicho.caminar()
    bicho.atacar()
    bicho.duerme()
    
    print("\n   Troll (Agresivo):")
    bicho2.caminar()
    bicho2.atacar()
    bicho2.duerme()
    
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

def probar_singleton():
    """
    Prueba el patrón Singleton con las Orientaciones.
    Verifica que Norte(), Sur(), Este(), Oeste() siempre retornan la misma instancia.
    """
    print("\n" + "=" * 50)
    print("PROBANDO PATRÓN SINGLETON")
    print("=" * 50)
    
    # --- 1. Verificar que siempre es la misma instancia ---
    print("\n-- 1. Crear múltiples 'instancias' de Norte:")
    norte1 = Norte()
    norte2 = Norte()
    norte3 = Norte()
    
    print(f"   norte1: id = {id(norte1)}")
    print(f"   norte2: id = {id(norte2)}")
    print(f"   norte3: id = {id(norte3)}")
    print(f"   ¿norte1 is norte2? {norte1 is norte2}")
    print(f"   ¿norte1 is norte3? {norte1 is norte3}")
    
    # --- 2. Verificar todas las orientaciones ---
    print("\n-- 2. Verificar Singleton en todas las orientaciones:")
    
    sur1, sur2 = Sur(), Sur()
    este1, este2 = Este(), Este()
    oeste1, oeste2 = Oeste(), Oeste()
    
    print(f"   Sur:   sur1 is sur2 = {sur1 is sur2}")
    print(f"   Este:  este1 is este2 = {este1 is este2}")
    print(f"   Oeste: oeste1 is oeste2 = {oeste1 is oeste2}")
    
    # --- 3. Verificar que obtener_opuesta() retorna el Singleton ---
    print("\n-- 3. Verificar que obtener_opuesta() retorna el Singleton:")
    norte = Norte()
    sur_desde_norte = norte.obtener_opuesta()
    sur_directo = Sur()
    
    print(f"   Norte().obtener_opuesta() is Sur() = {sur_desde_norte is sur_directo}")
    
    # --- 4. Beneficio: comparación por identidad ---
    print("\n-- 4. Beneficio: comparación por identidad (más eficiente):")
    orientacion_actual = Norte()
    print(f"   orientacion_actual is Norte() = {orientacion_actual is Norte()}")

def probar_abstract_factory():
    """
    Prueba el patrón Abstract Factory con LaberintoBombasFactory y LaberintoFuegoFactory.
    """
    print("\n" + "=" * 50)
    print("PROBANDO PATRÓN ABSTRACT FACTORY")
    print("=" * 50)
    
    # --- 1. Laberinto con familia BOMBAS ---
    print("\n-- 1. Crear laberinto con LaberintoBombasFactory:")
    juego = Juego()
    juego.setFactory(LaberintoBombasFactory())
    laberinto_bombas = juego.fabricarLab2HabAF()
    
    print(f"   {laberinto_bombas}")
    hab1 = laberinto_bombas.obtener_habitaciones(1)
    if hab1:
        print(f"   Habitación 1: {hab1}")
        print(f"   Norte (ParedBomba): {hab1.norte}")
        print(f"   Sur (PuertaBomba): {hab1.sur}")
    
    print("\n   Entrando por el norte (ParedBomba):")
    hab1.norte.entrar()
    
    print("\n   Intentando abrir puerta bomba:")
    hab1.sur.abrir()
    
    # --- 2. Laberinto con familia FUEGO ---
    print("\n-- 2. Crear laberinto con LaberintoFuegoFactory:")
    juego2 = Juego()
    juego2.setFactory(LaberintoFuegoFactory())
    laberinto_fuego = juego2.fabricarLab2HabAF()
    
    print(f"   {laberinto_fuego}")
    hab1_fuego = laberinto_fuego.obtener_habitaciones(1)
    if hab1_fuego:
        print(f"   Habitación 1: {hab1_fuego}")
        print(f"   Norte (ParedFuego): {hab1_fuego.norte}")
        print(f"   Sur (PuertaFuego): {hab1_fuego.sur}")
    
    print("\n   Entrando por el norte (ParedFuego):")
    hab1_fuego.norte.entrar()
    
    print("\n   Intentando pasar por puerta fuego cerrada:")
    hab1_fuego.sur.entrar()
    
    print("\n   Abriendo puerta fuego y pasando:")
    hab1_fuego.sur.abrir()
    hab1_fuego.sur.entrar()
    
    # --- 3. Mostrar flexibilidad: cambiar factory en tiempo de ejecución ---
    print("\n-- 3. Flexibilidad: mismo Juego, diferente factory:")
    juego3 = Juego()
    
    print("   Con LaberintoBombasFactory:")
    juego3.setFactory(LaberintoBombasFactory())
    lab1 = juego3.fabricarLab2HabAF()
    h1 = lab1.obtener_habitaciones(1)
    print(f"     Pared norte: {h1.norte}")
    
    print("   Con LaberintoFuegoFactory:")
    juego3.setFactory(LaberintoFuegoFactory())
    lab2 = juego3.fabricarLab2HabAF()
    h2 = lab2.obtener_habitaciones(3)  # IDs 3 y 4 porque el contador sigue
    print(f"     Pared norte: {h2.norte}")

def probar_builder():
    """
    Prueba el patrón Builder con Director y LaberintoBuilder.
    Construye laberintos desde archivos JSON.
    """
    print("\n" + "=" * 50)
    print("PROBANDO PATRÓN BUILDER")
    print("=" * 50)
    
    import os
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_laberintos = os.path.join(ruta_base, "laberintos")
    
    # --- 1. Crear laberinto simple (2 habitaciones) ---
    print("\n-- 1. Crear laberinto desde lab2hab.json:")
    director = Director()
    archivo = os.path.join(ruta_laberintos, "lab2hab.json")
    
    try:
        juego = director.procesar(archivo)
        print(f"   Laberinto creado: {juego.laberinto}")
        
        hab1 = juego.obtenerHabitacion(1)
        hab2 = juego.obtenerHabitacion(2)
        
        if hab1:
            print(f"   Hab 1: {hab1}")
            print(f"   Orientaciones de Hab 1: {[str(o) for o in hab1.orientaciones]}")
        if hab2:
            print(f"   Hab 2: {hab2}")
        
        # Verificar que la puerta conecta las habitaciones
        print(f"\n   ¿Puerta sur de Hab1 es puerta? {hab1.sur.es_puerta()}")
        print(f"   ¿Puerta conecta Hab1 y Hab2? lado1={hab1.sur.lado1.id}, lado2={hab1.sur.lado2.id}")
        
    except FileNotFoundError:
        print(f"   ERROR: No se encontró el archivo {archivo}")
    
    # --- 2. Crear laberinto con 4 habitaciones, bombas y bichos ---
    print("\n-- 2. Crear laberinto desde lab4hab2bichos.json:")
    director2 = Director()
    archivo2 = os.path.join(ruta_laberintos, "lab4hab2bichos.json")
    
    try:
        juego2 = director2.procesar(archivo2)
        print(f"   Laberinto creado: {juego2.laberinto}")
        
        # Mostrar habitaciones
        for i in range(1, 5):
            hab = juego2.obtenerHabitacion(i)
            if hab:
                print(f"   Hab {i}: N={hab.norte}, S={hab.sur}, E={hab.este}, O={hab.oeste}")
        
        # Mostrar bichos
        print(f"\n   Bichos creados: {len(juego2.obtenerBichos())}")
        for bicho in juego2.obtenerBichos():
            print(f"     - {bicho.nombre} en {bicho.posicion}")
        
        # Recorrer laberinto
        print("\n   Recorriendo laberinto con Iterator:")
        for i, elem in enumerate(juego2.laberinto, 1):
            if i <= 10:  # Limitar output
                print(f"     {i}. {elem}")
            elif i == 11:
                print(f"     ... (y más elementos)")
                break
                
    except FileNotFoundError:
        print(f"   ERROR: No se encontró el archivo {archivo2}")
    
    # --- 3. Probar Builder directamente (sin Director) ---
    print("\n-- 3. Usar LaberintoBuilder directamente:")
    builder = LaberintoBuilder()
    builder.fabricarLaberinto()
    builder.fabricarHabitacion(1)
    builder.fabricarHabitacion(2)
    builder.fabricarPuertaLado1Or1Lado2Or2(1, "Este", 2, "Oeste")
    
    lab = builder.obtenerLaberinto()
    print(f"   Laberinto: {lab}")
    
    h1 = lab.obtener_habitaciones(1)
    h2 = lab.obtener_habitaciones(2)
    print(f"   Hab1.Este es puerta: {h1.este.es_puerta()}")
    print(f"   Hab2.Oeste es puerta: {h2.oeste.es_puerta()}")
    print(f"   ¿Son la misma puerta? {h1.este is h2.oeste}")

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
    
    # 11. Probar patrón Template Method
    probar_template_method()
    
    # 12. Probar patrón Singleton
    probar_singleton()
    
    # 13. Probar patrón Abstract Factory
    probar_abstract_factory()
    
    # 14. Probar patrón Builder
    probar_builder()
    
    print("\n" + "#" * 60)
    print("#" + " " * 12 + "TODAS LAS PRUEBAS COMPLETADAS" + " " * 12 + "#")
    print("#" * 60 + "\n")

if __name__ == "__main__":
    main()
