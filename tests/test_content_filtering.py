import pytest
import pandas as pd
from config.helper_functions import book_data_reading
book_data, _ = book_data_reading()

@pytest.fixture(scope="class")

def book_df():
  # We only want to pull this data once for each TestCase since it is an expensive operation
  df = pd.read_csv(book_data, index_col=0)
  return df

class TestContentFilteringData:

  def test_required_columns_present(self, book_df):
    # ensures that the expected columns are all present

    assert "Janr" in book_df.columns
    assert "Nəşriyyat" in book_df.columns
    assert "Cild" in book_df.columns
    assert "Müəllif" in book_df.columns
    assert "dil" in book_df.columns
    assert "ad" in book_df.columns
    assert "qiymet" in book_df.columns
    assert "collection" in book_df.columns

  def test_non_empty(self, book_df):
    # ensures that there is more than one row of data
    assert len(book_df.index) != 0



