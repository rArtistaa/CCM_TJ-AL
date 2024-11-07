import flet as ft


class CCMTJALView:
    def __init__(self) -> None:
        self.text = '''Com sabedoria, o escritor argentino Jorge Luis
Borges, refletindo sobre o homem e o tempo,
afirma que “tudo nos diz adeus, tudo nos deixa”.
Há, no entanto, segundo ele, algo que se queda,
algo que permanece, algo que, de tão relevante,
não pode e não deve ser esquecido. São as
nossas memórias. Acontecimentos extraordinários
que precisam ficar registrados. Um presente do
tempo, o modo pelo qual ele, esse tirano incontido,
se faz generoso conosco: compensando a
efemeridade da vida, nos dá a oportunidade de
sermos importantes. E essa importância depende,
essencialmente, da capacidade que tenhamos,
enquanto povo, de aprender e de ensinar às
gerações seguintes, através dos nossos erros,
como a escravidão, e acertos, como o Quilombo
dos Palmares, onde a alegria e o contentamento
misturam-se a dores e horrores, compondo o
enredo da nossa história. Somente assim,
aprendendo e ensinando, as pegadas deixadas
pelo caminho não se apagarão e terão algum
sentido. Tudo o mais é caminhar sem direção.
Tudo o mais terá sido inútil. Mas, ainda bem
que não somos inúteis. Este Centro Cultural
e de Memória do Poder Judiciário de Alagoas
pretende mostrar um pouco isso. Aqui, guardamos
algumas pegadas. Elas nos convidam a olhar
criticamente sobre o que fizemos. Que esse
olhar nos faça lembrar o quanto de humano,
ainda, há em nós.'''

        self.expanded = False

    def expand_container(self, e):
        self.expanded = not self.expanded
        self.upper_container.height = 700 if self.expanded else 577
        self.text_content.height = 410 if self.expanded else 278
        self.read_more_text.offset = ft.Offset(0, 6 if self.expanded else -1)
        e.page.update()


    def build(self):
        self.text_content = ft.Text(
            value=self.text,
            height=278,
            width=378,
            size=16,
            text_align=ft.TextAlign.LEFT,
            top=200,
            animate_size=ft.Animation(400, 'ease')
        )

        self.image = ft.Image(
            src='/images/appccmtj_image2.jpg',
            height=104,
            width=104,
            fit=ft.ImageFit.CONTAIN,
            top=70    
        )

        self.read_more_text = ft.Text(
            spans=[
                ft.TextSpan(
                    text='LER MAIS',
                    style=ft.TextStyle(
                        color='#E5DFAE',
                        size=15,
                        decoration=ft.TextDecoration.UNDERLINE,
                        weight='bold'    
                    ),
                    on_click=self.expand_container    
                )    
            ],
            top=520,
            offset=ft.Offset(0, -1),
            animate_offset=ft.Animation(400, 'ease')    
        )

        self.upper_container = ft.Container(
            bgcolor='#051935',
            height=577,
            width=450,
            animate=ft.Animation(400, 'ease'),
            content=ft.Stack(
                    alignment=ft.alignment.center,
                    controls=[
                        self.image,
                        self.text_content,
                        self.read_more_text
                    ]    
                ),
                border_radius=ft.border_radius.only(bottom_right=80, bottom_left=80)
            )
        
        return ft.Container(
            expand=True,
            bgcolor='#071F49',
            padding=0,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
                controls=[
                    ft.Row(
                        alignment=ft.CrossAxisAlignment.START,
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Stack(
                                controls=[
                                    self.upper_container,
                                    ft.Container(
                                        bgcolor='#B05198',
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
                                            bgcolor='#B05198',
                                            icon_color=ft.colors.WHITE,
                                            icon_size=38,                            
                                            top=4,
                                            left=90,     
                                    ),
                                    ft.IconButton(
                                         icon=ft.icons.HOME_OUTLINED,
                                            bgcolor='#B05198',
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
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Container(height=20),
                            ft.Text(
                                value='FOTOS',
                                size=18
                            ),
                            ft.GridView()    
                        ]    
                    )
                ]    
            )    
        )
