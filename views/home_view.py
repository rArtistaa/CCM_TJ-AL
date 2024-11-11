import flet as ft
import asyncio


class HomeView:
    def __init__(self) -> None:
        pass


    def build(self):
        return ft.Container(
            expand=True,
            bgcolor='#071F49',
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                ft.Container(height=0),
                                ft.Image(
                                    src='/images/appccmtj_image.jpg',
                                    width=110,
                                    height=110,
                                    fit=ft.ImageFit.CONTAIN
                                ),
                                ft.Container(height=10),
                                ft.Container(
                                    content=ft.Row(
                                        spacing=40,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Column(
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Container(
                                                        content=ft.Column(
                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.IconButton(
                                                                    content=ft.Image(
                                                                        src='/images/qrcode_icon.png',
                                                                        fit=ft.ImageFit.CONTAIN,
                                                                        width=60,
                                                                        height=60,    
                                                                    ),
                                                                    icon_size=40,
                                                                    icon_color=ft.colors.WHITE,
                                                                    style=ft.ButtonStyle(
                                                                        shape=ft.RoundedRectangleBorder(6)
                                                                    ),
                                                                    offset=(0, 0.1)
                                                                ),
                                                                ft.Text(
                                                                    value='LER QRCODE',
                                                                    size=14,
                                                                    color=ft.colors.WHITE
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        content=ft.Column(
                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.IconButton(
                                                                    content=ft.Image(
                                                                        src='/images/agenda_icon.png',
                                                                        fit=ft.ImageFit.CONTAIN,
                                                                        width=60,
                                                                        height=60    
                                                                    ),
                                                                    icon_size=40,
                                                                    icon_color=ft.colors.WHITE,
                                                                    style=ft.ButtonStyle(
                                                                        shape=ft.RoundedRectangleBorder(6)
                                                                    ),
                                                                    offset=(0, 0.1),
                                                                    on_click=lambda e: e.page.go('/schedule')
                                                                ),
                                                                ft.Text(
                                                                    value='AGENDA',
                                                                    size=14,
                                                                    color=ft.colors.WHITE
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        content=ft.Column(
                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.IconButton(
                                                                    content=ft.Image(
                                                                        src='/images/accessibility_icon.png',
                                                                        fit=ft.ImageFit.CONTAIN,
                                                                        width=60,
                                                                        height=60    
                                                                    ),
                                                                    icon_size=40,
                                                                    icon_color=ft.colors.WHITE,
                                                                    style=ft.ButtonStyle(
                                                                        shape=ft.RoundedRectangleBorder(6)
                                                                    ),
                                                                    offset=(0, 0.1)
                                                                ),
                                                                ft.Text(
                                                                    value='ACESSIBILIDADE',
                                                                    size=14,
                                                                    color=ft.colors.WHITE
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ],
                                                spacing=16
                                            ),                                
                                            ft.Column(
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Container(
                                                        content=ft.Column(
                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.IconButton(
                                                                    content=ft.Image(
                                                                        src='/images/selfie_icon.png',
                                                                        fit=ft.ImageFit.CONTAIN,
                                                                        width=60,
                                                                        height=60    
                                                                    ),
                                                                    icon_size=40,
                                                                    icon_color=ft.colors.WHITE,
                                                                    style=ft.ButtonStyle(
                                                                        shape=ft.RoundedRectangleBorder(6)
                                                                    ),
                                                                    offset=(0, 0.1)
                                                                ),
                                                                ft.Text(
                                                                    value='SELFIE HISTÓRICA',
                                                                    size=14,
                                                                    color=ft.colors.WHITE
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        content=ft.Column(
                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.IconButton(
                                                                    content=ft.Image(
                                                                        src='/images/home_icon.png',
                                                                        fit=ft.ImageFit.CONTAIN,
                                                                        width=60,
                                                                        height=60    
                                                                    ),
                                                                    icon_size=40,
                                                                    icon_color=ft.colors.WHITE,
                                                                    style=ft.ButtonStyle(
                                                                        shape=ft.RoundedRectangleBorder(6)
                                                                    ),
                                                                    offset=(0, 0.1)
                                                                ),
                                                                ft.Text(
                                                                    value='LEVE PARA CASA',
                                                                    size=14,
                                                                    color=ft.colors.WHITE
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        content=ft.Column(
                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                            controls=[
                                                                ft.IconButton(
                                                                    content=ft.Image(
                                                                        src='/images/ccmtj_icon.png',
                                                                        fit=ft.ImageFit.CONTAIN,
                                                                        width=60,
                                                                        height=60    
                                                                    ),
                                                                    icon_size=40,
                                                                    icon_color=ft.colors.WHITE,
                                                                    style=ft.ButtonStyle(
                                                                        shape=ft.RoundedRectangleBorder(6)
                                                                    ),
                                                                    offset=(0, 0.1),
                                                                    on_click=lambda e: e.page.go('/ccmtj')
                                                                ),
                                                                ft.Text(
                                                                    value='CCM TJ AL',
                                                                    size=14,
                                                                    color=ft.colors.WHITE
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ],
                                                spacing=16
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                    ),
                    ft.Container(height=120),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.INFO,
                                icon_size=18,
                                icon_color='#c8c4d4',
                                on_click=lambda e: e.page.go('/aboutapp')
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        text='SOBRE O APP',
                                        style=ft.TextStyle(
                                            size=12,
                                            color='#c8c4d4'     
                                        ),
                                        on_click=lambda e: e.page.go('/aboutapp')
                                    )    
                                ]
                            )    
                        ]    
                    )
                ]
            )
        )
