import flet as ft  


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
                            controls=[
                                ft.Image(
                                    src='/images/appccmtj_image.jpg',  
                                    width=240,
                                    height=240,
                                    fit=ft.ImageFit.CONTAIN  
                                ),
                                ft.Container(height=10),
                                ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Container(
                                                    content=ft.Column(
                                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Icon(
                                                                name=ft.icons.QR_CODE_SCANNER,
                                                                size=70,
                                                                color=ft.colors.WHITE  
                                                            ),
                                                            ft.Text(
                                                                value='LER  QRCODE',
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
                                                            ft.Icon(
                                                                name=ft.icons.PHONE_IPHONE_ROUNDED,
                                                                size=70,
                                                                color=ft.colors.WHITE  
                                                            ),
                                                            ft.Text(
                                                                value='SELFIE  HISTÓRICA',
                                                                size=14,
                                                                color=ft.colors.WHITE    
                                                            )  
                                                        ]    
                                                    )  
                                                )  
                                            ],
                                            spacing=180    
                                        )    
                                    ]    
                                )    
                            ]
                        ),
                        alignment=ft.alignment.center   
                    )  
                ]
            )
        )

