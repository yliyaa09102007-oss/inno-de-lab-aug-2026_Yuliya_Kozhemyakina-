#=============================================
#---Расчет стоимости оптовой аренды фильмов---
#=============================================

MAX_RENTAL_BATCH_LIMIT = 150.0

#creating a wrapper to format the output
def format_output(func):
    def wrapper(*args, **kwargs):
        total, is_limit_exceeded = func(*args, **kwargs)
        return f"Сумма: {total}$. Превышение лимита: {is_limit_exceeded}"
    return wrapper

#creating a function to calculate rental batch
#maybe it would be better to also have parameters "name" and "index"? Not mentioned in the task though...
@format_output
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

#printing the report and calling the function
print("=== ОТЧЁТ ПО ПАРТИЯМ АРЕНДЫ ===")
print(f"Партия 1 (Academy Dinosaur): {calculate_rental_batch(quantity = 30, rental_rate = 2.99)}")
print(f"Партия 2 (Affair Prejudice): {calculate_rental_batch(40, 4.99, 10)}")
print(f"Партия 3 (Agent Truman): {calculate_rental_batch(10, 1.99)}")
print(f"Партия 4 (African Egg): {calculate_rental_batch(50, 3.50, discount=20)}")
