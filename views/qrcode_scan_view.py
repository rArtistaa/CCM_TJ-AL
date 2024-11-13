import flet as ft


class QrCodeScan:
    def __init__(self) -> None:
        pass


    def build(self):
        return ft.Container(
            expand=True,
            bgcolor='#071F49', 
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        alignment=ft.alignment.top_left,
                        padding=ft.padding.only(left=10, top=10),
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
                        margin=ft.margin.only(top=-25), 
                        alignment=ft.alignment.center,
                        content=ft.Image(
                            src='/images/appccmtj_image.jpg',
                            width=110,
                            height=110,
                            fit=ft.ImageFit.CONTAIN,
                        ),
                    ),
                    ft.Container(
                        bgcolor=ft.colors.WHITE,
                        width=364,
                        height=553,
                        border_radius=ft.border_radius.all(28),
                        margin=ft.margin.only(top=16),  
                    ),
                    ft.Container(
                        width=81,
                        height=81,
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(top=-40),  
                        content=ft.Container(
                            width=81,
                            height=81,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.WHITE, 
                            border_radius=ft.border_radius.all(40.5),  
                            border=ft.border.all(16, '#57A45D'),  
                            on_click=lambda e: print("Botão clicado!"),
                            clip_behavior=ft.ClipBehavior.ANTI_ALIAS
                        ),
                    ),
                ]
            )
        )
