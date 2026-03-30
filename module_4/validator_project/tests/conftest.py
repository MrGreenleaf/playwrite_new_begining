import pytest
import sys
from pathlib import Path

# Добавляем src директорию в sys.path чтобы импортировать validators
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from validators import EmailValidator, UserValidator


@pytest.fixture
def email_validator():
    """Фикстура для EmailValidator - используется в Task 1"""
    return EmailValidator()


@pytest.fixture
def user_validator():
    """Фикстура для UserValidator - используется в Task 3"""
    return UserValidator()
