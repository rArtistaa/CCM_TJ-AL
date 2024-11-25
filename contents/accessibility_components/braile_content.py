import flet as ft

text_content0 = 'Centro de Cultura e Memória do Tribunal de Justiça de Alagoas (CCMTJ/AL)'
text_content1 = '''
tem o prazer de anunciar uma importante iniciativa para tornar a experiência cultural e histórica ainda mais inclusiva: agora, os painéis de conteúdo histórico da justiça alagoana contam com acessibilidade em braille. Este avanço representa um compromisso com a acessibilidade e o respeito à diversidade, visando garantir que todos, independentemente de suas condições visuais, possam ter acesso às ricas histórias e informações que compõem o acervo do Centro. A inclusão do braille nos painéis permite que pessoas com deficiência visual explorem de forma autônoma as informações sobre a trajetória da Justiça em Alagoas, desde seus primeiros passos até as mudanças e marcos que moldaram a história do Judiciário no estado. Com esse recurso, a história e o legado do Tribunal de Justiça de Alagoas ficam ao alcance de um público ainda mais amplo, reforçando o compromisso da instituição em promover o acesso igualitário ao conhecimento e à memória cultural. Além de valorizar o patrimônio histórico, esta iniciativa está alinhada com os princípios de inclusão social e cidadania, fundamentais para a construção de uma sociedade mais justa e acolhedora. Convidamos todos a conhecerem o CCMTJ/AL e vivenciarem essa nova experiência de acessibilidade e inclusão, um marco que enriquece ainda mais o nosso compromisso com a justiça e com a sociedade alagoana.
'''

def braile_content():
    return [
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30,
            controls=[
                ft.IconButton(
                    content=ft.Image(
                        src='/images/braile_icon.png',
                        fit=ft.ImageFit.CONTAIN,
                        width=50,
                        height=50
                    ),
                    width=61,
                    height=61,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor='#7089C5'   
                    ),
                    padding=0,
                    disabled=True,
                    disabled_color='#7089C5'
                ),
                ft.Text(
                    value='BRAILLE',
                    style=ft.TextStyle(
                        size=18,
                        font_family='FuturaPTMedium'    
                    )    
                )           
            ]      
        ),
        ft.Column(
            width=338,
            height=900,
            spacing=0,
            controls=[
                ft.Text(
                    spans=[
                        ft.TextSpan(
                            text='O ',
                            style=ft.TextStyle(
                                font_family='FuturaPTLight',
                                size=17    
                            )    
                        ),
                        ft.TextSpan(
                            text=text_content0,
                            style=ft.TextStyle(
                                font_family='FuturaPTDemi',
                                size=17    
                            )    
                        ),
                        ft.TextSpan(
                            text=text_content1,
                            style=ft.TextStyle(
                                font_family='FuturaPTLight',
                                size=17    
                            )    
                        )    
                    ],
                    
                )
            ]    
        )
    ]
