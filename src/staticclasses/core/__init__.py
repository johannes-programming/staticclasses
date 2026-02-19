from typing import *

__all__ = ["staticmeta", "staticclass"]


class staticmeta(type):
    def __call__(cls: type, *args: Any, **kwargs: Any) -> None:
        "This magic method implements calling the class."
        e = "Not allowed to instantiate static class %r!"
        e %= cls.__name__
        raise TypeError(e)


class staticclass(metaclass=staticmeta): ...
