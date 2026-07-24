from lib.domain.models.counter_model import CounterModel


class CounterRepository:
    """Fonte única de verdade (SSOT) para o estado do contador."""

    def __init__(self) -> None:
        self._count = 0

    def get_counter(self) -> CounterModel:
        return CounterModel(value=self._count)

    def increment(self) -> CounterModel:
        self._count += 1
        return CounterModel(value=self._count)
