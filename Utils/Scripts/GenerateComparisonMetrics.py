import os
import re
import pandas as pd
from tabulate import tabulate

def extract_table_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    table_names = []
    starts = []
    for i, line in enumerate(lines):
        if 'Class' in line and 'AvgP' in line:
            starts.append(i)
            if lines[i - 1].strip() not in table_names:
                table_names.append(lines[i - 1].strip())

    ends = [i for i, line in enumerate(lines) if line.strip() == '']
    if len(ends) < len(starts):
        ends.append(len(lines))

    tables = [lines[starts[i]:ends[i]] for i in range(len(starts))]
    tables_data = []
    for table, name in zip(tables, table_names):
        table_dict = {'name': name}
        for line in table[1:]:
            if line.strip():
                parts = line.split()
                class_name = " ".join(parts[:-2])
                avgp = parts[-2]
                nrdet = parts[-1]
                table_dict[class_name] = {'AvgP': avgp, 'NrDet': nrdet}
        tables_data.append(table_dict)

    return tables_data

def reformat_and_compare_tables(dict_list, headers, file):
    all_classes = set()

    for d in dict_list:
        for table in d:
            all_classes.update(table.keys())
    all_classes.discard('name')
    all_classes = sorted(all_classes)

    sort_det = []
    for table_index in range(len(dict_list[0])):
        for idx, d in enumerate(dict_list):
            for class_name in all_classes:
                nrdet = d[table_index].get(class_name, {}).get('NrDet', 'N/A')
                sort_det.append(nrdet)
        break
    list1_int = [int(x) if x != 'N/A' else float('-inf') for x in sort_det]
    combined = list(zip(list1_int, all_classes))
    sorted_combined = sorted(combined, key=lambda x: x[0], reverse=True)
    sorted_list1_int, sorted_list2 = zip(*sorted_combined)
    all_classes = sorted_list2

    max_class_name_length = max(len(class_name) for class_name in all_classes)
    class_width = max(4, max_class_name_length + 2)

    for table_index in range(len(dict_list[0])):
        table_name = dict_list[0][table_index]['name']
        print(f"\nComparison for: {table_name}", file=file)
        print("{:<10} {:<8}".format("Model", "Metric"), end="", file=file)
        for class_name in all_classes:
            print(f"{class_name:<{class_width}}", end="", file=file)
        print("\n" + "-" * (23 + class_width * len(all_classes)), file=file)

        for idx, d in enumerate(dict_list):
            model_name = headers[idx]
            print("{:<10} {:<8}".format(model_name, "AvgP"), end="", file=file)
            for class_name in all_classes:
                avgp = d[table_index].get(class_name, {}).get('AvgP', 'N/A')
                print(f"{avgp:<{class_width}}", end="", file=file)
            print(file=file)

            print("{:<10} {:<8}".format(model_name, "NrDet"), end="", file=file)
            for class_name in all_classes:
                nrdet = d[table_index].get(class_name, {}).get('NrDet', 'N/A')
                print(f"{nrdet:<{class_width}}", end="", file=file)
            print(file=file)
            print("-" * (23 + class_width * len(all_classes)), file=file)

def extract_additional_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    additional_data = {}
    total_detections_pattern = re.compile(r'Total number of detections:\s*(\d+)')
    confidence_threshold_pattern = re.compile(r'confidence threshold:\s*(\d+\.?\d*)', re.IGNORECASE)
    avg_fps_pattern = re.compile(r'Average FPS:\s*([\d\.]+)')
    avg_inf_time_pattern = re.compile(r'Average InfTime:\s*([\d\.]+)\s*ms')
    total_inf_time_pattern = re.compile(r'Total inference time:\s*([\d\.]+)\s*s')

    for line in lines:
        if match := total_detections_pattern.search(line):
            additional_data['All Detections'] = match.group(1)
        if match := avg_fps_pattern.search(line):
            additional_data['Avg FPS'] = match.group(1)
        if match := avg_inf_time_pattern.search(line):
            additional_data['Avg InfTime'] = match.group(1) + ' ms'
        if match := total_inf_time_pattern.search(line):
            additional_data['Total InfTime'] = match.group(1) + ' s'
        if match := confidence_threshold_pattern.search(line):
            additional_data['Conf_thr'] = match.group(1)
    return additional_data


