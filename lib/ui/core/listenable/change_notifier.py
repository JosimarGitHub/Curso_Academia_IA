from collections.abc import Callable


class ChangeNotifier:
    """Adaptação do ChangeNotifier do Flutter para notificar listeners."""

    def __init__(self) -> None:
        self._listeners: list[Callable[[], None]] = []

    def add_listener(self, listener: Callable[[], None]) -> None:
        self._listeners.append(listener)

    def remove_listener(self, listener: Callable[[], None]) -> None:
        self._listeners.remove(listener)

    def notify_listeners(self) -> None:
        for listener in self._listeners:
            listener()
