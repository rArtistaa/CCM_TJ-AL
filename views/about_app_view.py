import flet as ft


class AboutAppView:
    def __init__(self) -> None:
        self.about_text = '''  PROJETO EXPOSITIVO, PRODUÇÃO DE
CONTEÚDO E TECNOLOGIA
Estúdio Núcleo Zero
Coordenador de conteúdo, design e 
tecnologia: Werner Salles Bagetti 
Ilustrações e animações: Weber Salles Bagetti 
Design e tecnologia: Ulysses Lins 
Pesquisa e produção: Nina Magalhães 
Pesquisa, produção e textos: Rafhael Barbosa 
Controller: Tiago Leão 
Revisão: Nilton Resende 
Digitalização de acervos: Flávia Correia 
Fotos da Coleção Perseverança: Larissa Fontes

PROJETO MUSEOGRÁFICO 

Consultoria: Adriana Guimarães 
Desenho: Carla Cansanção 
Maquete: Fernando Pedroza'''

    
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
                                        bgcolor='#0E428E',
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
                                            bgcolor='#0E428E',
                                            icon_color=ft.colors.WHITE,
                                            icon_size=38,                            
                                            top=4,
                                            left=90,     
                                    ),
                                    ft.IconButton(
                                         icon=ft.icons.HOME_OUTLINED,
                                            bgcolor='#0E428E',
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
                            ft.Column(
                                height=380,
                                width=320,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                scroll=ft.ScrollMode.ADAPTIVE,
                                controls=[
                                    ft.Text(
                                        value=self.about_text,
                                        height=530,
                                        width=336,
                                        style=ft.TextStyle(
                                            size=17,
                                            weight='bold',  
                                        ),
                                        text_align=ft.TextAlign.CENTER
                                    )    
                                ]    
                            ),
                            ft.Container(height=10),
                            ft.Text(
                                value='© 2024 APP DESENVOLVIDO POR NÚCLEO ZERO',
                                size=15    
                            ),
                            ft.Text(
                                value='VERSÃO 0.1',
                                size=15 ,
                                weight=ft.FontWeight.W_100  
                            )
                        ]    
                    ) 
                ]    
            )
        )