def compare_additional_metrics(all_additional_data, headers, file):
    print("\nComparison of Additional Metrics", file=file)
    # Prepare the data
    metrics = sorted(set().union(*(d.keys() for d in all_additional_data)))
    data_dict = {header: [] for header in headers}
    data_dict["Metric"] = metrics

    for metric in metrics:
        for i, data in enumerate(all_additional_data):
            data_dict[headers[i]].append(data.get(metric, 'N/A'))

    # Create a DataFrame
    df = pd.DataFrame(data_dict)
    df = df[["Metric"] + headers]  # Ensure the correct order of columns

    # Use tabulate to format the DataFrame with borders
    table = tabulate(df, headers='keys', tablefmt='grid')

    # Print the table
    print(table, file=file)
    print("\n*************************************More Informations**************************************", file=file)



def read_last_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines[-1], lines[-2] if lines else None
def print_last_lines_from_files(file_list,file):
    for filename in file_list:
        base_filename = os.path.splitext(os.path.basename(filename))[0]
        last_line, lastt_line = read_last_line(filename)
        print(f"{base_filename}: {last_line}",file=file)
        print(f"{base_filename}: {lastt_line}",file=file)


# Print the last line from each file

class ConfusionMatrixAnalyzer:
    def __init__(self, input_directory, output_file):
        self.input_directory = input_directory
        self.output_file = output_file
        self.confusion_data = {}

    def parse_file(self, filename):
        model_name = filename.split('.')[0]
        self.confusion_data[model_name] = {}

        pattern = re.compile(
            r'Classes (?P<class1>\w+) and (?P<class2>\w+) mismatched in (?P<frames>\d+) frames\.\n'
            r'Class (?P<class1_repeat>\w+) was predicted: (?P<class1_count>\d+) times in these frames\.\n'
            r'Class (?P<class2_repeat>\w+) was predicted: (?P<class2_count>\d+) times in these frames\.\n'
        )

        with open(os.path.join(self.input_directory, filename), 'r') as file:
            content = file.read()
            matches = pattern.finditer(content)
            for match in matches:
                class1 = match.group('class1')
                class2 = match.group('class2')
                frames = match.group('frames')
                class1_count = match.group('class1_count')
                class2_count = match.group('class2_count')

                class_pair = f"{class1} - {class2}"
                self.confusion_data[model_name][class_pair] = f"{class1_count} - {class2_count} ({frames})"

    def read_files(self):
        for filename in os.listdir(self.input_directory):
            if filename.endswith('.txt'):
                self.parse_file(filename)

    def create_dataframe(self):
        # Get all unique confusion pairs
        all_pairs = set()
        for model, data in self.confusion_data.items():
            all_pairs.update(data.keys())

        # Ensure consistent order of columns
        all_pairs = sorted(all_pairs)

        # Sort models alphabetically
        sorted_models = sorted(self.confusion_data.keys())

        # Create a list to store the DataFrame rows
        rows = []

        # Populate the rows list with confusion data
        for model in sorted_models:
            data = self.confusion_data[model]
            row = {'Model': model}
            for pair in all_pairs:
                row[pair] = data.get(pair, 'N/A')
            rows.append(row)

        # Convert the list of rows into a DataFrame
        self.df = pd.DataFrame(rows, columns=['Model'] + all_pairs)

    def generate_table(self):
        # Center align values
        for col in self.df.columns:
            self.df[col] = self.df[col].astype(str).apply(lambda x: x.center(20))

        # Format the DataFrame as a table
        self.table = tabulate(self.df, headers='keys', tablefmt='grid')

    def save_to_file(self):
        # Write the formatted table to a text file
        with open(self.output_file, 'a') as f:
            f.write("\n\nTable that contains an overview of the Confused Classes that were predicted for each model\n")
            f.write(self.table)
            f.write("\n\n")

    def run(self):
        self.read_files()
        self.create_dataframe()
        self.generate_table()
        self.save_to_file()



def main():
    directory_path = '../../ExperimentalResults/Metrics/day_video'
    filenames = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.txt')]
    filenames.sort()
    headers = [os.path.basename(file).split('.')[0] for file in filenames]

    output_file = "metrics.txt"
    with open(output_file, 'w') as file:
        all_table_data = [extract_table_data(file_name) for file_name in filenames]
        reformat_and_compare_tables(all_table_data, headers, file)

    analyzer = ConfusionMatrixAnalyzer(directory_path, output_file)
    analyzer.run()

    with open(output_file, 'a') as file:
        all_additional_data = [extract_additional_data(file_name) for file_name in filenames]
        compare_additional_metrics(all_additional_data, headers, file)
        print_last_lines_from_files(filenames, file)



if __name__ == "__main__":
    main()
