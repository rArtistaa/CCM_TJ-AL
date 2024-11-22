import flet as ft
import asyncio
from controllers.page_route_controller import PageRouteController


def main(page: ft.Page):
    page.scroll = 'auto'

    page.fonts = {
        'FuturaPTMedium': 'fonts/FuturaPTMedium.otf',
        'FuturaPTBold': 'fonts/FuturaPTBold.otf'    
    }
    

    route_controller = PageRouteController(page)
    page.on_route_change = route_controller.handle_route_change
    page.go('/schedule')

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir='assets')
