from lib.data.repositories.sensor_repository import SensorRepository
from lib.ui.core.commands.command import Command0
from lib.ui.core.listenable.change_notifier import ChangeNotifier


class SensorViewModel(ChangeNotifier):
    """ViewModel da leitura de sensor — gerencia estado e expõe comando para UI."""

    def __init__(self, sensor_repository: SensorRepository) -> None:
        super().__init__()
        self._sensor_repository = sensor_repository
        self._reading_result = None
        self._is_loading = False
        self.read_sensor = Command0(self._load_sensor)

    @property
    def sensor_value(self) -> str:
        if self._reading_result is None:
            return "****"
        if self._reading_result.success and self._reading_result.value is not None:
            return self._reading_result.value
        return "****"

    @property
    def status_message(self) -> str:
        if self._reading_result is None:
            return "Clique em Ler sensor para iniciar"
        if self._is_loading:
            return "Requisição em andamento..."
        return self._reading_result.status_message

    @property
    def has_error(self) -> bool:
        return self._reading_result is not None and not self._reading_result.success

    @property
    def is_loading(self) -> bool:
        return self._is_loading

    def _load_sensor(self) -> None:
        self._is_loading = True
        self.notify_listeners()
        self._reading_result = self._sensor_repository.read_sensor()
        self._is_loading = False
        self.notify_listeners()
