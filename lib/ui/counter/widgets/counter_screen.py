import flet as ft

from lib.ui.counter.view_models.counter_view_model import CounterViewModel


class CounterScreen:
    """View do contador — apenas apresenta dados e encaminha eventos ao ViewModel."""

    def __init__(self, view_model: CounterViewModel) -> None:
        self._view_model = view_model
        self._count_text = ft.Text(value=self._view_model.count_label, size=20)
        self._view_model.add_listener(self._on_view_model_changed)

    def build(self) -> ft.Control:
        return ft.Column(
            controls=[
                ft.Text(
                    value="Você pressionou o botão quantas vezes:",
                    size=16,
                ),
                self._count_text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
        )

    def build_floating_action_button(self) -> ft.FloatingActionButton:
        return ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            tooltip="Incrementar",
            on_click=lambda _: self._view_model.increment.execute(),
        )

    def _on_view_model_changed(self) -> None:
        self._count_text.value = self._view_model.count_label
        self._count_text.update()
