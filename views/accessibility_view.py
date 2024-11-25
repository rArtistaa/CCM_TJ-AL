import flet as ft
from utils.navigation_bar import create_navigation_bar
from contents.accessibility_components.audio_desc_content import aud_desc_content
from contents.accessibility_components.braile_content import braile_content
from contents.accessibility_components.videos_content import videos_content


class AccessibilityView:
    def __init__(self) -> None:
        self.main_access_container = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,  
        )
        self.history_stack = []
        self.current_container = 'initial'


    def initial_content(self):
            return [
                ft.ElevatedButton(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src='/images/accessibility_icon.png',
                                fit=ft.ImageFit.CONTAIN,
                                width=54,  
                                height=54,
                                offset=(-0.3, 0)
                            ),
                            ft.Text(
                                "ACESSIBILIDADE",
                                style=ft.TextStyle(
                                    size=17,
                                    color=ft.colors.WHITE,
                                    font_family='FuturaPTMedium'
                                )  
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                                
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
                            style=ft.TextStyle(font_family='FuturaPTDemi', size=17)   
                        ),
                        ft.TextSpan(
                            text=' Centro de Cultura e Memória TJ/AL',
                            style=ft.TextStyle(font_family='FuturaPTLight' ,size=17)  
                        )    
                    ],
                    width=350   
                ),
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
                                    ),
                                    on_click=lambda e: self.update_main_access_view(aud_desc_content())
                                ),
                                ft.Text(
                                    value='DESCRIÇÃO',
                                    style=ft.TextStyle(
                                        font_family='FuturaPTMedium',
                                        size=17    
                                    ),
                                    text_align=ft.TextAlign.CENTER,
                                    width=102    
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
                                    ),
                                    on_click=lambda e: self.update_main_access_view(braile_content())
                                ),
                                ft.Text(
                                    value='BRAILLE',
                                    style=ft.TextStyle(
                                        font_family='FuturaPTMedium',
                                        size=17    
                                    ),
                                    text_align=ft.TextAlign.CENTER,
                                    width=102    
                                )      
                            ]    
                        )    
                    ]    
                ),
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
                                        src='/images/libras_icon.png',
                                        fit=ft.ImageFit.CONTAIN,

                                    ),
                                    width=93,
                                    height=93,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=8),
                                        bgcolor='#7089C5'   
                                    ),
                                    on_click=lambda e: self.update_main_access_view(videos_content())
                                ),
                                ft.Text(
                                    value='VÍDEOS COM LIBRAS',
                                    style=ft.TextStyle(
                                        font_family='FuturaPTMedium',
                                        size=17    
                                    ),
                                    text_align=ft.TextAlign.CENTER,
                                    width=102    
                                )    
                            ]    
                        ),
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=22,
                            controls=[
                                ft.IconButton(
                                    content=ft.Image(
                                        src='/images/cc_icon.png',
                                        fit=ft.ImageFit.CONTAIN,

                                    ),
                                    width=93,
                                    height=93,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=8),
                                        bgcolor='#7089C5'   
                                    ),
                                    on_click=lambda e: self.update_main_access_view(videos_content())
                                ),
                                ft.Text(
                                    value='VIDEOS COM LEGENDA',
                                    style=ft.TextStyle(
                                        font_family='FuturaPTMedium',
                                        size=17    
                                    ),
                                    text_align=ft.TextAlign.CENTER,
                                    width=102    
                                )      
                            ]    
                        )    
                    ]    
                )
            ]


    def update_main_access_view(self, new_content):
        self.history_stack.append(self.main_access_container.controls)
        self.main_access_container.controls.clear()
        self.main_access_container.controls.extend(new_content)
        self.main_access_container.update()
        self.current_container = 'modified'
    

    def go_back(self, e):
        if self.current_container == 'initial':
            e.page.go('/home')
        elif self.current_container == 'modified':
             self.main_access_container.controls.clear()
             self.main_access_container.controls.extend(self.initial_content())
             self.main_access_container.update()
             self.current_container = 'initial'


    def build(self):
        self.main_access_container.controls.extend(self.initial_content())

        return ft.View(
            bgcolor='#071F49',
            scroll=ft.ScrollMode.AUTO,
            padding=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                *create_navigation_bar(
                    on_back_click=self.go_back,
                    color='#7089C5'
                ),
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=30,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Image(
                            src='/images/appccmtj_logo.png',
                            height=104,
                            width=104,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        self.main_access_container  
                    ]
                )
            ]
        )
