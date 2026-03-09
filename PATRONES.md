# Patrones de Diseño - Proyecto Laberinto

Este documento explica los patrones de diseño implementados en el proyecto.

---

## 1. Patrón Composite

### Descripción
El patrón **Composite** permite componer objetos en estructuras de árbol para representar jerarquías parte-todo. Permite a los clientes tratar objetos individuales y composiciones de objetos de manera uniforme.

### Estructura en el proyecto

```
ElementoMapa (Component - Clase abstracta)
    │
    ├── Contenedor (Composite)
    │       │
    │       ├── Laberinto (contiene Habitaciones)
    │       │
    │       └── Habitacion (contiene Paredes, Puertas)
    │
    └── Hoja (Leaf)
            │
            ├── Pared
            │     └── ParedBomba
            │
            └── Puerta
```

### Participantes

| Rol | Clase | Descripción |
|-----|-------|-------------|
| **Component** | `ElementoMapa` | Define la interfaz común para todos los elementos (`entrar()`, `recorrer()`) |
| **Composite** | `Contenedor` | Almacena hijos y define operaciones para gestionarlos (`agregar_hijo()`, `eliminar_hijo()`) |
| **Leaf** | `Hoja` | Elementos sin hijos (Pared, Puerta) |

### Código clave

```python
# ElementoMapa.py - Component
class ElementoMapa(ABC):
    def __init__(self):
        self.padre = None  # Referencia al padre
    
    @abstractmethod
    def entrar(self) -> None:
        pass

# Contenedor.py - Composite
class Contenedor(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.hijos = []
    
    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

# Hoja.py - Leaf
class Hoja(ElementoMapa):
    def obtener_hijos(self):
        return []  # Las hojas no tienen hijos
```

### Beneficios
- **Tratamiento uniforme**: Puedes llamar `entrar()` en cualquier elemento sin importar si es Laberinto, Habitación o Pared
- **Navegación bidireccional**: Cada elemento conoce a su padre (`elemento.padre`)
- **Estructura jerárquica**: Representa naturalmente la relación Laberinto → Habitaciones → Elementos

---

## 2. Patrón Iterator

### Descripción
El patrón **Iterator** proporciona una forma de acceder a los elementos de un objeto agregado secuencialmente sin exponer su representación interna.

### Implementación en el proyecto

Se implementa mediante el método `recorrer()` que usa **generadores de Python** (`yield`).

### Participantes

| Rol | Clase | Descripción |
|-----|-------|-------------|
| **Aggregate** | `Contenedor` | Define `recorrer()` que devuelve un iterador |
| **Iterator** | Generador Python | El `yield` crea un iterador implícito |
| **ConcreteAggregate** | `Laberinto`, `Habitacion` | Heredan el recorrido de `Contenedor` |

### Código clave

```python
# Contenedor.py
def recorrer(self):
    """Iterador interno: primero el contenedor, luego sus hijos recursivamente"""
    yield self
    for h in self.hijos:
        yield from h.recorrer()

def __iter__(self):
    """Iterador externo: permite usar for elemento in laberinto"""
    return self.recorrer()

# Hoja.py
def recorrer(self):
    yield self  # Las hojas solo se devuelven a sí mismas
```

### Uso

```python
# Recorrer todos los elementos del laberinto
for elemento in laberinto:
    print(elemento)
```

### Beneficios
- **Encapsulación**: No expone la estructura interna del laberinto
- **Recorrido uniforme**: Un solo bucle recorre todo el árbol
- **Pythonic**: Usa generadores nativos de Python

---

## 3. Patrón Factory Method

### Descripción
El patrón **Factory Method** define una interfaz para crear objetos, pero deja que las subclases decidan qué clases instanciar. Factory Method permite a una clase delegar la instanciación a las subclases.

### Estructura en el proyecto

```
Juego (Creator)
    │
    └── JuegoBomba (ConcreteCreator)

ElementoMapa (Product)
    │
    ├── Habitacion (ConcreteProduct)
    ├── Pared (ConcreteProduct)
    │     └── ParedBomba (ConcreteProduct)
    └── Puerta (ConcreteProduct)
```

### Participantes

| Rol | Clase | Descripción |
|-----|-------|-------------|
| **Product** | `ElementoMapa` | Interfaz de los objetos que crea el factory |
| **ConcreteProduct** | `Habitacion`, `Pared`, `Puerta`, `ParedBomba` | Implementaciones concretas |
| **Creator** | `Juego` | Declara los factory methods |
| **ConcreteCreator** | `JuegoBomba` | Sobrescribe factory methods para crear productos específicos |

### Código clave

```python
# Juego_arreglar.py - Creator
class Juego:
    def fabricarPared(self):
        return Pared()
    
    def fabricarPuerta(self, lado1=None, lado2=None):
        return Puerta(lado1, lado2)
    
    def fabricarHabitacion(self, id_habitacion=None):
        return Habitacion(id_habitacion)
    
    def fabricarLab2HabFM(self):
        """Operación que usa los factory methods"""
        hab1 = self.fabricarHabitacion()
        hab2 = self.fabricarHabitacion()
        # ... usa fabricarPared(), fabricarPuerta() ...

# JuegoBomba.py - ConcreteCreator
class JuegoBomba(Juego):
    def fabricarPared(self):
        return ParedBomba()  # Sobrescribe para crear ParedBomba
```

