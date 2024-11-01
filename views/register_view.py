import flet as ft
from controllers.auth_controller import AuthController
from validators.validators import validate_name, validate_password, validate_password_match, validate_email_exists
import asyncio


class RegisterView:
    def __init__(self, route_controller) -> None:
        self.route_controller = route_controller
        self.controller = AuthController()
        self.show_password = False

        self.name_label = 'Nome'
        self.email_label = 'Email'
        self.password_label = 'Senha'
        self.password_label2 = 'Confirme sua senha'
    

    def toggle_password_visibility(self, e):
        self.show_password = not self.show_password
        self.password_field.password = not self.show_password
        self.password_field2.password = not self.show_password
        self.icon_button.icon = (
            ft.icons.VISIBILITY if self.show_password else ft.icons.VISIBILITY_OFF
        )
        self.icon_button.update()  
        self.password_field.update() 
        self.password_field2.update() 


    async def handle_register(self, e):
        name = self.name_field.value
        email = self.email_field.value
        password = self.password_field.value
        password2 = self.password_field2.value

        self.error_message.visible = False
        self.error_message.value = ''

        valid, error_message = validate_name(name)
        if not valid:
            self.error_message.value = error_message
            self.error_message.visible = True
            self.error_message.update()
            return
        
        valid, error_message = validate_password(password)
        if not valid:
            self.error_message.value = error_message
            self.error_message.visible = True
            self.error_message.update()
            return

        valid, error_message = validate_password_match(password, password2)
        if not valid:
            self.error_message.value = error_message
            self.error_message.visible = True
            self.error_message.update()
            return

        valid, error_message = validate_email_exists(self.controller, email)
        if not valid:
            self.error_message.value = error_message
            self.error_message.visible = True
            self.error_message.update()
            return
        
        if self.controller.create_new_user(name, email, password):
            await self.route_controller.change_route('/login')
        else:
            self.error_message.value = 'Erro ao registrar. Tente novamente.'
            self.error_message.visible = True
            self.error_message.update()


    def build(self):
        self.icon_button = ft.IconButton(
            icon=ft.icons.VISIBILITY_OFF,
            on_click=self.toggle_password_visibility
        )
        
        self.name_field = ft.TextField(
            width=340,
            label=self.name_label,
            border_width=0    
        )

        self.email_field = ft.TextField(
            width=340,
            label=self.email_label,
            border_width=0    
        )

        self.password_field = ft.TextField(
            width=340,  
            label=self.password_label,
            password=True,  
            border_width=0,
        )

        self.password_field2 = ft.TextField(
            width=290,
            label=self.password_label2,
            password=True,
            border_width=0
        )

        self.error_message = ft.Text(
            value='',
            color=ft.colors.RED,
            visible=False  
        )

        self.register_button = ft.ElevatedButton(
            text='Registrar',
            bgcolor={
                ft.ControlState.DEFAULT: '#58a45c',
                ft.ControlState.DISABLED: '#A0C4A6'   
            },
            color=ft.colors.WHITE,
            height=50,
            width=340,
            on_click=lambda e: asyncio.run(self.handle_register(e))
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
                                ft.Image(
                                    src="/images/logo_museu.jpg",
                                    width=300,
                                    height=300,
                                    fit=ft.ImageFit.CONTAIN
                                ),
                                ft.Container(height=20),
                                self.name_field,
                                ft.Container(height=20),
                                self.email_field,
                                ft.Container(height=20),
                                self.password_field,
                                ft.Container(height=10),
                                ft.Row(
                                    controls=[
                                        self.password_field2, self.icon_button    
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER    
                                ),
                                ft.Container(height=30),
                                self.error_message,
                                self.register_button,
                                ft.Row(
                                    controls=[
                                        ft.Text(
                                            spans=[
                                                ft.TextSpan('Já tem uma conta?  '),
                                                ft.TextSpan(
                                                    'Entrar',
                                                    ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                                                    on_click=lambda e: self.route_controller.change_route('/login')
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

