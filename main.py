import flet as ft
import os

def main(page: ft.Page):
    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View("/", controls=[
                    ft.Text("✅ Projeto Flet Web no Render funcionando perfeitamente!", size=24)
                ])
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route or "/")

if __name__ == "__main__":
    ft.app(target=main, port=int(os.getenv("PORT", 8000)), view=ft.WEB_BROWSER)
