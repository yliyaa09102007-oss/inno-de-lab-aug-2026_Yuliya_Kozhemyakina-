#===================================
#--Безопасная обработка возвратов---
#===================================

from typing import Any

DEFAULT_RETURN_INDEX_BASE = 10.0

def calculate_overdue_fine(film_name: str, days_overdue: Any, fine_rate: Any) \
    -> tuple[float, float] | None:
    """
    This function calculates the total fine and return index for a given film.
    If there is an input mistake, the function will return this mistake.
    Args:
        film_name: name of the film
        days_overdue: days overdue
        fine_rate: fine rate
    Returns:
        -If successful, returns total_fine, return_index
        -If not, returns none and prints film_name and the name of the error
    """

    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days
        print(f"Фильм: {film_name} | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")
        return total_fine, return_index
    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для {film_name}:\n {e}")
        return None
    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для {film_name}:\n {e}")
        return None
    except ZeroDivisionError as e:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для {film_name}:\n {e}")
        return None
    except Exception as e:
        print(f"[ОШИБКА] Что-то пошло не так для {film_name}:\n {e}")
        return None
    finally:
        print("--- Проверка транзакции возврата завершена ---\n")

print("=== ПРОВЕРКА ВОЗВРАТОВ ===\n")

#running tests and calling the function
calculate_overdue_fine("Matrix", 5, 1.5)
calculate_overdue_fine("Inception", "пять", 2.0)
calculate_overdue_fine("Avatar", 0, 2.5)
calculate_overdue_fine("Inception", [3,], 3.0)
#one more from me
calculate_overdue_fine("Spider-Man: Brand New Day", 8, "три")