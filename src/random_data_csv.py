import csv
import random
import string

# function to generate random data
def generate_random_data(data_type):
    if data_type == 'str':
        return ''.join(random.choices(string.ascii_letters, k=5))
    elif data_type == 'int':
        return random.randint(10000, 99999)
    elif data_type == 'float':
        return format(random.uniform(10000, 99999), '0.4f')
    else:
        return None

def main():
    # prompt user for file locations and number of rows
    input_file = input('Enter the location of the input file: ')
    output_file = input('Enter the location and name of the output file: ')
    num_rows = int(input('Enter the number of rows for the output file: '))

    # read the input file and generate the output data
    with open(input_file, 'rt') as infile:
        reader = csv.reader(infile)
        headers = []
        data_types = []
        for row in reader:
            headers.append(row[0])
            data_types.append(row[1])
        num_columns = len(headers)
        data = []
        for i in range(num_columns):
            data_type = data_types[i]
            random_data = generate_random_data(data_type)
            data.append([random_data] * num_rows)

    # write the output file
    with open(output_file, 'wt', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers)
        for i in range(num_rows):
            writer.writerow([data[j][i] for j in range(num_columns)])

    print(f'Output written to {output_file}')

if __name__ == '__main__':
    main()