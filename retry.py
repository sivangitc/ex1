import random
from functools import wraps
from typing import Callable, Any


def retry(f: Callable) -> Callable:
    @wraps(f)
    def wrapper(*args: Any, **kwds: Any) -> Any:
        val = None
        while val is None:
            val = f(*args, **kwds)
        return val
    return wrapper


@retry
def return_three() -> Any:
    number = random.randint(0, 5)
    print(number)
    if number == 3:
        return number
    return None


if __name__ == "__main__":
    return_three()
