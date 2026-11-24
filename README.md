# Product Inventory Management System

A small Python application that calculates product totals, applies discounts and checks stock availability. It validates inputs, raises suitable exceptions, logs every operation to `application.log`, and is covered by pytest tests. Code quality is checked and formatted with Ruff.

## Features implemented

- `calculate_total_price(price, quantity)` returns `price * quantity`.
- `apply_discount(total, discount_percent)` returns the amount payable after the discount.
- `check_stock(available_stock, requested_quantity)` returns `True` if the request can be fulfilled, otherwise `False`.
- Input validation: `ValueError` for negative values and discounts outside 0-100; `TypeError` for wrong types (strings, decimals for quantities, booleans).
- Logging at DEBUG, INFO, WARNING and ERROR levels, written to `application.log`.
- 26 pytest tests covering valid inputs, boundary conditions, invalid inputs and logging.
- Ruff linting and formatting.

## Project structure

```
product-inventory-management/
├── inventory.py        # application code
├── test_inventory.py   # pytest tests
├── README.md
├── .gitignore
└── application.log     # generated when inventory.py runs
```

## macOS setup

Check that Python 3 and pip are installed:

```bash
python3 --version
python3 -m pip --version
```

Clone the repository and enter the folder:

```bash
git clone https://github.com/YOUR-USERNAME/product-inventory-management.git
cd product-inventory-management
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Installation

```bash
python -m pip install --upgrade pip
python -m pip install pytest ruff
```

## Running the application

```bash
python inventory.py
cat application.log
```

## Running the tests

```bash
python -m pytest -v
```

Expected result: all 26 tests pass.

## Code quality (Ruff)

```bash
python -m ruff check .
python -m ruff check . --fix
python -m ruff format .
python -m ruff check .
```

Expected result: `All checks passed!`

## Screenshots

Screenshots of the pytest run and the Ruff checks are in the `screenshots/` folder.
# Product-Inventory-Management-System-Objective
