import flet as ft
from views.login_view import LoginView
from views.home_view import HomeView
from views.register_view import RegisterView
from views.about_app_view import AboutAppView
from utils.exceptions import RouteNotFoundError


class PageRouteController:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.routes = {
            '/login': LoginView,
            '/register': RegisterView,
            '/home': HomeView,
            '/aboutapp': AboutAppView ,  
        }
    
    def handle_route_change(self, route_event):
        route = route_event.route
        self.page.views.clear()

        if route in self.routes:
            view_class = self.routes[route]
            view_instance = view_class()
            self.page.views.append(view_instance.build())
        else:
            raise RouteNotFoundError(f'Rota não encontrada: {route}')
        
        self.page.update()
    