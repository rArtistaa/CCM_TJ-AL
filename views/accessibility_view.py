import flet as ft
from utils.navigation_bar import create_navigation_bar


class AccessibilityView:
    def __init__(self) -> None:
        pass


    def build(self):
        return ft.View(
            bgcolor='#071F49',
            scroll=ft.ScrollMode.AUTO,
            padding=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                *create_navigation_bar(
                    on_back_click=lambda e: e.page.go('/home'),
                    color='#7089C5'    
                ),
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Image(
                            src='/images/appccmtj_image.jpg',
                            height=104,
                            width=104,
                            fit=ft.ImageFit.CONTAIN    
                        ),
                        ft.ElevatedButton(
                            content=ft.Row(
                                controls=[
                                    ft.Image(
                                        src='/images/accessibility_icon.png',
                                        fit=ft.ImageFit.CONTAIN,
                                        width=54,  
                                        height=54
                                    ),
                                    ft.Text(
                                        "ACESSIBILIDADE",
                                        style=ft.TextStyle(size=16, color=ft.colors.WHITE)  
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                spacing=0  
                            ),
                            bgcolor='#7089C5',
                            width=234,
                            height=69
                        ),
                        ft.Container(height=2),
                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    text='O',
                                    style=ft.TextStyle(size=17)    
                                ),
                                ft.TextSpan(
                                    text=' Centro de Cultura e Memória TJ/AL',
                                    style=ft.TextStyle(weight=ft.FontWeight.BOLD, size=17)   
                                ),
                                ft.TextSpan(
                                    text=' Centro de Cultura e Memória TJ/AL',
                                    style=ft.TextStyle(size=17)  
                                )    
                            ],
                            width=350   
                        ),
                        ft.Container(height=2),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            width=290,
                            controls=[
                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=22,
                                    controls=[
                                        ft.IconButton(
                                            content=ft.Image(
                                                src='/images/ad_icon.png',
                                                fit=ft.ImageFit.CONTAIN,

                                            ),
                                            width=93,
                                            height=93,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=8),
                                                bgcolor='#7089C5'   
                                            )
                                        ),
                                        ft.Text(
                                            value='AESCRIÇÃO',
                                            size=17    
                                        )    
                                    ]    
                                ),
                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=22,
                                    controls=[
                                        ft.IconButton(
                                            content=ft.Image(
                                                src='/images/braile_icon.png',
                                                fit=ft.ImageFit.CONTAIN,

                                            ),
                                            width=93,
                                            height=93,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=8),
                                                bgcolor='#7089C5'   
                                            )
                                        ),
                                        ft.Text(
                                            value='BRAILLE',
                                            size=17    
                                        )      
                                    ]    
                                )    
                            ]    
                        ),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            controls=[
                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=22,
                                    controls=[
                                        ft.IconButton(
                                            content=ft.Image(
                                                src='/images/libras_icon.png',
                                                fit=ft.ImageFit.CONTAIN,

                                            ),
                                            width=93,
                                            height=93,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=8),
                                                bgcolor='#7089C5'   
                                            )
                                        ),
                                        ft.Text(
                                            value='VÍDEOS COM LIBRAS',
                                            size=17,
                                            width=102,
                                            text_align=ft.TextAlign.CENTER    
                                        )    
                                    ]    
                                ),
                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=22,
                                    controls=[
                                        ft.IconButton(
                                            content=ft.Image(
                                                src='/images/braile_icon.png',
                                                fit=ft.ImageFit.CONTAIN,

                                            ),
                                            width=93,
                                            height=93,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=8),
                                                bgcolor='#7089C5'   
                                            )
                                        ),
                                        ft.Text(
                                            value='BRAILLE',
                                            size=17    
                                        )      
                                    ]    
                                )    
                            ]    
                        )
                    ]    
                )    
            ]    
        )
