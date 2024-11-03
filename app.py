import flet as ft
from controllers.page_route_controller import PageRouteController


def main(page: ft.Page):
    page.scroll = 'auto'
    page.padding = 20

    route_controller = PageRouteController(page)
    page.on_route_change = route_controller.handle_route_change
    page.go('/login')

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir='assets')
