import flet as ft
from views.login_view import LoginView
from views.home_view import HomeView
from views.register_view import RegisterView
from exceptions import RouteNotFoundError


class RouteController:
    def __init__(self, page) -> None:
        self.page = page
        self.views = {
            '/login': LoginView(self),
            '/home': HomeView(self),
            '/register': RegisterView(self),
        }
    
    def change_route(self, route):
        ''' Alterna entre as views conforme a rota. '''
        view = self.views.get(route)

        if view:
            self.page.views.clear()
            self.page.views.append(view.build())
            self.page.update()
        else:
            raise RouteNotFoundError(f'Rota não encontrada: {route}')
