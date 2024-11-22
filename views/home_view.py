import flet as ft


class HomeView:
    def __init__(self) -> None:
        pass


    def build(self):
        return ft.View(
            padding=0,
            controls=[
                ft.Container(
                    expand=True,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=["#1D1D1B", "#071F49"],
                        stops=[0, 0.44]       
                    ),
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll=ft.ScrollMode.AUTO,
                        controls=[
                            ft.Container(
                                content=ft.Column(
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    scroll=ft.ScrollMode.AUTO,
                                    controls=[
                                        ft.Container(height=20),
                                        ft.Image(
                                            src="/images/appccmtj_logo.png",
                                            width=130,
                                            height=130,
                                            fit=ft.ImageFit.CONTAIN,
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
                                                                height=87,
                                                                width=92,
                                                                content=ft.Column(
                                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                    spacing=5,
                                                                    controls=[
                                                                        ft.IconButton(
                                                                            content=ft.Image(
                                                                                src="/images/qrcode_icon.png",
                                                                                fit=ft.ImageFit.CONTAIN,
                                                                                width=80,
                                                                                height=80,
                                                                            ),
                                                                            icon_size=50,
                                                                            icon_color=ft.colors.WHITE,
                                                                            style=ft.ButtonStyle(
                                                                                shape=ft.RoundedRectangleBorder(6),
                                                                                padding=0,
                                                                            ),                         
                                                                            on_click=lambda e: e.page.go(
                                                                                "/qrcode"
                                                                            ),
                                                                            padding=0,
                                                                            alignment=ft.alignment.center_left,
                                                                        ),
                                                                        ft.Text(
                                                                            value="LER QRCODE",
                                                                            size=16,
                                                                            color=ft.colors.WHITE,
                                                                            width=190,
                                                                            font_family='FuturaPTMedium'
                                                                        ),
                                                                    ],
                                                                )
                                                            ),
                                                            ft.Container(),
                                                            ft.Container(
                                                                content=ft.Column(
                                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.IconButton(
                                                                            content=ft.Image(
                                                                                src="/images/agenda_icon.png",
                                                                                fit=ft.ImageFit.CONTAIN,
                                                                                width=80,
                                                                                height=80,
                                                                            ),
                                                                            icon_size=50,
                                                                            icon_color=ft.colors.WHITE,
                                                                            style=ft.ButtonStyle(
                                                                                shape=ft.RoundedRectangleBorder(
                                                                                    6
                                                                                )
                                                                            ),
                                                                            offset=(0, 0.1),
                                                                            on_click=lambda e: e.page.go(
                                                                                "/schedule"
                                                                            ),
                                                                            padding=0
                                                                        ),
                                                                        ft.Text(
                                                                            value="AGENDA",
                                                                            size=16,
                                                                            color=ft.colors.WHITE,
                                                                            font_family='FuturaPTMedium'
                                                                        ),
                                                                    ],
                                                                )
                                                            ),
                                                            ft.Container(
                                                                content=ft.Column(
                                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.IconButton(
                                                                            content=ft.Image(
                                                                                src="/images/accessibility_icon.png",
                                                                                fit=ft.ImageFit.CONTAIN,
                                                                                width=80,
                                                                                height=80,
                                                                            ),
                                                                            icon_size=50,
                                                                            icon_color=ft.colors.WHITE,
                                                                            style=ft.ButtonStyle(
                                                                                shape=ft.RoundedRectangleBorder(
                                                                                    6
                                                                                )
                                                                            ),
                                                                            offset=(0, 0.1),
                                                                            on_click=lambda e: e.page.go(
                                                                                "/acces"
                                                                            ),
                                                                            padding=0
                                                                        ),
                                                                        ft.Text(
                                                                            value="ACESSIBILIDADE",
                                                                            size=16,
                                                                            color=ft.colors.WHITE,
                                                                            font_family='FuturaPTMedium'
                                                                        ),
                                                                    ],
                                                                )
                                                            ),
                                                        ],
                                                        spacing=16,
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
                                                                                src="/images/selfie_icon.png",
                                                                                fit=ft.ImageFit.CONTAIN,
                                                                                width=80,
                                                                                height=80,
                                                                            ),
                                                                            icon_size=50,
                                                                            icon_color=ft.colors.WHITE,
                                                                            style=ft.ButtonStyle(
                                                                                shape=ft.RoundedRectangleBorder(
                                                                                    6
                                                                                )
                                                                            ),
                                                                            offset=(0, 0.1),
                                                                            padding=0
                                                                        ),
                                                                        ft.Text(
                                                                            value="SELFIE HISTÓRICA",
                                                                            size=16,
                                                                            color=ft.colors.WHITE,
                                                                            font_family='FuturaPTMedium'
                                                                        ),
                                                                    ],
                                                                )
                                                            ),
                                                            ft.Container(
                                                                content=ft.Column(
                                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.IconButton(
                                                                            content=ft.Image(
                                                                                src="/images/home_icon.png",
                                                                                fit=ft.ImageFit.CONTAIN,
                                                                                width=80,
                                                                                height=80,
                                                                            ),
                                                                            icon_size=45,
                                                                            icon_color=ft.colors.WHITE,
                                                                            style=ft.ButtonStyle(
                                                                                shape=ft.RoundedRectangleBorder(
                                                                                    6
                                                                                )
                                                                            ),
                                                                            offset=(0, 0.1),
                                                                            padding=0
                                                                        ),
                                                                        ft.Text(
                                                                            value="LEVE PARA CASA",
                                                                            size=16,
                                                                            color=ft.colors.WHITE,
                                                                            font_family='FuturaPTMedium'
                                                                        ),
                                                                    ],
                                                                )
                                                            ),
                                                            ft.Container(
                                                                content=ft.Column(
                                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                    controls=[
                                                                        ft.IconButton(
                                                                            content=ft.Image(
                                                                                src="/images/ccmtj_icon.png",
                                                                                fit=ft.ImageFit.CONTAIN,
                                                                                width=80,
                                                                                height=80,
                                                                            ),
                                                                            icon_size=50,
                                                                            icon_color=ft.colors.WHITE,
                                                                            style=ft.ButtonStyle(
                                                                                shape=ft.RoundedRectangleBorder(
                                                                                    6
                                                                                )
                                                                            ),
                                                                            offset=(0, 0.1),
                                                                            on_click=lambda e: e.page.go(
                                                                                "/ccmtj"
                                                                            ),
                                                                            padding=0
                                                                        ),
                                                                        ft.Text(
                                                                            value="CCM TJ AL",
                                                                            size=16,
                                                                            color=ft.colors.WHITE,
                                                                            font_family='FuturaPTMedium'
                                                                        ),
                                                                    ],
                                                                )
                                                            ),
                                                        ],
                                                        spacing=18,
                                                    ),
                                                ],
                                            )
                                        ),
                                    ],
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
                                        icon_color="#c8c4d4",
                                        on_click=lambda e: e.page.go("/aboutapp"),
                                    ),
                                    ft.Text(
                                        spans=[
                                            ft.TextSpan(
                                                text="SOBRE O APP",
                                                style=ft.TextStyle(
                                                    size=12, color="#c8c4d4"
                                                ),
                                                on_click=lambda e: e.page.go(
                                                    "/aboutapp"
                                                ),
                                            )
                                        ]
                                    ),
                                ],
                            ),
                        ],
                    )
                ),
                
            ],
        )
