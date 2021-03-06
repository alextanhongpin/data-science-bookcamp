import itertools
from collections import defaultdict


def is_in_interval(number, minimum, maximum):
    return minimum <= number <= maximum


def generate_coin_sample_space(num_flips=10):
    weighted_sample_space = defaultdict(int)

    for coin_flips in itertools.product(["heads", "tails"], repeat=num_flips):
        heads_count = len([outcome for outcome in coin_flips if outcome == "heads"])
        weighted_sample_space[heads_count] += 1

    return weighted_sample_space