### Uso

```python
# Crear laberinto normal
juego = Juego()
laberinto = juego.fabricarLab2HabFM()  # Paredes normales

# Crear laberinto con bombas (mismo código, diferentes productos)
juego_bomba = JuegoBomba()
laberinto = juego_bomba.fabricarLab2HabFM()  # ParedBomba en vez de Pared
```

### Beneficios
- **Extensibilidad**: Añadir nuevos tipos de laberintos sin modificar el código existente
- **Encapsulación de la creación**: El cliente no necesita saber qué clases concretas se instancian
- **Principio Open/Closed**: Abierto para extensión, cerrado para modificación

---

## Diagrama de Clases General

```
                    ┌─────────────────┐
                    │  ElementoMapa   │ (Abstract)
                    │─────────────────│
                    │ + padre         │
                    │ + entrar()      │
                    │ + recorrer()    │
                    └────────┬────────┘
                             │
           ┌─────────────────┴─────────────────┐
           │                                   │
    ┌──────┴──────┐                    ┌───────┴───────┐
    │ Contenedor  │                    │     Hoja      │
    │─────────────│                    │───────────────│
    │ + hijos[]   │                    │ + recorrer()  │
    │ + agregar() │                    └───────┬───────┘
    │ + eliminar()│                            │
    │ + recorrer()│                    ┌───────┴───────┐
    └──────┬──────┘                    │               │
           │                      ┌────┴────┐    ┌─────┴─────┐
    ┌──────┴──────┐               │  Pared  │    │  Puerta   │
    │             │               └────┬────┘    └───────────┘
┌───┴────┐  ┌─────┴─────┐              │
│Laberinto│  │Habitacion │        ┌────┴─────┐
└─────────┘  └───────────┘        │ParedBomba│
                                  └──────────┘

         ┌─────────┐
         │  Juego  │ (Creator)
         │─────────│
         │ fabricarPared()      │
         │ fabricarHabitacion() │
         │ fabricarPuerta()     │
         └────┬────┘
              │
       ┌──────┴──────┐
       │ JuegoBomba  │ (ConcreteCreator)
       │─────────────│
       │ fabricarPared() → ParedBomba │
       └─────────────┘
```

---

## 4. Patrón Decorator

### Descripción
El patrón **Decorator** asigna dinámicamente responsabilidades adicionales a un objeto. Los decoradores proporcionan una alternativa flexible a la subclasificación para extender la funcionalidad.

### Estructura en el proyecto

```
ElementoMapa (Component)
    │
    ├── Laberinto, Habitacion, Puerta, Pared (ConcreteComponent)
    │
    └── Decorator ─────────────────┐
            │                      │  +componente
            ├── Bomba              │
            └── Hechizo            │
```

### Participantes

| Rol | Clase | Descripción |
|-----|-------|-------------|
| **Component** | `ElementoMapa` | Interfaz común para objetos que pueden ser decorados |
| **ConcreteComponent** | `Pared`, `Puerta`, `Habitacion` | Objetos que se pueden decorar |
| **Decorator** | `Decorator` | Clase base que envuelve un `ElementoMapa` y delega operaciones |
| **ConcreteDecorator** | `Bomba`, `Hechizo` | Añaden comportamiento específico |

### Código clave

```python
# Decorator.py - Decorator base
class Decorator(ElementoMapa):
    def __init__(self, componente: ElementoMapa):
        super().__init__()
        self._componente = componente  # Referencia al objeto envuelto
    
    def entrar(self):
        self._componente.entrar()  # Delega al componente

# Bomba.py - ConcreteDecorator
class Bomba(Decorator):
    def __init__(self, componente: ElementoMapa, activa: bool = True):
        super().__init__(componente)
        self.activa = activa
    
    def entrar(self):
        if self.activa:
            print("BOOM! La bomba explota.")
            self.activa = False
        super().entrar()  # Delega al componente envuelto

# Hechizo.py - ConcreteDecorator
class Hechizo(Decorator):
    def __init__(self, componente: ElementoMapa, tipo_hechizo: str = "misterioso"):
        super().__init__(componente)
        self.tipo_hechizo = tipo_hechizo
    
    def entrar(self):
        print(f"Un hechizo {self.tipo_hechizo} te afecta...")
        super().entrar()
```

### Uso

```python
# Decorar una pared con bomba
pared_bomba = Bomba(Pared())
pared_bomba.entrar()  # "BOOM! + Has chocado contra una pared"

# Decorar una puerta con hechizo
puerta_hechizada = Hechizo(Puerta(None, None), "de hielo")
puerta_hechizada.entrar()  # "Hechizo de hielo... + La puerta está cerrada"

# ¡Combinar decoradores!
pared_bomba_hechizada = Hechizo(Bomba(Pared()), "de fuego")
pared_bomba_hechizada.entrar()  # "Hechizo + BOOM! + Has chocado..."
```

