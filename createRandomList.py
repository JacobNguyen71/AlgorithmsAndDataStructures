import random


def generate_list(lower_bound, upper_bound):
    return random.sample(range(lower_bound, upper_bound), upper_bound - lower_bound)
