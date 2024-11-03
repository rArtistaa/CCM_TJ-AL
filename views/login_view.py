import flet as ft
from controllers.auth_controller import AuthController
import asyncio


class LoginView:
    def __init__(self) -> None:
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


    async def handle_login(self, e):
        email = self.email_field.value
        password = self.password_field.value

        self.error_message.visible = False
        self.login_button.disabled = True
        self.error_message.update()
        self.login_button.update()

        await asyncio.sleep(0.8)  

        if self.controller.authenticate(email, password):
            e.page.go('/home')
        else:
            self.error_message.value = 'Email ou senha incorretos!'
            self.password_field.value = ''
            self.password_field.update()
            self.error_message.visible = True

        self.login_button.disabled = False
        self.error_message.update()
        self.login_button.update()


    def build(self):
        self.icon_button = ft.IconButton(
            icon=ft.icons.VISIBILITY_OFF,
            on_click=self.toggle_password_visibility
        )

        self.email_field = ft.TextField(
            width=340,
            label=self.email_label,
            border_width=0,
        )

        self.password_field = ft.TextField(
            width=290,  
            label=self.password_label,
            password=True,  
            border_width=0,
        )

        self.error_message = ft.Text(
            value='',
            color=ft.colors.RED,
            visible=False,  
        )

        self.login_button = ft.ElevatedButton(
            text='Entrar',
            bgcolor={
                ft.ControlState.DEFAULT: '#58a45c',
                ft.ControlState.DISABLED: '#A0C4A6'   
            },
            color=ft.colors.WHITE,
            height=50,
            width=340,
            on_click=lambda e: asyncio.run(self.handle_login(e))  
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
                                ft.Image(
                                    src="/images/logo_museu.jpg",
                                    width=300,
                                    height=300,
                                    fit=ft.ImageFit.CONTAIN
                                ),
                                ft.Container(height=30),
                                self.email_field,
                                ft.Container(height=20),
                                ft.Row(
                                    controls=[
                                        self.password_field,
                                        self.icon_button  
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER  
                                ),
                                self.error_message, 
                                ft.Container(height=30),
                                self.login_button,                     
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            spans=[
                                                ft.TextSpan('Não tem uma conta?  '),
                                                ft.TextSpan(
                                                    'Registrar',
                                                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                                                    on_click=lambda e: e.page.go('/register')   
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
