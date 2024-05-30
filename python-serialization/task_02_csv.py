#!/usr/bin/python3
"""Convert CSV to JSON"""
import csv
import json

def convert_csv_to_json(csv_filename):
    """Convert CSV file to JSON"""
    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception as error:
        print(f"Error: {error}")
        return False

# Example usage
if __name__ == "__main__":
    result = convert_csv_to_json('input.csv')
    print("Conversion successful:", result)

