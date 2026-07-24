from lib.data.repositories.counter_repository import CounterRepository
from lib.ui.core.commands.command import Command0
from lib.ui.core.listenable.change_notifier import ChangeNotifier


class CounterViewModel(ChangeNotifier):
    """ViewModel do contador — gerencia estado e expõe comandos para a View."""

    def __init__(self, counter_repository: CounterRepository) -> None:
        super().__init__()
        self._counter_repository = counter_repository
        self.increment = Command0(self._increment)

    @property
    def count(self) -> int:
        return self._counter_repository.get_counter().value

    @property
    def count_label(self) -> str:
        presses = "vez" if self.count == 1 else "vezes"
        return f"Você pressionou o botão {self.count} {presses}."

    def _increment(self) -> None:
        self._counter_repository.increment()
        self.notify_listeners()
