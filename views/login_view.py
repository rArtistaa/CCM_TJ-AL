import flet as ft
from controllers.auth_controller import AuthController


class LoginView:
    def __init__(self, route_controller) -> None:
        self.route_controller = route_controller
        self.controller = AuthController()
        self.show_password = False  

        self.email_label = 'Email'
        self.password_label = 'Senha'


    def toggle_password_visibility(self, e):
        self.show_password = not self.show_password
        self.password_field.password = not self.show_password
        self.icon_button.icon = (
            ft.icons.VISIBILITY if self.show_password else ft.icons.VISIBILITY_OFF
        )
        self.icon_button.update()  
        self.password_field.update()  
    

    def build(self):
        self.icon_button = ft.IconButton(
            icon=ft.icons.VISIBILITY_OFF,
            on_click=self.toggle_password_visibility
        )

        self.password_field = ft.TextField(
            width=290,  
            label=self.password_label,
            password=True,  
            border_width=0,
        )
        
        return ft.Container(
            expand=True,  
            bgcolor="#081c44",
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,  
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
                controls=[
                    ft.Container(  
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Container(height=50),
                                ft.Image(src="/images/logo_museu.jpg"),
                                ft.Container(height=30),
                                ft.TextField(
                                    width=340,
                                    label=self.email_label,
                                    border_width=0, 
                                ),
                                ft.Container(height=20),
                                ft.Row(
                                    controls=[
                                        self.password_field,
                                        self.icon_button  
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER  
                                ),
                                ft.Container(height=30),
                                ft.ElevatedButton(
                                    text='Entrar',
                                    bgcolor='#58a45c',
                                    color=ft.colors.WHITE,
                                    height=50,
                                    width=340,   
                                ),                     
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            spans=[
                                                ft.TextSpan('Não tem uma conta?  '),
                                                ft.TextSpan(
                                                    'Registrar',
                                                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                                                    on_click=lambda e: self.route_controller.change_route('/register')   
                                                )    
                                            ]                                        
                                        )    
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER    
                                )
                            ],
                        ),
                        padding=40,
                        alignment=ft.alignment.center
                    )
                ]
            )
        )
