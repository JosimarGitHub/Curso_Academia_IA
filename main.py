import flet as ft

from lib.data.repositories.sensor_repository import SensorRepository
from lib.ui.sensor.view_models.sensor_view_model import SensorViewModel
from lib.ui.sensor.widgets.sensor_screen import SensorScreen


def main(page: ft.Page) -> None:
    page.title = "Sensor Reader"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    sensor_repository = SensorRepository()
    sensor_view_model = SensorViewModel(sensor_repository)
    sensor_screen = SensorScreen(sensor_view_model)

    page.add(sensor_screen.build())


ft.app(target=main)
