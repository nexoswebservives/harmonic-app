from services.theory_service import MusicTheoryService
import flet as ft

class MainView:
    def __init__(self, page: ft.Page, theory_service: MusicTheoryService, config):
        self.page = page
        self.theory_service = theory_service
        self.config = config  # ✅ Corrigido
        self.output_text = ft.Text()
        self.tonic_dropdown = ft.Dropdown()
        self.scale_type_dropdown = ft.Dropdown()
        self._init_ui()

    def _init_ui(self):
        self.page.title = f"Harmonic APP - {self.config.VERSION}"
        self.page.window_min_width = 800
        self.page.window_min_height = 600
        self._setup_main_content()

    def _setup_main_content(self):
        self.tonic_dropdown = ft.Dropdown(
            options=[ft.dropdown.Option(note) for note in self.config.sharp_notes],
            label="Tônica"
        )

        self.scale_type_dropdown = ft.Dropdown(
            options=[ft.dropdown.Option(mode) for mode in self.config.patterns],
            label="Tipo de Escala"
        )

        self.page.add(
            ft.Column(
                controls=[
                    ft.Text("Gerador de Escalas Musicais", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    self.tonic_dropdown,
                    self.scale_type_dropdown,
                    ft.ElevatedButton("Gerar Escala", on_click=self._generate_scale),
                    self.output_text
                ],
                scroll=ft.ScrollMode.ADAPTIVE
            )
        )

    def _generate_scale(self, e):
        try:
            if not self.tonic_dropdown.value or not self.scale_type_dropdown.value:
                raise ValueError("Selecione a tônica e o tipo de escala!")

            scale_info = self.theory_service.generate_full_scale_info(
                self.tonic_dropdown.value,
                self.scale_type_dropdown.value
            )

            self.output_text.value = (
                f"Escala Gerada: {', '.join(scale_info['scale'])}\n"
                f"Acordes: {', '.join(scale_info['chords'])}"
            )
            self.page.update()

        except ValueError as ve:
            self.output_text.value = f"Erro: {str(ve)}"
            self.page.update()
        except Exception as ex:
            self.output_text.value = "Erro interno no processamento"
            self.page.update()

    def get_view(self):
        return ft.View(
            route="/scales",
            controls=[
                ft.Text("Gerador de Escalas Musicais", size=24),
                self.tonic_dropdown,
                self.scale_type_dropdown,
                ft.ElevatedButton("Gerar Escala", on_click=self._generate_scale),
                self.output_text
            ]
        )

    @staticmethod
    def landing_view(page):
        return ft.View(
            route="/",
            controls=[
                ft.Text("🎶 Bem-vindo ao Harmônico App!", size=28, weight=ft.FontWeight.BOLD),
                ft.Text("Escolha uma funcionalidade:", size=16),
                ft.Divider(),

                ft.ElevatedButton("🎼 Tons Maiores e Menores", on_click=lambda _: page.go("/scales")),
                ft.ElevatedButton("♯ e ♭ Tons Relativos", on_click=lambda _: page.go("/relatives")),
                ft.ElevatedButton("🎹 Escalas com Tríades, Pentatônicas e Blues", on_click=lambda _: page.go("/types")),
                ft.ElevatedButton("🧠 Análise de Tonalidades Musicais", on_click=lambda _: page.go("/analysis")),
                ft.ElevatedButton("🎵 Campos Harmônicos", on_click=lambda _: page.go("/harmonics")),

                ft.Divider(),
                ft.Text("Toque uma opção para começar!", italic=True),
            ],
            vertical_alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )

