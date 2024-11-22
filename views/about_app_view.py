import flet as ft
from utils.navigation_bar import create_navigation_bar


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
        return ft.View(
            bgcolor='#071F49',
            scroll=ft.ScrollMode.AUTO,
            padding=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                *create_navigation_bar(
                    on_back_click=lambda e: e.page.go('/home'),
                    color='#0E428E'    
                ),
                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=40,
                    controls=[
                        ft.Image(
                            src='/images/appccmtj_logo.png',
                            fit=ft.ImageFit.CONTAIN,
                            width=104,
                            height=104    
                        ),
                        ft.Text(
                            value='PATROCÍNIO',
                            style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD,
                                size=17,
                                color=ft.colors.WHITE    
                            )
                        )    
                    ]    
                )  
            ]    
        )