# Практические задания по pytest

Полная реализация всех трех практических заданий с использованием pytest, фикстур и параметризации.

## Структура проекта

```
validator_project/
├── src/
│   └── validators.py           # Все классы и функции валидаторов
├── tests/
│   ├── conftest.py             # Фикстуры для всех тестов
│   └── test_validators.py      # Все тесты для всех трех задач
├── pytest.ini                  # Конфигурация pytest с маркерами
└── README.md
```

## Задание 1: Фикстуры для валидатора ✅

### Реализованная функциональность:
- ✅ Класс `EmailValidator` с методом `is_valid(email)`
- ✅ Фикстура `email_validator` в `tests/conftest.py`
- ✅ 9 тестов для разных сценариев валидации email:
  - Валидные: простой email, с цифрами, с точками, с плюсом
  - Невалидные: без @, пустой, None, без домена, без расширения

### Запуск:
```bash
pytest tests/test_validators.py::TestEmailValidator -v
```

---

## Задание 2: Параметризация ✅

### Реализованная функциональность:
- ✅ Функция `celsius_to_fahrenheit(celsius)`
- ✅ Функция `fahrenheit_to_celsius(fahrenheit)` (бонус)
- ✅ Параметризованные тесты с использованием `@pytest.mark.parametrize`
- ✅ Использование `ids` для названия тестов:
  - freezing, boiling, equal_point, absolute_zero
  - room_temperature, body_temperature, very_hot
  - Плюс обратные конвертации
- ✅ 15 параметризованных тестов + 1 интеграционный тест

### Запуск:
```bash
pytest tests/test_validators.py::TestTemperatureConversion -v
```

---

## Задание 3: Комбинирование всего ✅

### Реализованная функциональность:

#### Класс `UserValidator` с методами:
1. **`is_valid_username(username)`**
   - Требования: 3-20 символов, буквы/цифры/подчеркивание, начинается с буквы
   - 11 параметризованных тестов с ids

2. **`is_valid_password(password)`**
   - Требования: ≥8 символов, заглавные, строчные, цифры, спецсимволы (!@#$%^&*)
   - 11 параметризованных тестов с ids
   - 1 медленный тест (@pytest.mark.slow)

3. **`is_valid_age(age)`**
   - Требования: целое число (не bool, не float), 18-120 лет
   - 10 параметризованных тестов с ids
   - 2 дополнительных теста для типов данных

#### Фикстура:
- ✅ `user_validator` в `tests/conftest.py`

#### Маркеры:
- ✅ `@pytest.mark.validation` - применен ко всем тестам валидации (38 тестов)
- ✅ `@pytest.mark.slow` - применен к медленным проверкам (2 теста)

#### Интеграционные тесты:
- ✅ Тест полностью валидного пользователя
- ✅ Тест частично невалидного пользователя
- ✅ Тест граничных случаев

### Запуск тестов:

```bash
# Запустить только validation тесты (38 из 62)
pytest tests/ -v -m validation

# Запустить все, кроме slow тестов (60 из 62)
pytest tests/ -m "not slow"

# Запустить только slow тесты (2 из 62)
pytest tests/ -m slow

# Запустить все тесты
pytest tests/ -v
```

---

## Статистика тестов

| Компонент | Тесты | Маркеры |
|-----------|-------|---------|
| **EmailValidator** | 9 | - |
| **TemperatureConversion** | 15 | - |
| **UserValidator:Username** | 11 | @validation |
| **UserValidator:Password** | 12 | @validation, @slow (1) |
| **UserValidator:Age** | 12 | @validation |
| **Интеграционные тесты** | 3 | @validation, @slow (1) |
| **ИТОГО** | **62** | **38 @validation, 2 @slow** |

---

## Требования

- Python 3.7+
- pytest 9.0+

## Установка зависимостей

```bash
pip install pytest
```

## Запуск всех тестов

```bash
pytest tests/ -v
```
