import flet as ft


def videos_content():
    return [
        ft.ElevatedButton(
            content=ft.Row(
                controls=[
                    ft.Image(
                        src='/images/video_icon.png',
                        fit=ft.ImageFit.CONTAIN,
                        width=36,  
                        height=36,
                        offset=(0, 0)
                    ),
                    ft.Text(
                        "VÍDEOS",
                        style=ft.TextStyle(
                            size=14,
                            color=ft.colors.WHITE,
                            font_family='FuturaPTMedium',
                            
                        ),
                        offset=(0.34, 0)  
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                        
            ),
            bgcolor='#7089C5',
            width=157,
            height=57
        ),
        ft.Column(
            controls=[
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    width=307,
                    height=163,
                    content=ft.IconButton(
                        bgcolor=ft.colors.WHITE,
                        icon=ft.icons.PLAY_ARROW,
                        icon_color='#071F49',
                        icon_size=70,                          
                    )  
                ),
                ft.Text(
                    value='A Mulher no judiciário Alagoano',
                    font_family='FuturaPTDemi',
                    size=17,
                    offset=(0, 0.4)   
                )    
            ],
            offset=(0, 0.1)   
        ),
        ft.Column(
            controls=[
                ft.Container(
                    bgcolor=ft.colors.WHITE,
                    width=307,
                    height=163,
                    content=ft.IconButton(
                        bgcolor=ft.colors.WHITE,
                        icon=ft.icons.PLAY_ARROW,
                        icon_color='#071F49',
                        icon_size=70   
                    )   
                ),
                ft.Text(
                    value=' O Impeachment de Muniz Falcão 1957 - Alagoas',
                    font_family='FuturaPTDemi',
                    size=17,
                    width=307,
                    offset=(0, 0.4)   
                )    
            ],
            offset=(0, 0.24)   
        ),
        ft.Container(height=80)    
    ]
