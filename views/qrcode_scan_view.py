import flet as ft


class QrCodeScan:
    def __init__(self) -> None:
        pass

    def build(self):
        return ft.View(
            bgcolor='#071F49',
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
                                bgcolor='#57A45D',
                                icon_color='#E7EBE0',
                                on_click=lambda e: e.page.go('/home'),
                                width=50,
                                height=50,
                            ),
                            
                        ),
                        ft.Container(
                            margin=ft.margin.only(top=-45), 
                            alignment=ft.alignment.center,
                            content=ft.Image(
                                src='/images/appccmtj_logo.png',
                                width=130,
                                height=130,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                        ),
                        ft.Container(
                            bgcolor=ft.colors.WHITE,
                            width=364,
                            height=553,
                            border_radius=ft.border_radius.all(36),
                            margin=ft.margin.only(top=16),  
                        ),
                        ft.Container(
                            width=101,
                            height=101,
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(top=-50),  
                            content=ft.IconButton(
                                content=ft.Image(
                                    src='/images/open_camera_icon.png',
                                    width=91,
                                    height=91    
                                )    
                            ),
                        ),
                    ]
                )
            ]
        )
