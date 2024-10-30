import flet as ft


class RegisterView:
    def __init__(self, route_controller) -> None:
        self.route_controller = route_controller
    
    def build(self):
        return ft.Container(
            expand=True,
            content=ft.Column(
                controls=[
                    ft.ElevatedButton(text='Voltar', on_click=lambda e: self.route_controller.change_route('/login'))    
                ]    
            ) 
        )
