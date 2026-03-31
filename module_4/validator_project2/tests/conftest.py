import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from validators import EmailValidator

@pytest.fixture
def validator():
    return EmailValidator()