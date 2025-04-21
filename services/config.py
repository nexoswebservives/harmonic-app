
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
            "jónico": ["T", "2M", "3M", "4J", "5J", "6M", "7M"],
            "dórico": ["T", "2M", "3m", "4J", "5J", "6M", "7m"],
            "frígio": ["T", "2m", "3m", "4J", "5J", "6m", "7m"],
            "lídio": ["T", "2M", "3M", "4A", "5J", "6M", "7M"],
            "mixolídio": ["T", "2M", "3M", "4J", "5J", "6M", "7m"],
            "eólio": ["T", "2M", "3m", "4J", "5J", "6m", "7m"],
            "lócrio": ["T", "2m", "3m", "4J", "5d", "6m", "7m"]
        }

    @property
    def chord_qualities(self):
        return {
            "jónico": ["M", "m", "m", "M", "M", "m", "dim"],
            "dórico": ["m", "m", "M", "M", "m", "dim", "M"],
            "frígio": ["m", "M", "M", "m", "dim", "M", "M"],
            "lídio": ["M", "M", "m", "dim", "M", "m", "m"],
            "mixolídio": ["M", "m", "dim", "M", "m", "m", "M"],
            "eólio": ["m", "dim", "M", "m", "m", "M", "M"],
            "lócrio": ["dim", "M", "m", "m", "M", "M", "m"]
        }

    @property
    def seventh_qualities(self):
        return {
            "jónico": ["maj7", "m7", "m7", "maj7", "7", "m7", "m7b5"],
            "dórico": ["m7", "m7", "maj7", "7", "m7", "m7b5", "maj7"],
            "frígio": ["m7", "maj7", "7", "m7", "m7b5", "maj7", "m7"],
            "lídio": ["maj7", "7", "m7", "m7b5", "maj7", "m7", "m7"],
            "mixolídio": ["7", "m7", "m7b5", "maj7", "m7", "m7", "maj7"],
            "eólio": ["m7", "m7b5", "maj7", "m7", "m7", "maj7", "7"],
            "lócrio": ["m7b5", "maj7", "m7", "m7", "maj7", "7", "m7"]
        }
