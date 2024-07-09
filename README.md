# Frequency Analysis and Association Rules with MapReduce

This repository contains implementations for two tasks: computing the frequency of pairs and triples of items and computing the confidence score of association rules. The tasks are implemented using MapReduce, and the results are stored locally.

## Table of Contents

- [Task 1: Frequency of Item Pairs and Triples](#task-1-frequency-of-item-pairs-and-triples)
- [Task 2: Confidence Score of Association Rules](#task-2-confidence-score-of-association-rules)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Task 1: Frequency of Item Pairs and Triples

In Task 1, we compute the frequency of pairs and triples of items in a dataset. The results are stored locally. This task leverages MapReduce to efficiently handle large datasets.

### Implementation

The frequency computation is implemented using a single MapReduce pair. The mapper function generates pairs and triples of items, and the reducer function aggregates their counts.

## Task 2: Confidence Score of Association Rules

In Task 2, we compute the confidence score of association rules using the output from Task 1. We set a threshold to filter the rules based on their confidence scores.

### Implementation

This task uses the output from Task 1 as input. A single MapReduce pair is used to compute the confidence scores of the rules and filter them based on a predefined threshold.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/haroonwajid/Mapper-Reduce.git
    cd frequency-association-mapreduce
    ```

2. Install necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run Task 1 to compute the frequency of pairs and triples:
    ```bash
    python task1_frequency.py
    ```

2. Run Task 2 to compute the confidence score of association rules and filter them:
    ```bash
    python task2_association_rules.py
    ```

3. The output will be stored locally in the specified output directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

