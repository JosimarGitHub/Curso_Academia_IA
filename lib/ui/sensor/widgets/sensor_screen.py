import flet as ft

from lib.ui.sensor.view_models.sensor_view_model import SensorViewModel


class SensorScreen:
    """View que apresenta a leitura do sensor e o status de leitura."""

    def __init__(self, view_model: SensorViewModel) -> None:
        self._view_model = view_model
        self._value_text = ft.Text(value=self._view_model.sensor_value, size=32, weight=ft.FontWeight.BOLD)
        self._status_text = ft.Text(value=self._view_model.status_message, size=16)
        self._read_button_label = ft.Text("Ler sensor")
        self._read_button = ft.ElevatedButton(
            content=self._read_button_label,
            on_click=lambda _: self._view_model.read_sensor.execute(),
        )
        self._view_model.add_listener(self._on_view_model_changed)

    def build(self) -> ft.Control:
        return ft.Column(
            controls=[
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text("Leitura de sensor", size=24, weight=ft.FontWeight.BOLD),
                                ft.Divider(thickness=1),
                                ft.Text("Valor lido", size=18),
                                self._value_text,
                                ft.Text("Status da leitura", size=18),
                                self._status_text,
                                self._read_button,
                            ],
                            spacing=18,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=ft.Padding(24, 24, 24, 24),
                        width=460,
                    ),
                    elevation=4,
                    shape=ft.RoundedRectangleBorder(radius=16),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )

    def _on_view_model_changed(self) -> None:
        self._value_text.value = self._view_model.sensor_value
        self._status_text.value = self._view_model.status_message

        if self._view_model.is_loading:
            self._status_text.color = ft.Colors.BLUE
        elif self._view_model.has_error:
            self._status_text.color = ft.Colors.RED
        else:
            self._status_text.color = ft.Colors.GREEN

        self._read_button.disabled = self._view_model.is_loading
        self._read_button_label.value = "Aguarde..." if self._view_model.is_loading else "Ler sensor"

        self._value_text.update()
        self._status_text.update()
        self._read_button_label.update()
        self._read_button.update()
