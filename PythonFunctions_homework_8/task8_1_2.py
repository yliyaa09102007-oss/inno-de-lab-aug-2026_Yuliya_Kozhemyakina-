#=============================================
#---Расчет стоимости оптовой аренды фильмов---
#=============================================

MAX_RENTAL_BATCH_LIMIT = 150.0

#creating a wrapper to format the output
def format_output(func):
    def wrapper(*args, **kwargs):
        batch_index, name, total, is_limit_exceeded = func(*args, **kwargs)
        return f"Партия {batch_index} ({name}): Сумма: {total}$. Превышение лимита: {is_limit_exceeded}"
    return wrapper

#creating a function to calculate rental batch
#now we can give the function name and batch_index, though we don't use it inside the function,
#so I'm not sure if this is correct
@format_output
def calculate_rental_batch(quantity: int, rental_rate: float,
        discount: float = 0.0, batch_index: int = 0, name: str = "") \
        -> tuple[int, str, float, bool]:
    """
    This function calculates the total amount for rental batch.
    Args:
        quantity: quantity of rental batch
        rental_rate: the cost of 1 item
        discount: discount in percent (optional), by default 0.0
        batch_index: index of batch (optional), by default 0
        name: name of batch (optional), by default ""
    Returns:
        batch_index, name, final_sum and is_limit_exceeded
    """
    discount = discount * 0.01 #converting % into float
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT

    return batch_index, name, final_sum, is_limit_exceeded

#printing the report and calling the function
print("=== ОТЧЁТ ПО ПАРТИЯМ АРЕНДЫ ===")
print(f"{calculate_rental_batch(batch_index = 1, name = 'Academy Dinosaur', quantity = 30, rental_rate = 2.99)}")
print(f"{calculate_rental_batch(40, 4.99, 10, 2, 'Affair Prejudice')}")
print(f"{calculate_rental_batch(10, 1.99, batch_index = 3, name = 'Agent Truman')}")
print(f"{calculate_rental_batch(50, 3.50, 20, 4, 'African Egg')}")
