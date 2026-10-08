import csv
import os

DATA_FILE = "Occupancy_Estimation.csv"


def load_dataset():
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError("Dataset file not found")

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    return rows


def validate_dataset():
    rows = load_dataset()

    if len(rows) == 0:
        return False

    required_columns = [
        "Date",
        "Time",
        "S1_Temp",
        "S2_Temp",
        "S3_Temp",
        "S4_Temp",
        "S1_Light",
        "S2_Light",
        "S3_Light",
        "S4_Light",
        "S1_Sound",
        "S2_Sound",
        "S3_Sound",
        "S4_Sound",
        "S5_CO2",
        "S5_CO2_Slope",
        "S6_PIR",
        "S7_PIR",
        "Room_Occupancy_Count"
    ]

    for column in required_columns:
        if column not in rows[0]:
            return False

    return True


def get_occupancy_values():
    rows = load_dataset()

    values = []

    for row in rows:
        values.append(int(row["Room_Occupancy_Count"]))

    return values


if __name__ == "__main__":
    print("Dataset loaded successfully")
    print("Number of records:", len(load_dataset()))
    print("Dataset valid:", validate_dataset())
