#=============================================
#---Мониторинг производительности аналитики---
#=============================================

import time
from typing import Callable, Any


PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


def performance_logger(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        This function is a wrapper for 'get_sorted_report'
        It calculates the execution time of 'func'
        Then, it prints out the execution time of the function, rounded to TIME_DECIMALS numbers after coma.
        """
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = round(end_time - start_time, TIME_DECIMALS)
        print(f"[PERF_LOG] Функция '{func.__name__}' выполнена за {execution_time} сек.")
        return result
    return wrapper


@performance_logger
def get_sorted_report(revenue_data: list[dict[str, str | float]]) \
        -> list[dict[str, str | float]]:
    """
    This function sorts the given list of dictionaries by key 'total_sales' from the highest to lowest.
    Args:
        revenue_data: a list of dictionaries with keys 'category' and 'total_sales'
    Returns:
        sorted_revenue_data: a sorted list of dictionaries.
    """
    sorted_revenue_data = sorted(revenue_data, key = lambda x: x['total_sales'], reverse=True)
    return sorted_revenue_data


def format_output(revenue_data: list[dict[str, str | float]]) -> str:
    """
    This function formats the output of 'get_sorted_report'
    Then, it prints out the formatted output.
    Args:
        revenue_data: a list of dictionaries with keys 'category' and 'total_sales'
    Returns:
        nothing
    """
    print("Топ категорий по выручке:")
    for i, item in enumerate(revenue_data):
        print(f"{i+1}. {item['category']}: {item['total_sales']}")


#defining test lists
test1 = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55}
]

test2 = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00}
]

test3 = [
    {"category": "Drama", "total_sales": 500.00}
]

#calling the functions and getting a result
sorted_report = get_sorted_report(test1)
format_output(sorted_report)

sorted_report = get_sorted_report(test2)
format_output(sorted_report)

sorted_report = get_sorted_report(test3)
format_output(sorted_report)