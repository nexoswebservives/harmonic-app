
class ChordGenerator:
    def __init__(self, config):
        self.config = config

    def get_chords_from_scale(self, scale, mode_type):
        qualities = self.config.chord_qualities.get(mode_type.lower(), [])
        return [self._format_chord(n, q) for n, q in zip(scale, qualities)]

    def get_7th_chords(self, scale, mode_type):
        qualities = self.config.seventh_qualities.get(mode_type.lower(), [])
        return [self._format_7th_chord(n, q) for n, q in zip(scale, qualities)]

    def get_triads(self, scale):
        return [f"{scale[i]} {scale[(i+2)%7]} {scale[(i+4)%7]}" for i in range(len(scale))]

    def _format_chord(self, note, quality):
        return f"{note}m" if quality == "m" else f"{note}°" if quality == "dim" else note

    def _format_7th_chord(self, note, quality):
        return f"{note}m7♭5" if quality == "m7b5" else f"{note}{quality}"
