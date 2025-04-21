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

        elif page.route == "/formacao_acordes":
            dropdown = ft.Dropdown(label="Selecione o Tom", options=[ft.dropdown.Option(n) for n in config.sharp_notes + config.flat_notes])
            output = ft.Column()

            def gerar_acordes(e):
                nota = dropdown.value
                if nota:
                    acordes = service.gerar_formacao_acordes(nota)
                    output.controls.clear()
                    for nome, notas in acordes.items():
                        output.controls.append(ft.Text(f"{nome}: {', '.join(notas)}"))
                page.update()

            page.views.append(
                ft.View(
                    "/formacao_acordes",
                    controls=[
                        ft.Text("🎹 Formação de Acordes", size=24, weight=ft.FontWeight.BOLD),
                        dropdown,
                        ft.ElevatedButton("Gerar Acordes", on_click=gerar_acordes),
                        ft.ElevatedButton("🔙 Voltar", on_click=lambda _: page.go("/")),
                        output
                    ]
                )
            )

        elif page.route == "/campo_harmonico":
            dropdown = ft.Dropdown(label="Tônica", options=[ft.dropdown.Option(n) for n in config.sharp_notes + config.flat_notes])
            output = ft.Column()

            def gerar_campo(e):
                nota = dropdown.value
                if nota:
                    campo = service.gerar_campo_harmonico(nota)
                    output.controls.clear()
                    output.controls.append(ft.Text(f"Escala: {', '.join(campo['escala'])}", weight=ft.FontWeight.BOLD))
                    output.controls.append(ft.Text(f"Acordes: {', '.join(campo['acordes'])}"))
                    output.controls.append(ft.Text(f"Acordes com 7ª: {', '.join(campo['acordes7'])}"))
                page.update()

            page.views.append(
                ft.View(
                    "/campo_harmonico",
                    controls=[
                        ft.Text("🎼 Campo Harmônico", size=24, weight=ft.FontWeight.BOLD),
                        dropdown,
                        ft.ElevatedButton("Gerar Campo Harmônico", on_click=gerar_campo),
                        ft.ElevatedButton("🔙 Voltar", on_click=lambda _: page.go("/")),
                        output
                    ]
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go(page.route or "/")

if __name__ == "__main__":

if __name__ == "__main__":
    import os
    ft.app(target=main, port=int(os.getenv("PORT", 8000)), view=ft.WEB_BROWSER)
