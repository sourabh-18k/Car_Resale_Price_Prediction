# tests/test_dummy.py

import pandas as pd

def test_data_file_exists():
    """Test if the cleaned car resale dataset exists and can be loaded."""
    try:
        df = pd.read_csv('data/cleaned_car_resale_data.csv')
        assert not df.empty
    except FileNotFoundError:
        assert False, "cleaned_car_resale_data.csv not found."

def test_target_column_present():
    """Check if 'resale_price' column is present in the dataset."""
    df = pd.read_csv('data/cleaned_car_resale_data.csv')
    assert 'resale_price' in df.columns
