import csv




def add_to_csv(new_data):

# CSV file path
    csv_file_path = "output.csv"

    # Check if the CSV file already exists
    file_exists = False
    try:
        with open(csv_file_path, 'r') as file:
            file_exists = True
    except FileNotFoundError:
        pass

    # Append data to CSV file
    with open(csv_file_path, 'a', newline='') as file:
        fieldnames = ["Problem", "Solution", "AVJ", "Reviews", "good/bad"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header if the file is created now
        if not file_exists:
            writer.writeheader()

        # Append new data
        writer.writerows(new_data)

    print(f"Data has been appended to {csv_file_path}.")