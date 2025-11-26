# ML and AI Assignments

A collection of programming assignments focused on ML, AI, and Python fundamentals.

## Modules

### Python Basics (`python_basics/`)

10 Python programming assignments focused on supply chain and warehouse management concepts:

1. **Inventory Normalization** - Parse and validate inventory records
2. **Routing Rules Engine** - Assign warehouse zones based on business rules
3. **Stock Reconciliation** - Compare system vs physical inventory
4. **Purchase Order Costing** - Calculate PO totals with tax
5. **ShipmentTracker Class** - Track shipments with class/instance attributes
6. **BinCollection Sequence Class** - Custom sequence type implementation
7. **Naive Forecasting** - Analyze demand patterns
8. **SKU Comparison Class** - Case-insensitive SKU comparison
9. **Warehouse Allocation Simulator** - First-fit bin allocation
10. **Linehaul Time Calculator** - Calculate transit times

## Setup

```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync --dev
```

## Running Tests

Run all tests:
```bash
uv run pytest
```

Run tests for a specific module:
```bash
uv run pytest tests/test_python_basics/
```

Run tests for a specific assignment:
```bash
uv run pytest tests/test_python_basics/test_01_inventory_normalization.py
```

Run with verbose output:
```bash
uv run pytest -v
```

## Running Individual Assignments

Each assignment file can be run directly:
```bash
uv run python python_basics/inventory_normalization_01.py
```

This will run the built-in tests and show whether your implementation passes.

## How to Complete Assignments

1. Open the assignment file (e.g., `python_basics/inventory_normalization_01.py`)
2. Find the function/class stubs with `# TODO: Implement this function`
3. Replace `pass` with your implementation
4. Run the file or pytest to check your solution
