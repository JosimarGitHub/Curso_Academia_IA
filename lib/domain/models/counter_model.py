from dataclasses import dataclass


@dataclass(frozen=True)
class CounterModel:
    """Modelo de domínio que representa o estado do contador."""

    value: int
