#!/usr/bin/env python3

import sys

# Initialize itemset count dictionary
itemset_counts = {}
threshold = 0.5

# Read input and aggregate counts
for line in sys.stdin:
    rule, count = line.strip().split('\t')
    itemset_counts[rule] = float(count)

# Output association rules with support
for rule, count in itemset_counts.items():
    print(f"{rule}\t{count}")

