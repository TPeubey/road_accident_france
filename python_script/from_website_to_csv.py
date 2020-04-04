import ssl
import time
import pandas as pd
import structure


class Website2Csv:

    def __init__(self):

        # allow to get the csv file from the website
        ssl._create_default_https_context = ssl._create_unverified_context

        # self.st = structure.ProjectStructure()
        self.st = structure.FolderStructure()
        self.st.start_folder_structure()

    def import_csv_from_website(self, url, file_name):
        dataframe = pd.read_csv(url, sep=',', encoding='latin-1')
        dataframe.to_csv(self.st.folder_raw_data + file_name, encoding='latin-1', index=False)

    def main(self):

        self.import_csv_from_website(self.st.vehicles_url, self.st.vehicles_filename)
        self.import_csv_from_website(self.st.users_url, self.st.users_filename)
        self.import_csv_from_website(self.st.location_url, self.st.location_filename)
        self.import_csv_from_website(self.st.characteristic_url, self.st.characteristic_filename)


if __name__ == '__main__':

    start_time = time.time()

    test = Website2Csv()
    test.main()

    end_time = time.time()

    print('Execution time: ', end_time - start_time)
