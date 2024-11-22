import flet as ft
from utils.navigation_bar import create_navigation_bar


class ScheduleView:
    def __init__(self) -> None:
        self.selected_month = ft.Ref[ft.Text]()
        self.dropdown_ref = ft.Ref[ft.Dropdown]()  
        self.months = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]


    def on_select(self, e):
        selected_month = e.control.value
        self.selected_month.current.value = f'Mês selecionado: {selected_month}'
        self.dropdown_ref.current.label = ''
        e.page.update()


    def build(self):
        dropdown = ft.Dropdown(
            ref=self.dropdown_ref,
            label="Selecione um mês", 
            options=[
                ft.dropdown.Option(month) for month in self.months
            ],
            on_change=self.on_select,
            width=274,
            bgcolor=ft.colors.WHITE,
            max_menu_height=212,
            text_style=ft.TextStyle(
                color='#071F49',
                font_family='FuturaPTBold',
                size=20 
            ),
            border_color='#707070',
            label_style=ft.TextStyle(
                color='#071F49',
                font_family='FuturaPTBold',
                size=20    
            )
        )

        return ft.View(
            bgcolor="#071F49",
            padding=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                *create_navigation_bar(
                    on_back_click=lambda e: e.page.go('/home'),
                    color='#69AABC'
                ),
                ft.Container(),
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
                        ft.ElevatedButton(
                            icon=ft.icons.CALENDAR_TODAY_OUTLINED,
                            text='   AGENDA',
                            bgcolor="#69AABC",
                            color=ft.colors.WHITE,
                            height=58,
                            width=223,
                            style=ft.ButtonStyle(
                                icon_size=37,
                                text_style=ft.TextStyle(size=18)
                            )
                        ),
                        dropdown,
                        ft.Text(ref=self.selected_month, color='#071F49'),
                    ]
                )
            ]
        )
