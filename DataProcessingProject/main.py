import sys
import csv

def read_data(file_path):
    data = []
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                try:
                    value = float(row[1])
                    data.append(value)
                except ValueError:
                    print(f"Attention: Invalid Value - {row[1]}")
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    return data


def process_data(data):
    total = sum(data)
    average = total / len(data) if data else 0
    return total, average


def write_output(output_path, total, average):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"Value Total: {total:.2f}\n")
        f.write(f"Average Total: {average:.2f}\n")


import sys
import os

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Correct usage: python main.py data/input.csv")
        sys.exit(1)

    input_file = sys.argv[1]


    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "data")
    output_file = os.path.join(data_dir, "Sales.txt")


    os.makedirs(data_dir, exist_ok=True)

    valori = read_data(input_file)
    total, medie = process_data(valori)
    write_output(output_file, total, medie)

    print("All Done. All info exported to Sales.txt")