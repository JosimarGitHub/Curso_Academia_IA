from collections.abc import Awaitable, Callable
from typing import Generic, TypeVar

from lib.ui.core.listenable.change_notifier import ChangeNotifier

T = TypeVar("T")
R = TypeVar("R")


class Command0(ChangeNotifier, Generic[R]):
    """Comando sem argumentos, equivalente ao Command0 do estudo de caso Flutter."""

    def __init__(self, action: Callable[[], Awaitable[R] | R]) -> None:
        super().__init__()
        self._action = action
        self.running = False
        self.error: Exception | None = None
        self.result: R | None = None

    def execute(self) -> None:
        if self.running:
            return

        self.running = True
        self.error = None
        self._safe_notify_listeners()

        try:
            self.result = self._action()
        except Exception as error:
            self.error = error
        finally:
            self.running = False
            self._safe_notify_listeners()

    def _safe_notify_listeners(self) -> None:
        try:
            self.notify_listeners()
        except Exception:
            pass


class Command1(ChangeNotifier, Generic[T, R]):
    """Comando com um argumento, equivalente ao Command1 do estudo de caso Flutter."""

    def __init__(self, action: Callable[[T], Awaitable[R] | R]) -> None:
        super().__init__()
        self._action = action
        self.running = False
        self.error: Exception | None = None
        self.result: R | None = None

    def execute(self, argument: T) -> None:
        if self.running:
            return

        self.running = True
        self.error = None
        self._safe_notify_listeners()

        try:
            self.result = self._action(argument)
        except Exception as error:
            self.error = error
        finally:
            self.running = False
            self._safe_notify_listeners()
