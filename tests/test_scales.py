import pytest
from services.config import AppConfig
from services.theory_service import MusicTheoryService

@pytest.fixture
def theory_service():
    config = AppConfig()
    return MusicTheoryService(config)

def test_generate_jonic_scale(theory_service):
    result = theory_service.generate_full_scale_info("C", "jónico")
    assert result["scale"] == ["C", "D", "E", "F", "G", "A", "B"]
    assert "Cmaj7" in result["sevenths"][0]
    assert "C E G" in result["triads"][0]
