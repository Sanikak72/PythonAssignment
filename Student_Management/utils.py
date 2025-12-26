import math
import random
import datetime

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_random_id():
    return random.randint(1000, 9999)

def print_math_properties():
    print(f"Math module properties: {dir(math)}")
