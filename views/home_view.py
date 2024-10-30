import flet as ft



class HomeView:
    def __init__(self, page) -> None:
        self.page = page


    def build(self):
        return ft.Container(
            expand=True,
            bgcolor=ft.colors.ORANGE_200,
            content=ft.Text(value='HOME PAGE', size=24)    
        )
