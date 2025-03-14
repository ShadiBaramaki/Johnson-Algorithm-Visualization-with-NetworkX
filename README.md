# Johnson's Algorithm Visualization

## Overview
This Python application provides a graphical visualization of **Johnson’s Algorithm**, which efficiently computes the shortest paths between all pairs of nodes in a weighted graph. It features a **Tkinter-based GUI** for user-friendly input and leverages **NetworkX** and **Matplotlib** to display both the original and modified graphs.


## Installation
Ensure you have Python installed, then install the required dependencies:

```bash
pip install matplotlib networkx tkinter
```
## Usage
1. Run the script:

    ```bash
    python johnson_algorithm.py
    ```
2. Enter the adjacency matrix in the text box. Example:
    ```
    0 -5 2 3
    0 0 4 0
    0 0 0 1
    0 0 0 0
    ```
3. Click the button to process the graph.
4. After processing, the original and modified graphs will be displayed, along with the computed shortest paths for each node.
## How It Works

1. **Graph Input**: The user enters an adjacency matrix representing the weighted graph.

2. **Johnson's Algorithm Execution**:
    - The **Bellman-Ford Algorithm** checks for negative weight cycles and reweights the graph.
    - **Dijkstra’s Algorithm** computes the shortest paths for each node.

3. **Graph Visualization**:
    - The original and modified graphs are displayed.
    - The shortest paths are shown for each source node.
