import pytest

from inventory import apply_discount, calculate_total_price, check_stock


# ---------- calculate_total_price ----------
def test_total_price_valid():
    assert calculate_total_price(250, 4) == 1000


def test_total_price_zero_quantity():
    assert calculate_total_price(250, 0) == 0


def test_total_price_float_price():
    assert calculate_total_price(19.5, 2) == pytest.approx(39.0)


def test_total_price_negative_price_rejected():
    with pytest.raises(ValueError, match="Price cannot be negative"):
        calculate_total_price(-1, 5)


def test_total_price_negative_quantity_rejected():
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        calculate_total_price(100, -2)


@pytest.mark.parametrize(
    "price, quantity", [("100", 2), (100, 2.5), (None, 1), (True, 1)]
)
def test_total_price_wrong_types_rejected(price, quantity):
    with pytest.raises(TypeError):
        calculate_total_price(price, quantity)


# ---------- apply_discount ----------
def test_discount_valid():
    assert apply_discount(1000, 10) == 900


def test_discount_zero_percent():
    assert apply_discount(1000, 0) == 1000


def test_discount_hundred_percent():
    assert apply_discount(1000, 100) == 0


@pytest.mark.parametrize("percent", [-1, 100.01, 150])
def test_discount_out_of_range_rejected(percent):
    with pytest.raises(ValueError, match="between 0 and 100"):
        apply_discount(1000, percent)


def test_discount_negative_total_rejected():
    with pytest.raises(ValueError):
        apply_discount(-500, 10)


def test_discount_non_numeric_rejected():
    with pytest.raises(TypeError):
        apply_discount(1000, "ten")


# ---------- check_stock ----------
def test_stock_sufficient():
    assert check_stock(50, 30) is True


def test_stock_exact_boundary():
    assert check_stock(50, 50) is True


def test_stock_insufficient():
    assert check_stock(50, 51) is False


def test_stock_zero_available():
    assert check_stock(0, 1) is False


def test_stock_negative_requested_rejected():
    with pytest.raises(ValueError):
        check_stock(50, -1)


def test_stock_negative_available_rejected():
    with pytest.raises(ValueError):
        check_stock(-5, 1)


def test_stock_non_integer_rejected():
    with pytest.raises(TypeError):
        check_stock(50, 2.5)


# ---------- logging ----------
def test_insufficient_stock_logs_warning(caplog):
    with caplog.at_level("WARNING"):
        check_stock(5, 10)
    assert "Insufficient stock" in caplog.text


def test_invalid_input_logs_error(caplog):
    with caplog.at_level("ERROR"), pytest.raises(ValueError):
        calculate_total_price(-1, 1)
    assert "Negative price rejected" in caplog.text
