import flet as ft


class ScheduleView:
    def __init__(self) -> None:
        pass


    def build(self):
        return ft.Container(
            expand=True,
            bgcolor='#071F49',
            padding=0,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        alignment=ft.CrossAxisAlignment.START,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        bgcolor='#69AABC',
                                        height=64,
                                        width=236,
                                        border_radius=ft.border_radius.only(bottom_right=66)
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.ARROW_BACK_IOS_ROUNDED,
                                            bgcolor='#071F49',
                                            icon_color='#E7EBE0',
                                            icon_size=22,
                                            height=41,
                                            width=41,
                                            top=11,
                                            left=26,
                                            alignment=ft.alignment.center_left,
                                            on_click=lambda e: e.page.go('/home')
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.QR_CODE_SCANNER_ROUNDED,
                                            bgcolor='#69AABC',
                                            icon_color=ft.colors.WHITE,
                                            icon_size=38,                            
                                            top=4,
                                            left=90,     
                                    ),
                                    ft.IconButton(
                                         icon=ft.icons.HOME_OUTLINED,
                                            bgcolor='#69AABC',
                                            icon_color=ft.colors.WHITE,
                                            icon_size=38,
                                            top=4,
                                            left=155,
                                            on_click=lambda e: e.page.go('/home')   
                                    )    
                                ]    
                            )    
                        ]
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
                                icon=ft.icons.CALENDAR_TODAY_OUTLINED,
                                text='   AGENDA',
                                bgcolor='#69AABC',
                                color=ft.colors.WHITE,
                                height=58,
                                width=223,
                                style=ft.ButtonStyle(
                                    icon_size=37,
                                    text_style=ft.TextStyle(
                                        size=18    
                                    )
                                )
                            )
                        ]    
                    )    
                ]    
            )    
        )
