class AppConfig:
    @property
    def sharp_notes(self):
        return ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    @property
    def flat_notes(self):
        return ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

    @property
    def formulas(self):
        return {
            "jónico": ["T", "2M", "3M", "4J", "5J", "6M", "7M"]
        }

    @property
    def chord_qualities(self):
        return {
            "jónico": ["M", "m", "m", "M", "M", "m", "dim"]
        }

    @property
    def seventh_qualities(self):
        return {
            "jónico": ["maj7", "m7", "m7", "maj7", "7", "m7", "m7b5"]
        }
