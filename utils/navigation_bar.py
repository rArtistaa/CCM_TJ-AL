import flet as ft


def create_navigation_bar(on_back_click=None, color: str=None):
    '''''
    Cria a barra de navegação com 3 botões fixos:
    - Voltar
    - QR Code Scanner
    - Home
    
    :param on_back_click: Função chamada ao clicar no ícone de voltar
    :param on_home_click: Função chamada ao clicar no ícone de home
    :param on_qr_code_click: Função chamada ao clicar no ícone de QR code
    :return: Lista de controles para a barra de navegação.
    '''

    return [
        ft.Row(
            alignment=ft.CrossAxisAlignment.START,
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Stack(
                    controls=[
                        ft.Container(
                            bgcolor=color,
                            height=64,
                            width=236,
                            border_radius=ft.border_radius.only(bottom_right=66)    
                        ),
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK_IOS_ROUNDED,
                            bgcolor="#071F49",
                            icon_color="#E7EBE0",
                            icon_size=22,
                            height=41,
                            width=41,
                            top=11,
                            left=26,
                            alignment=ft.alignment.center_left,
                            on_click=on_back_click 
                        ),
                        ft.IconButton(
                            icon=ft.icons.QR_CODE_SCANNER_ROUNDED,
                            bgcolor=color,
                            icon_color=ft.colors.WHITE,
                            icon_size=38,
                            top=4,
                            left=90,
                            on_click=lambda e: e.page.go('/qrcode')
                        ),
                        ft.IconButton(
                            icon=ft.icons.HOME_OUTLINED,
                            bgcolor=color,
                            icon_color=ft.colors.WHITE,
                            icon_size=38,
                            top=4,
                            left=155,
                            on_click=lambda e: e.page.go('/home')
                        )  
                    ]    
                ) 
            ]
        )         
    ]
