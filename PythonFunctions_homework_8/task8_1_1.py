#=============================================
#---Расчет стоимости оптовой аренды фильмов---
#=============================================

MAX_RENTAL_BATCH_LIMIT = 150.0


#creating a function to calculate rental batch
def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) \
        -> tuple[float, bool]:
    """
    This function calculates the total amount for rental batch.
    Args:
        quantity: quantity of rental batch
        rental_rate: the cost of 1 item
        discount: discount in percent (optional), by default 0.0
    Returns:
        final_sum and is_limit_exceeded
    """
    discount = discount * 0.01 #converting % into float
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    return final_sum, is_limit_exceeded


#defining tests
tests = [
    ("Academy Dinosaur", 30, 2.99, 0.0),
    ("Affair Prejudice", 40, 4.99, 10.0),
    ("Agent Truman", 10, 1.99, 0.0),
    ("African Egg", 50, 3.50, 20.0),
]

#printing the report and calling the function
print("=== ОТЧЁТ ПО ПАРТИЯМ АРЕНДЫ ===")

for i, (title, qty, rate, disc) in enumerate(tests, start=1):
    summ, limit = calculate_rental_batch(qty, rate, disc)
    print(f"Партия {i} ({title}): Сумма: {summ}. Превышение лимита: {limit}")


