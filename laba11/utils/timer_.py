from time import time

def timer(func):
    """
    Декоратор для измерения времени функции
    """
    def wrapper(*args, **kwargs) -> [str, list]:
        start = time()
        result = func(*args, **kwargs)
        end = time()
        return f"{(end - start):.5g} секунд", *result
    return wrapper