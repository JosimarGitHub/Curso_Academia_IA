import flet as ft

from lib.data.repositories.counter_repository import CounterRepository
from lib.ui.counter.view_models.counter_view_model import CounterViewModel
from lib.ui.counter.widgets.counter_screen import CounterScreen


def main(page: ft.Page) -> None:
    page.title = "Counter"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    counter_repository = CounterRepository()
    counter_view_model = CounterViewModel(counter_repository)
    counter_screen = CounterScreen(counter_view_model)

    page.add(counter_screen.build())
    page.floating_action_button = counter_screen.build_floating_action_button()
    page.floating_action_button_location = ft.FloatingActionButtonLocation.END_FLOAT


ft.app(target=main)
