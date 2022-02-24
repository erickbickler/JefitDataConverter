from asyncore import write
import sqlite3
import csv

CSV_INPUT_FILE_NAME = "jefit_data.csv"
DATABASE_PATH = "jefit_data.db"

def write_to_csv(path, data):
    with open(path, "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerows(data)


def seperate_csvs():
    table_exclusions = []
    with open(CSV_INPUT_FILE_NAME, "r") as input_file:
        data = list(csv.reader(input_file))
        for index, line in enumerate(data):
            if len(line) > 0 and line[0].startswith('### '):
                table_name = line[0].strip("#").strip()
                end = data.index(["######################################################"], index)
                table_data = data[index + 2:end - 2]
                if len(table_data) == 0:
                    continue
                write_to_csv("TableCSVs/" + table_name + '.csv', table_data)
                

def create_tables():
    conn = sqlite3.connect(DATABASE_PATH)

if __name__ == "__main__":
    seperate_csvs()