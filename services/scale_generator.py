class ScaleGenerator:
    def __init__(self, config):
        self.config = config

    def generate_mode_scale(self, tonic, mode_type):
        formulas = {
            "jónico": [2, 2, 1, 2, 2, 2, 1]
        }

        steps = formulas.get(mode_type.lower())
        if not steps:
            raise ValueError(f"Modo inválido: {mode_type}")

        notes = self.config.flat_notes if "b" in tonic else self.config.sharp_notes
        index = notes.index(tonic)
        scale = [tonic]
        for step in steps:
            index = (index + step) % len(notes)
            scale.append(notes[index])
        return scale
