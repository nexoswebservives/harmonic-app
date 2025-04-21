from .scale_generator import ScaleGenerator
from .chord_generator import ChordGenerator

class MusicTheoryService:
    def __init__(self, config):
        self.scale_generator = ScaleGenerator(config)
        self.chord_generator = ChordGenerator(config)
        self.config = config

    def generate_full_scale_info(self, tonic: str, mode_type: str) -> dict:
        scale = self.scale_generator.generate_mode_scale(tonic, mode_type)
        return {
            "scale": scale,
            "formula": self.config.formulas.get(mode_type, []),
            "chords": self.chord_generator.get_chords_from_scale(scale, mode_type),
            "sevenths": self.chord_generator.get_7th_chords(scale, mode_type),
        }

    def gerar_formacao_acordes(self, tonic):
        notas = self.config.flat_notes if "b" in tonic else self.config.sharp_notes
        idx = notas.index(tonic)
        def intervalo(i): return notas[(idx + i) % 12]

        return {
            f"{tonic} Maior": [intervalo(0), intervalo(4), intervalo(7)],
            f"{tonic} Menor": [intervalo(0), intervalo(3), intervalo(7)],
            f"{tonic} Diminuto": [intervalo(0), intervalo(3), intervalo(6)],
        }

    def gerar_campo_harmonico(self, tonic):
        escala = self.scale_generator.generate_mode_scale(tonic, "jónico")
        acordes = self.chord_generator.get_chords_from_scale(escala, "jónico")
        acordes7 = self.chord_generator.get_7th_chords(escala, "jónico")
        return {"escala": escala, "acordes": acordes, "acordes7": acordes7}
