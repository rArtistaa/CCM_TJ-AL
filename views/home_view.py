import flet as ft


class HomeView:
    def __init__(self) -> None:
        pass

    def build(self):
        print("Construindo HomeView")  
        return ft.Container(
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.RED, ft.colors.YELLOW]
            ),
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Bem-vindo à HomeView!", color=ft.colors.WHITE, size=24)
                ]
            )
        )
