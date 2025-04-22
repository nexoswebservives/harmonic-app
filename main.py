import flet as ft
from flet import Page, app
from services.config import AppConfig
from services.theory_service import MusicTheoryService

def main(page: Page):
    config = AppConfig()
    service = MusicTheoryService(config)

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    controls=[
                        ft.Text("🎶 Bem-vindo ao Harmonic App", size=28, weight=ft.FontWeight.BOLD),
                        ft.Text("Escolha uma funcionalidade:", size=16),
                        ft.ElevatedButton("📚 Estudo de Escalas", on_click=lambda _: page.go("/estudo_escalas")),
                        ft.ElevatedButton("🎹 Formação de Acordes", on_click=lambda _: page.go("/formacao_acordes")),
                        ft.ElevatedButton("🎼 Campo Harmônico", on_click=lambda _: page.go("/campo_harmonico"))
                    ]
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go(page.route or "/")

if __name__ == "__main__":
    import os
    ft.app(target=main, port=int(os.getenv("PORT", 8000)), view=ft.WEB_BROWSER)
