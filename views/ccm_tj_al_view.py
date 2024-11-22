import flet as ft
from utils.navigation_bar import create_navigation_bar


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
        self.current_image_index = 0
        self.images_per_view = 8


    def expand_container(self, e):
        self.expanded = not self.expanded
        self.upper_container.height = 700 if self.expanded else 577
        self.text_content.height = 410 if self.expanded else 278
        self.read_more_text.offset = ft.Offset(0, 6 if self.expanded else -1)
        e.page.update()


    def scroll_left(self, e):
        if self.current_image_index > 1:
            self.current_image_index -= 2  
            self.update_photo_grid(e)
            e.page.update()
        

    def scroll_right(self, e):
        if self.current_image_index < len(self.photo_grid.controls) - self.images_per_view - 2:
            self.current_image_index += 2 
            self.update_photo_grid(e)
            e.page.update()


    def update_photo_grid(self, e):
        for i, img in enumerate(self.photo_grid.controls):
            img.visible = self.current_image_index <= i < self.current_image_index + self.images_per_view
            if img.visible:
                img.offset = ft.Offset(0, 0)  
                img.animate_offset = ft.Animation(300, "ease") 
            else:
                img.offset = ft.Offset(0, -10) 
                img.animate_offset = ft.Animation(300, "ease") 
        e.page.update()


    def build(self):
        self.text_content = ft.Text(
            value=self.text,
            height=250,
            width=378,
            size=16,
            text_align=ft.TextAlign.LEFT,
            animate_size=ft.Animation(400, 'ease'),
            top=200
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
            offset=ft.Offset(0, -1),
            animate_offset=ft.Animation(400, 'ease'),
            top=530    
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

        self.photo_grid = ft.Row(      
            controls=[
                *[
                    ft.Image(
                        src=f"https://picsum.photos/150/150?{i}",
                        fit=ft.ImageFit.COVER,
                        border_radius=ft.border_radius.all(2),
                        width=168,
                        height=168   
                    ) for i in range(16)
                ]
            ],
            scroll=ft.ScrollMode.ALWAYS,  
        )

        self.video_grid = ft.Row(
            controls=[
                ft.Image(
                    src=f"https://picsum.photos/150/150?{i}",
                    fit=ft.ImageFit.COVER,
                    border_radius=ft.border_radius.all(2)   
                ) for i in range(16)  
            ],
            scroll=ft.ScrollMode.ALWAYS,  
        )

        return ft.View(
            bgcolor='#071F49',
            scroll=ft.ScrollMode.AUTO,
            padding=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
            controls=[
                ft.Row(
                    alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Stack(
                            controls=[
                                self.upper_container,
                                *create_navigation_bar(
                                    on_back_click=lambda e: e.page.go('/home'),
                                    color='#B05198'    
                                ),    
                            ]    
                        )    
                    ]
                ),
                ft.Container(height=40),
                ft.Text(
                    value='FOTOS',
                    size=18
                ),
                ft.Container(height=10),
                ft.Container(
                    content=self.photo_grid,  
                    height=150,                
                    width=450,                 
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(
                            content=ft.Image(
                                src='/images/arrow_images.png',
                                fit=ft.ImageFit.CONTAIN,
                                width=60,
                                height=60,
                                scale=ft.Scale(scale_x=-1, scale_y=1)                        
                            ),
                            on_click=self.scroll_left                  
                        ),
                        ft.IconButton(
                            content=ft.Image(
                                src='/images/arrow_images.png',
                                fit=ft.ImageFit.CONTAIN,
                                width=60,
                                height=60,                      
                            ),
                            on_click=self.scroll_right    
                        )    
                    ]    
                ),
                ft.Text(
                value='VÍDEOS',
                size=18    
                ),
                ft.Container(height=10),
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    height=207,
                    width=340,
                    content=ft.IconButton(
                        icon=ft.icons.PLAY_ARROW_ROUNDED,
                        icon_size=30   
                    )    
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(
                            content=ft.Image(
                                src='/images/arrow_images.png',
                                fit=ft.ImageFit.CONTAIN,
                                width=60,
                                height=60,
                                scale=ft.Scale(scale_x=-1, scale_y=1)                        
                            ),               
                        ),
                        ft.IconButton(
                            content=ft.Image(
                                src='/images/arrow_images.png',
                                fit=ft.ImageFit.CONTAIN,
                                width=60,
                                height=60,                      
                            ),
                        )    
                    ]    
                ),
                ft.Container(height=20)
            ]    
        )
