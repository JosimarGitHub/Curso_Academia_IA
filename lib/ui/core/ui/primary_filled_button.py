import flet as ft


def primary_filled_button(
    text: str,
    icon: ft.Icon | None = None,
    on_click: ft.ControlEventHandler | None = None,
) -> ft.FilledButton:
    """Botão compartilhado com estilo padrão da aplicação."""
    return ft.FilledButton(text=text, icon=icon, on_click=on_click)
