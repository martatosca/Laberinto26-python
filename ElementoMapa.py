from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterator, Optional, TYPE_CHECKING



class ElementoMapa(ABC):
    def __init__(self) -> None:
        self.padre = None

    def agregar_hijo(self, hijo: "ElementoMapa") -> None:
        raise TypeError(f"{self.__class__.__name__} no admite hijos")

    def eliminar_hijo(self, hijo: "ElementoMapa") -> None:
        raise TypeError(f"{self.__class__.__name__} no admite hijos")

    def obtener_hijos(self) -> list["ElementoMapa"]:
        raise TypeError(f"{self.__class__.__name__} no tiene hijos")

    @abstractmethod
    def entrar(self) -> None:
        pass

    @abstractmethod
    def recorrer(self) -> Iterator["ElementoMapa"]:
        pass

    #Iterador externo
    def __iter__(self) -> Iterator["ElementoMapa"]:
        return self.recorrer()

    @abstractmethod
    def __str__(self) -> str:
        pass