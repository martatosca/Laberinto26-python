# Laberinto26-python

Implementación en Python de un juego de laberinto con patrones de diseño, basada en el proyecto original de Pharo (Smalltalk).

## Descripción

El jugador recorre habitaciones conectadas por puertas, recoge objetos y debe alcanzar la salida. Los bichos se mueven de forma autónoma en hilos independientes y pueden atacar al personaje. El juego termina cuando el personaje gana (llega a la habitación de salida con la llave) o pierde (sus vidas llegan a cero).

## Estructura del proyecto

```
Laberinto26-python/
├── Laberinto26-Solucion/   # Clases principales del juego
├── Laberinto26-Builder/    # Patrón Builder (Director + LaberintoBuilder)
├── Laberinto26-Visitor/    # Patrón Visitor (abrir/cerrar puertas)
├── Laberinto26-Pruebas/    # Tests con pytest
├── laberintos/             # Ficheros JSON que definen los laberintos
└── main.py                 # Punto de entrada
```

## Requisitos

- Python 3.10 o superior
- No se requieren paquetes externos (usa solo la biblioteca estándar)
- Para ejecutar los tests: `pytest` (instalar con `pip install pytest`)

## Ejecución

```bash
python main.py
```

Para usar un laberinto distinto, edita la variable `_RUTA` en `main.py` con la ruta a cualquier fichero JSON de la carpeta `laberintos/`.

## Tests

```bash
python -m pytest Laberinto26-Pruebas/ -v
```

## Patrones de diseño implementados

| Patrón | Dónde se aplica |
|--------|----------------|
| **Composite** | `ElementoMapa` → `Contenedor` / `Hoja`. Habitaciones, armarios, puertas, trampas, llaves, etc. forman un árbol uniforme |
| **State** | `EstadoPuerta` con tres estados concretos: `Abierta`, `Cerrada` y `Bloqueada` (extensión media 2) |
| **Builder** | `Director` lee el JSON y delega la construcción en `LaberintoBuilder`; existen variantes para rombo y triángulo |
| **Visitor** | `VisitorAbrirPuertas` y `VisitorCerrarPuertas` recorren el árbol Composite sin modificar las clases visitadas |
| **Strategy** | `Modo` define el comportamiento de los bichos: `Agresivo`, `Perezoso`, `Dormido` |
| **Mediator** | `Juego` coordina la comunicación entre `Bicho` y `Personaje`; gestiona las condiciones de victoria y derrota |
| **Prototype** | Los elementos del laberinto implementan `clonar()` para poder duplicarse |

## Extensiones

### Extensiones básicas
- **Trampa** – reduce vidas al entrar
- **Escalera** – teletransporta a otra habitación
- **Dormido** – estado inicial del bicho; no ataca
- **ParedTransparente** – pared con descripción visible
- **BichoFuerte** – bicho con más poder de ataque

### Extensiones medias

**Media 1 – Llave e inventario**
- `Llave`: nueva hoja del árbol Composite; se recoge al entrar en ella
- `Personaje` gana un `inventario` con métodos `coger_llave()` y `tiene_llave()`
- Se añade `visitar_llave()` a la interfaz `Visitor`

**Media 2 – PuertaSalida + Estado Bloqueada + HabitacionSalida**
- `Bloqueada`: tercer estado de `EstadoPuerta`; solo deja pasar si el personaje lleva una llave (la consume al desbloquear)
- `PuertaSalida`: hereda de `Puerta` e inicia en estado `Bloqueada`
- `HabitacionSalida`: hereda de `Habitacion`; al entrar llama a `juego.gana_personaje()` (la llave fue el "ticket de entrada" en la `PuertaSalida`)
- `Juego` añade `gana_personaje()`, `muere_personaje()` y el flag `terminado` para detener los hilos de los bichos

