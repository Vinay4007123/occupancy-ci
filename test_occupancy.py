import unittest

from occupancy import load_dataset, validate_dataset, get_occupancy_values


class TestOccupancyDataset(unittest.TestCase):

    def test_dataset_exists_and_has_records(self):
        rows = load_dataset()
        self.assertGreater(len(rows), 0)

    def test_required_columns_exist(self):
        self.assertTrue(validate_dataset())

    def test_occupancy_values_are_numeric(self):
        values = get_occupancy_values()

        self.assertGreater(len(values), 0)

        for value in values:
            self.assertIsInstance(value, int)

    def test_occupancy_values_are_non_negative(self):
        values = get_occupancy_values()

        for value in values:
            self.assertGreaterEqual(value, 0)


if __name__ == "__main__":
    unittest.main()
