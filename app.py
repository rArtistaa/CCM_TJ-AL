import flet as ft
from controllers.route_controller import RouteController
from exceptions import RouteNotFoundError


def main(page: ft.Page):
    page.scroll = 'auto'
    page.padding = 20

    route_controller = RouteController(page)

    route_controller.change_route('/login')
    

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir='assets')