### Diferencia con herencia (ParedBomba)

| Herencia (ParedBomba) | Decorator (Bomba) |
|-----------------------|-------------------|
| Solo puede ser Pared | Puede decorar **cualquier** ElementoMapa |
| Fijo en compilación | Dinámico en ejecución |
| Una bomba por clase | Combinable: `Hechizo(Bomba(Pared))` |

### Beneficios
- **Flexibilidad**: Añadir Bomba a Puerta, Pared o Habitación
- **Combinable**: Múltiples decoradores en cadena
- **Open/Closed**: Añadir funcionalidad sin modificar clases existentes
- **Dinámico**: Decidir decoraciones en tiempo de ejecución

---

## 5. Patrón Strategy

### Descripción
El patrón **Strategy** define una familia de algoritmos, encapsula cada uno en un objeto, de modo que son intercambiables. Permite cambiar el algoritmo sin afectar al cliente que lo usa.

### Estructura en el proyecto

Se implementan **dos aplicaciones** del Strategy:

**1. Modo de comportamiento para Bicho:**
```
Bicho (Context)
    │
    └── +modo ──→ Modo (Strategy)
                    │
              ┌─────┴─────┐
              │           │
          Agresivo    Perezoso
        (ConcreteStrategy)
```

**2. Orientaciones para Habitación:**
```
Habitacion (Context)
    │
    └── +orientaciones ──→ Orientacion (Strategy)
                               │
                    ┌──────────┼──────────┬──────────┐
                    │          │          │          │
                  Norte      Sur       Este      Oeste
                            (ConcreteStrategy)
```

### Participantes

| Rol | Clase | Descripción |
|-----|-------|-------------|
| **Strategy** | `Modo`, `Orientacion` | Interfaz común para los algoritmos |
| **ConcreteStrategy** | `Agresivo`, `Perezoso`, `Norte`, `Sur`, `Este`, `Oeste` | Implementaciones concretas |
| **Context** | `Bicho`, `Habitacion` | Mantiene referencia a un Strategy y delega |

### Código clave

```python
# Modo.py - Strategy abstracto
class Modo(ABC):
    @abstractmethod
    def actuar(self, bicho) -> str:
        pass

# Agresivo.py - ConcreteStrategy
class Agresivo(Modo):
    def actuar(self, bicho) -> str:
        print(f"{bicho.nombre} está en modo AGRESIVO: ¡Ataca ferozmente!")

# Perezoso.py - ConcreteStrategy
class Perezoso(Modo):
    def actuar(self, bicho) -> str:
        print(f"{bicho.nombre} está en modo PEREZOSO: Se mueve lentamente...")

# Bicho.py - Context
class Bicho:
    def __init__(self, nombre: str, modo: Modo = None):
        self.nombre = nombre
        self._modo = modo if modo else Agresivo()
    
    @property
    def modo(self) -> Modo:
        return self._modo
    
    @modo.setter
    def modo(self, nuevo_modo: Modo):
        self._modo = nuevo_modo  # ¡Cambio en tiempo de ejecución!
    
    def actuar(self):
        self._modo.actuar(self)  # Delega al strategy
```

### Uso

```python
# Crear bicho con modo por defecto (Agresivo)
bicho = Bicho("Goblin")
bicho.actuar()  # "Goblin está en modo AGRESIVO: ¡Ataca ferozmente!"

# Cambiar modo en tiempo de ejecución
bicho.modo = Perezoso()
bicho.actuar()  # "Goblin está en modo PEREZOSO: Se mueve lentamente..."

# Orientaciones
norte = Norte()
print(norte.obtener_opuesta())  # Sur
```

### Beneficios
- **Intercambiable**: Cambiar comportamiento en tiempo de ejecución
- **Elimina condicionales**: No necesitas `if modo == "agresivo"` 
- **Open/Closed**: Añadir nuevos modos sin modificar Bicho
- **Reutilizable**: El mismo Modo puede usarse en diferentes Bichos

---

## Resumen de Patrones

| Patrón | Propósito | Clases principales |
|--------|-----------|-------------------|
| **Composite** | Estructurar el laberinto como árbol jerárquico | `ElementoMapa`, `Contenedor`, `Hoja` |
| **Iterator** | Recorrer todos los elementos uniformemente | `recorrer()`, `__iter__()` |
| **Factory Method** | Crear diferentes tipos de laberintos sin cambiar código | `Juego`, `JuegoBomba` |
| **Decorator** | Añadir responsabilidades dinámicamente a objetos | `Decorator`, `Bomba`, `Hechizo` |
| **Strategy** | Encapsular algoritmos intercambiables | `Modo`, `Agresivo`, `Perezoso`, `Bicho` |

---

*Última actualización: Marzo 2026*
