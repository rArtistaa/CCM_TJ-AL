import flet as ft
from contents.exclusive_content_components.video_content import videos_content


class TakeItHomeView:
    def __init__(self) -> None:
        self.main_access_container = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,  
        )
        self.history_stack = []
        self.current_container = 'initial'
    

    def initial_content(self):
        return [
            ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        value='CONTEÚDO EXCLUSIVO',
                        size=22,
                        font_family='FuturaPTBold',
                        color=ft.colors.WHITE,
                        offset=(0, -0.6)
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.IconButton(
                                        content=ft.Image(
                                            src='/images/video_icon.png',
                                            width=60,
                                            height=60,
                                            fit=ft.ImageFit.CONTAIN    
                                        ),
                                        width=80,
                                        height=80,
                                        padding=0,
                                        on_click=lambda e: self.update_main_access_view(videos_content())    
                                    ),
                                    ft.Text(
                                        value='VÍDEOS',
                                        size=17,
                                        font_family='FuturaPTMedium',
                                        color=ft.colors.WHITE  
                                    )    
                                ]    
                            ),
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.IconButton(
                                        content=ft.Image(
                                            src='/images/image_icon.png',
                                            width=60,
                                            height=60,
                                            fit=ft.ImageFit.CONTAIN,   
                                        ),
                                        width=80,
                                        height=80,
                                        padding=0    
                                    ),
                                    ft.Text(
                                        value='IMAGENS',
                                        size=17,
                                        font_family='FuturaPTMedium',
                                        color=ft.colors.WHITE  
                                    )    
                                ]    
                            )    
                        ],
                        offset=(0, -0.16)    
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.IconButton(
                                        content=ft.Image(
                                            src='/images/360_icon.png',
                                            width=76,
                                            height=76,
                                            fit=ft.ImageFit.CONTAIN    
                                        ),
                                        width=80,
                                        height=80,
                                        padding=0    
                                    ),
                                    ft.Text(
                                        value='PASSEIO 360º',
                                        size=17,
                                        font_family='FuturaPTMedium',
                                        color=ft.colors.WHITE,
                                        text_align=ft.TextAlign.CENTER,
                                        offset=(0, -0.1)  
                                    )    
                                ],
                                offset=(0.1, 0)    
                            ),
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.IconButton(
                                        content=ft.Image(
                                            src='/images/doc_icon.png',
                                            width=60,
                                            height=60,
                                            fit=ft.ImageFit.CONTAIN,   
                                        ),
                                        width=80,
                                        height=80,
                                        padding=0    
                                    ),
                                    ft.Text(
                                        value='DOCUMENTOS',
                                        size=17,
                                        font_family='FuturaPTMedium',
                                        color=ft.colors.WHITE,
                                        offset=(0, -0.1)  
                                    )    
                                ]    
                            )    
                        ],
                        offset=(0, 0.05)    
                    ),
                    ft.Container(
                        content=ft.Image(
                            src='/images/icone_logo_ccmtj.png',
                            fit=ft.ImageFit.COVER, 
                        ),
                        height=68,
                        width=265,
                        offset=(0, 0.8)
                    ),
                    ft.Container(height=100),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.INFO,
                                icon_size=18,
                                icon_color=ft.colors.WHITE,
                                on_click=lambda e: e.page.go("/aboutapp"),
                                width=30,
                                height=30,
                                padding=0
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        text="SOBRE O APP",
                                        style=ft.TextStyle(
                                            size=12, color=ft.colors.WHITE
                                        ),
                                        on_click=lambda e: e.page.go("/aboutapp"),
                                    )
                                ]
                            ),
                        ],
                    )
                ],
                alignment=ft.alignment.center    
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
            bgcolor='#272628',
            scroll=ft.ScrollMode.AUTO,
            padding=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.top_left,
                            padding=ft.padding.only(left=50, top=50),
                            content=ft.IconButton(
                                icon=ft.icons.ARROW_BACK_IOS_ROUNDED,
                                bgcolor='#F5A017',
                                icon_color='#E7EBE0',
                                on_click=self.go_back,
                                width=50,
                                height=50,
                            ),
                                
                        ),
                        ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=30,
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                ft.Image(
                                    src='/images/appccmtj_logo.png',
                                    height=130,
                                    width=130,
                                    fit=ft.ImageFit.CONTAIN,
                                    offset=(0, -0.2)
                                ),
                                self.main_access_container  
                            ]
                        )
                    ]
                )     
            ]
        )
