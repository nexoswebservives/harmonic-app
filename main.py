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
                        ft.Text("🎶 Bem-vindo ao Harmonic App!", size=28, weight=ft.FontWeight.BOLD),
                        ft.Text("Escolha uma funcionalidade:", size=16),
                        ft.ElevatedButton("📚 Estudo de Escalas", on_click=lambda _: page.go("/estudo")),
                        ft.ElevatedButton("🎹 Formação de Acordes", on_click=lambda _: page.go("/acordes")),
                        ft.ElevatedButton("🎼 Campo Harmônico", on_click=lambda _: page.go("/campo"))
                    ]
                )
            )

        elif page.route == "/estudo":
            dropdown = ft.Dropdown(label="Tônica", options=[ft.dropdown.Option(n) for n in config.sharp_notes + config.flat_notes])
            result_column = ft.Column()

            def gerar_estudo(e):
                result_column.controls.clear()
                nota = dropdown.value
                if nota:
                    for modo in config.formulas.keys():
                        try:
                            info = service.generate_full_scale_info(nota, modo)
                            result_column.controls.append(ft.Text(f"🎼 Modo {modo.title()} - Escala: {', '.join(info['scale'])}", weight=ft.FontWeight.BOLD))
                            result_column.controls.append(ft.Text(f"Acordes: {', '.join(info['chords'])}"))
                            result_column.controls.append(ft.Text(f"Acordes com 7ª: {', '.join(info['sevenths'])}"))
                            result_column.controls.append(ft.Divider())
                        except Exception as err:
                            result_column.controls.append(ft.Text(f"Erro no modo {modo}: {err}", color=ft.colors.RED))
                page.update()

            page.views.append(
                ft.View("/estudo", controls=[
                    ft.Text("📚 Estudo de Escalas", size=24, weight=ft.FontWeight.BOLD),
                    dropdown,
                    ft.ElevatedButton("Gerar Modos", on_click=gerar_estudo),
                    ft.ElevatedButton("🔙 Voltar", on_click=lambda _: page.go("/")),
                    result_column
                ])
            )

        elif page.route == "/acordes":
            dropdown = ft.Dropdown(label="Tônica", options=[ft.dropdown.Option(n) for n in config.sharp_notes + config.flat_notes])
            acordes_result = ft.Column()

            def gerar_acordes(e):
                acordes_result.controls.clear()
                nota = dropdown.value
                if nota:
                    formacao = service.gerar_formacao_acordes(nota)
                    for nome, notas in formacao.items():
                        acordes_result.controls.append(ft.Text(f"{nome}: {', '.join(notas)}"))
                page.update()

            page.views.append(
                ft.View("/acordes", controls=[
                    ft.Text("🎹 Formação de Acordes", size=24, weight=ft.FontWeight.BOLD),
                    dropdown,
                    ft.ElevatedButton("Gerar Formação", on_click=gerar_acordes),
                    ft.ElevatedButton("🔙 Voltar", on_click=lambda _: page.go("/")),
                    acordes_result
                ])
            )

        elif page.route == "/campo":
            dropdown = ft.Dropdown(label="Tônica", options=[ft.dropdown.Option(n) for n in config.sharp_notes + config.flat_notes])
            campo_result = ft.Column()

            def gerar_campo(e):
                campo_result.controls.clear()
                nota = dropdown.value
                if nota:
                    dados = service.gerar_campo_harmonico(nota)
                    campo_result.controls.append(ft.Text(f"Escala: {', '.join(dados['escala'])}", weight=ft.FontWeight.BOLD))
                    campo_result.controls.append(ft.Text(f"Acordes: {', '.join(dados['acordes'])}"))
                    campo_result.controls.append(ft.Text(f"Acordes com 7ª: {', '.join(dados['acordes7'])}"))
                page.update()

            page.views.append(
                ft.View("/campo", controls=[
                    ft.Text("🎼 Campo Harmônico", size=24, weight=ft.FontWeight.BOLD),
                    dropdown,
                    ft.ElevatedButton("Gerar Campo", on_click=gerar_campo),
                    ft.ElevatedButton("🔙 Voltar", on_click=lambda _: page.go("/")),
                    campo_result
                ])
            )

        page.update()

    page.on_route_change = route_change
    page.go(page.route or "/")

if __name__ == "__main__":
    import os
    ft.app(target=main, port=int(os.getenv("PORT", 8000)), view=ft.WEB_BROWSER)
