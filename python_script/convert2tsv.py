import csv
import os
import time

import structure


class ConvertToCsv:

    def __init__(self):
        self.st = structure.FolderStructure()
        self.st.start_folder_structure()

    @property
    def get_file_list(self):
        input_file_list = os.listdir(self.st.folder_raw_data)

        return input_file_list

    def open_csv_file(self):
        for file in self.get_file_list:

            with open(self.st.folder_raw_data + file, encoding='latin-1', mode='r') as input_file, \
                    open(self.st.folder_tsv_data + file.split('.')[0] + '.tsv', mode='w') as output_file:
                input_reader = csv.reader(input_file, delimiter=',')
                header = input_file.readline().split(',')  # read only first line; returns string convert to list
                output_writer = csv.writer(output_file, delimiter='\t')

                self.write_header(output_writer, header, file)
                self.write_tsv_file(input_reader, output_writer, file)

    def write_header(self, output_writer, header, file):
        if file == self.st.characteristic_filename:  # join an/mois/jour columns into a single column 'date'
            del header[1:4]
            header.insert(1, 'date')
            output_writer.writerow(header)  # write header
        else:
            output_writer.writerow(header)  # write header

    def write_tsv_file(self, input_reader, output_writer, file):

        for row in input_reader:
            # self.data_processing_characteristic(file, row)
            if file == self.st.characteristic_filename:  # data_processing_characteristic
                new_date = '-'.join(row[1:4])  # reformat the date
                row.insert(4, new_date)
                del row[1:4]

                if row[10] != 'M':  # This is column '10' because we join the date
                    continue

            if file == self.st.location_filename:  # data_processing_locations
                if (row[1] != '2') & (row[1] != '3'):
                    continue
            output_writer.writerow(row)

    def data_processing_characteristic(self, file, row):
        if file == self.st.characteristic_filename:  # reformat the date
            new_date = '-'.join(row[1:4])
            row.insert(4, new_date)
            del row[1:4]

    def main(self):
        self.open_csv_file()


if __name__ == '__main__':

    start_time = time.time()

    test = ConvertToCsv()
    test.main()

    end_time = time.time()

    print('Execution time: ', end_time - start_time)
