#!/usr/bin/env python3

import sys

# Initialize item count dictionary
item_counts = {}

# Read input and aggregate counts
for line in sys.stdin:
    item, count = line.strip().split('\t')
    item_counts[item] = item_counts.get(item, 0) + int(count)

# Output frequent itemsets above minimum support threshold
for item, count in item_counts.items():
    print(f"{item}\t{count}")

