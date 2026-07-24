from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class SensorReadingModel:
    """Representa o resultado de uma leitura de sensor remota."""

    value: Optional[str]
    status_message: str
    success: bool
