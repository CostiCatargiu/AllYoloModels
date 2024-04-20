import os
import re

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
    num_files = len(dict_list)
    all_classes = set()

    for d in dict_list:
        for table in d:
            all_classes.update(table.keys())
    all_classes.discard('name')
    all_classes = sorted(all_classes)

    max_class_name_length = max(len(class_name) for class_name in all_classes)
    class_width = max(12, max_class_name_length + 2)

    for table_index in range(len(dict_list[0])):
        table_name = dict_list[0][table_index]['name']
        print(f"\nComparison for: {table_name}", file=file)
        print("{:<15} {:<8}".format("Model", "Metric"), end="", file=file)
        for class_name in all_classes:
            print(f"{class_name:<{class_width}}", end="", file=file)
        print("\n" + "-" * (23 + class_width * len(all_classes)), file=file)

        for idx, d in enumerate(dict_list):
            model_name = headers[idx]
            print("{:<15} {:<8}".format(model_name, "AvgP"), end="", file=file)
            for class_name in all_classes:
                avgp = d[table_index].get(class_name, {}).get('AvgP', 'N/A')
                print(f"{avgp:<{class_width}}", end="", file=file)
            print(file=file)

            print("{:<15} {:<8}".format(model_name, "NrDet"), end="", file=file)
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
    avg_fps_pattern = re.compile(r'Average FPS:\s*([\d\.]+)')
    avg_inf_time_pattern = re.compile(r'Average InfTime:\s*([\d\.]+)\s*ms')
    total_inf_time_pattern = re.compile(r'Total inference time:\s*([\d\.]+)\s*s')

    for line in lines:
        if match := total_detections_pattern.search(line):
            additional_data['All Detections'] = match.group(1)
        elif match := avg_fps_pattern.search(line):
            additional_data['Avg FPS'] = match.group(1)
        elif match := avg_inf_time_pattern.search(line):
            additional_data['Avg InfTime'] = match.group(1) + ' ms'
        elif match := total_inf_time_pattern.search(line):
            additional_data['Total InfTime'] = match.group(1) + ' s'

    return additional_data

def compare_additional_metrics(all_additional_data, headers, file):
    print("\nComparison of Additional Metrics", file=file)
    metrics = sorted(set().union(*(d.keys() for d in all_additional_data)))
    metric_width = max(len(metric) for metric in metrics) + 2
    print("{:<15}".format(""), end="", file=file)
    for header in headers:
        print(f"{header:<12}", end="", file=file)
    print(file=file)
    print("-" * (15 + 12 * len(headers)), file=file)

    for metric in metrics:
        print(f"{metric:<{metric_width}}", end="", file=file)
        for data in all_additional_data:
            print(f"{data.get(metric, 'N/A'):<12}", end="", file=file)
        print(file=file)
    print("-" * (15 + 12 * len(headers)), file=file)

def main():
    directory_path = 'ExperimentalResults/Metrics/'
    filenames = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if f.endswith('.txt')]
    headers = [os.path.basename(file).split('.')[0] for file in filenames]

    output_file = "Utils/Scripts/metrics.txt"
    with open(output_file, 'w') as file:
        all_table_data = [extract_table_data(file_name) for file_name in filenames]
        reformat_and_compare_tables(all_table_data, headers, file)

        all_additional_data = [extract_additional_data(file_name) for file_name in filenames]
        compare_additional_metrics(all_additional_data, headers, file)

if __name__ == "__main__":
    main()
