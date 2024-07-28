
### Test Example

import pytest
import pandas as pd
from app import (
    read_data, compute_total_revenue_per_month, compute_total_revenue_per_product,
    compute_total_revenue_per_customer, top_10_customers_by_revenue
)

@pytest.fixture
def sample_data():
    data = {
        'order_id': [1, 2, 3, 4, 5],
        'customer_id': [101, 102, 103, 104, 105],
        'order_date': ['2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'],
        'product_id': [1001, 1002, 1003, 1004, 1005],
        'product_name': ['A', 'B', 'C', 'D', 'E'],
        'product_price': [10, 20, 30, 40, 50],
        'quantity': [1, 2, 3, 4, 5]
    }
    df = pd.DataFrame(data)
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df

def test_compute_total_revenue_per_month(sample_data):
    result = compute_total_revenue_per_month(sample_data)
    assert result is not None
    assert len(result) == 5

def test_compute_total_revenue_per_product(sample_data):
    result = compute_total_revenue_per_product(sample_data)
    assert result is not None
    assert len(result) == 5

def test_compute_total_revenue_per_customer(sample_data):
    result = compute_total_revenue_per_customer(sample_data)
    assert result is not None
    assert len(result) == 5

def test_top_10_customers_by_revenue(sample_data):
    result = top_10_customers_by_revenue(sample_data)
    assert result is not None
    assert len(result) == 5
