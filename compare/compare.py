import csv
import glob


def load_ids_from(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        file_ids = []
        next(csv_reader)  # Skip the header row of the CSV file
        for row in csv_reader:
            file_ids.append(row[0])
    return file_ids


all_csv_files = glob.glob("data/*.csv")
scheme_accounts = [load_ids_from(file) for file in all_csv_files]
print(set.intersection(*map(set, scheme_accounts)))
