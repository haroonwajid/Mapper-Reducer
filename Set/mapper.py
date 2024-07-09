#!/usr/bin/env python3

import sys

def generate_subsets(items):
    subsets = []
    for i in range(len(items)):
        for subset in itertools.combinations(items, i+1):
            subsets.append(subset)
    return subsets

min_support = 3

# Initialize item count dictionary
item_counts = {}

# Read input and count occurrences of each item
for line in sys.stdin:
    items = line.strip().split()
    for item in items:
        item_counts[item] = item_counts.get(item, 0) + 1

# Output frequent itemsets above minimum support threshold
for item, count in item_counts.items():
    if count >= min_support:
        print(f"{item}\t{count}")

