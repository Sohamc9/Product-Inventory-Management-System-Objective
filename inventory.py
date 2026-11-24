"""Product Inventory Management System.

Provides price calculation, discount calculation and stock availability
checks with input validation, exception handling and logging.
"""

import logging

logger = logging.getLogger(__name__)


def _validate_price(price):
    """Raise an exception unless price is a non-negative number."""
    if isinstance(price, bool) or not isinstance(price, (int, float)):
        logger.error("Invalid price type: %r", price)
        raise TypeError("Price must be a number")
    if price < 0:
        logger.error("Negative price rejected: %s", price)
        raise ValueError("Price cannot be negative")


def _validate_quantity(quantity, name="Quantity"):
    """Raise an exception unless quantity is a non-negative integer."""
    if isinstance(quantity, bool) or not isinstance(quantity, int):
        logger.error("Invalid %s type: %r", name.lower(), quantity)
        raise TypeError(f"{name} must be a whole number")
    if quantity < 0:
        logger.error("Negative %s rejected: %s", name.lower(), quantity)
        raise ValueError(f"{name} cannot be negative")


def calculate_total_price(price, quantity):
    """Return the total cost for the given unit price and quantity."""
    logger.debug("Calculating total price: price=%s, quantity=%s", price, quantity)
    _validate_price(price)
    _validate_quantity(quantity)

    total = price * quantity
    logger.info("Total price for %s item(s) at %s each: %s", quantity, price, total)
    return total


def apply_discount(total, discount_percent):
    """Return the amount payable after applying a discount percentage."""
    logger.debug("Applying discount: total=%s, discount=%s%%", total, discount_percent)
    _validate_price(total)
    if isinstance(discount_percent, bool) or not isinstance(
        discount_percent, (int, float)
    ):
        logger.error("Invalid discount type: %r", discount_percent)
        raise TypeError("Discount must be a number")
    if not 0 <= discount_percent <= 100:
        logger.error("Discount out of range: %s", discount_percent)
        raise ValueError("Discount must be between 0 and 100")

    if discount_percent == 100:
        logger.warning("100%% discount applied to total %s: item is free", total)

    discounted = total - (total * discount_percent / 100)
    logger.info(
        "Discount of %s%% applied: %s -> %s", discount_percent, total, discounted
    )
    return discounted


def check_stock(available_stock, requested_quantity):
    """Return True if the requested quantity can be fulfilled, else False."""
    logger.debug(
        "Checking stock: available=%s, requested=%s",
        available_stock,
        requested_quantity,
    )
    _validate_quantity(available_stock, "Available stock")
    _validate_quantity(requested_quantity, "Requested quantity")

    if requested_quantity <= available_stock:
        logger.info(
            "Stock available: requested %s, in stock %s",
            requested_quantity,
            available_stock,
        )
        return True

    logger.warning(
        "Insufficient stock: requested %s, only %s available",
        requested_quantity,
        available_stock,
    )
    return False


def main():
    """Run a small demonstration and write the log to application.log."""
    logging.basicConfig(
        filename="application.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logger.info("Inventory demo started")

    try:
        total = calculate_total_price(250, 4)
        payable = apply_discount(total, 10)
        print(f"Total: ₹{total:.2f} | After 10% discount: ₹{payable:.2f}")

        for requested in (30, 80):
            if check_stock(50, requested):
                print(f"Stock check: {requested} unit(s) available")
            else:
                print(f"Stock check: {requested} unit(s) NOT available")

        # Deliberately invalid input to demonstrate exception handling.
        calculate_total_price(-100, 2)
    except (TypeError, ValueError) as error:
        logger.exception("Operation failed")
        print(f"Error: {error}")

    logger.info("Inventory demo finished")


if __name__ == "__main__":
    main()
