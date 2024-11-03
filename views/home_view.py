import flet as ft



class HomeView:
    def __init__(self, page) -> None:
        self.page = page


    def build(self):
        return ft.Container(
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.RED, ft.colors.PURPLE],
                tile_mode=ft.GradientTileMode.MIRROR    
            ),
            width=150,
            height=150,
            border_radius=5
        )
