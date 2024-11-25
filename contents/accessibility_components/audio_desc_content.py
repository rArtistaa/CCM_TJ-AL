import flet as ft


def aud_desc_content():
    return [
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30,
            controls=[
                ft.IconButton(
                    content=ft.Image(
                        src='/images/ad_icon.png',
                        fit=ft.ImageFit.CONTAIN,

                    ),
                    width=60,
                    height=60,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        bgcolor='#7089C5'   
                    ),
                    padding=0,
                    disabled=True,
                    disabled_color='#7089C5'
                ),
                ft.Text(
                    value='AUDIODESCRIÇÃO',
                    style=ft.TextStyle(
                        size=18,
                        font_family='FuturaPTMedium'    
                    )    
                )           
            ]      
        ),
        ft.Container(height=10),
        ft.Container(
            bgcolor='#041428',
            width=394,
            height=41,
            border_radius=ft.border_radius.all(40),
            content=ft.Text(
                value='         Título do audio',
                size=18,
                font_family='FuturaPTBook',
                text_align=ft.TextAlign.END,
            ),
            alignment=ft.alignment.center_left
        ),
        ft.Container(
            bgcolor='#041428',
            width=490,
            height=41,
            content=ft.Row(
                controls=[
                    ft.IconButton(
                    icon=ft.icons.PLAY_ARROW_ROUNDED,
                    icon_size=40,
                    padding=0,
                    icon_color='#7089C5' 
                    ),
                    ft.Slider(
                        width=370,
                        inactive_color='#E7EBE0',
                        active_color='#7089C5',
                        max=10,
                        min=0,
                        value=2
                    )       
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            )
        ) ,
        ft.Column(
            spacing=0,
            controls=[
                ft.Text(
                    value='Interpretação: Nome Aqui',
                    size=16,
                    font_family='FuturaPTBook'
                ),
                ft.Text(
                    value='Texto: Nome Aqui',
                    size=16,
                    font_family='FuturaPTBook'
                ),
                ft.Text(
                    value='Trilha: Nome Aqui',
                    size=16,
                    font_family='FuturaPTBook'
                ),
            ],
            offset=(-0.55, 0)
        ),
        ft.Container(height=16),
        ft.Container(
            bgcolor='#041428',
            width=394,
            height=41,
            border_radius=ft.border_radius.all(40),
            content=ft.Text(
                value='         Título do audio',
                size=18,
                font_family='FuturaPTBook',
                text_align=ft.TextAlign.END,
            ),
            alignment=ft.alignment.center_left
        ),
        ft.Container(
            bgcolor='#041428',
            width=490,
            height=41,
            content=ft.Row(
                controls=[
                    ft.IconButton(
                    icon=ft.icons.PLAY_ARROW_ROUNDED,
                    icon_size=40,
                    padding=0,
                    icon_color='#7089C5' 
                    ),
                    ft.Slider(
                        width=370,
                        inactive_color='#E7EBE0',
                        active_color='#7089C5',
                        max=10,
                        min=0,
                        value=2
                    )       
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            )
        ) ,
        ft.Column(
            spacing=0,
            controls=[
                ft.Text(
                    value='Interpretação: Nome Aqui',
                    size=16,
                    font_family='FuturaPTBook'
                ),
                ft.Text(
                    value='Texto: Nome Aqui',
                    size=16,
                    font_family='FuturaPTBook'
                ),
                ft.Text(
                    value='Trilha: Nome Aqui',
                    size=16,
                    font_family='FuturaPTBook'
                ),
            ],
            offset=(-0.55, 0)
        ),
        ft.Container(height=40)
    ]
