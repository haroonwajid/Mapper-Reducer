#!/usr/bin/env python3

import sys
from collections import defaultdict
import itertools

confidence_threshold = 0.1

# Using defaultdict to simplify dictionary handling
itemset_counts = {}
subset_counts = {}

# Read each line from the standard input stream
for line in sys.stdin:
    itemset, count_str = line.strip().split('\t')
    count = int(count_str)

    # Update counts for the entire itemset
    itemset_counts[itemset] += count
    
    # Generate and update counts for all non-empty subsets of the itemset
    items = itemset.split()
    for i in range(1, len(items) + 1):
        for subset in itertools.combinations(items, i):
            subset_str = ' '.join(sorted(subset))
            subset_counts[subset_str] += count

for itemset, full_count in itemset_counts.items():
    items = itemset.split()
    for i in range(1, len(items)):
        for subset in itertools.combinations(items, i):
            # Create the string representation of the current subset
            subset_str = ' '.join(sorted(subset))
            # Compute the complementary set of items
            remaining_items = set(items) - set(subset)
            remaining_items_str = ' '.join(sorted(remaining_items))

            # Calculate the confidence value for the association rule
            confidence = full_count / float(subset_counts[subset_str])

            if confidence >= confidence_threshold:
                print(f"{subset_str} => {remaining_items_str}\t{confidence:.2f}")
