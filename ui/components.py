import flet as ft

class PianoKeyboard(ft.Container):
    def __init__(self, octaves=2):
        super().__init__()
        self.octaves = octaves
        self.content = self._build_keyboard()
        self.width = 800
        self.height = 150

    def _build_keyboard(self):
        white_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        black_notes = {'C#': 0, 'D#': 1, 'F#': 3, 'G#': 4, 'A#': 5}
        
        white_keys = ft.Row(
            controls=[
                ft.Container(
                    width=100,
                    height=150,
                    bgcolor=ft.colors.WHITE,
                    border=ft.border.all(1),
                    alignment=ft.alignment.bottom_center,
                    content=ft.Text(note, color=ft.colors.BLACK)
                ) for note in white_notes * self.octaves
            ],
            spacing=0
        )

        black_keys = ft.Row(
            controls=[
                ft.Container(
                    width=50,
                    height=100,
                    bgcolor=ft.colors.BLACK,
                    left=pos * 100 + 60,
                    alignment=ft.alignment.bottom_center,
                    content=ft.Text(note, color=ft.colors.WHITE)
                ) for note, pos in black_notes.items()
            ],
            spacing=0
        )

        return ft.Stack(
            controls=[
                white_keys,
                black_keys
            ]
        )

class ScaleControls(ft.Column):
    def __init__(self, generate_handler):
        super().__init__()
        self.tonic_dropdown = ft.Dropdown(label="Tônica")
        self.scale_type_dropdown = ft.Dropdown(label="Tipo de Escala")
        self.generate_button = ft.ElevatedButton(
            "Gerar Escala",
            on_click=generate_handler
        )
        self.controls = [
            self.tonic_dropdown,
            self.scale_type_dropdown,
            self.generate_button
        ]