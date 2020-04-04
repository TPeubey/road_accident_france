import os
import sys


class ProjectStructure:

    def __init__(self):

        # Variable use in from_website_to_csv file
        # url of csv file
        self.vehicles_url = 'https://static.data.gouv.fr/resources/' \
                            'base-de-donnees-accidents-corporels-de-la-circulation/20191014-112113/vehicules-2018.csv'
        self.users_url = 'https://static.data.gouv.fr/resources/' \
                         'base-de-donnees-accidents-corporels-de-la-circulation/20191014-112100/usagers-2018.csv'
        self.location_url = 'https://static.data.gouv.fr/resources/' \
                            'base-de-donnees-accidents-corporels-de-la-circulation/20191014-112036/lieux-2018.csv'
        self.characteristic_url = 'https://static.data.gouv.fr/resources/' \
                                  'base-de-donnees-accidents-corporels-de-la-circulation/20191014-111741/' \
                                  'caracteristiques-2018.csv'

        # get the file name for each csv file
        self.vehicles_filename = self.vehicles_url.split('/')[-1]
        self.users_filename = self.users_url.split('/')[-1]
        self.location_filename = self.location_url.split('/')[-1]
        self.characteristic_filename = self.characteristic_url.split('/')[-1]

        # get the file name for each tsv file
        self.vehicles_tsv_file = self.vehicles_filename.replace('csv', 'tsv')
        self.usager_tsv_file = self.users_filename.replace('csv', 'tsv')
        self.loc_tsv_file = self.location_filename.replace('csv', 'tsv')
        self.charac_tsv_file = self.characteristic_filename.replace('csv', 'tsv')

        # Initialize path folder and path working directory
        self.working_directory = ''

        self.folder_raw_data = ''
        self.folder_tsv_data = ''
        self.folder_join = ''
        self.folder_map = ''

    @staticmethod
    def confirm_working_directory(project_name):
        working_directory = sys.path[0]
        the_list = working_directory.split('/')
        i = 0
        for i, name in enumerate(the_list):
            if project_name in name:
                break
        return '/'.join(the_list[:i + 1]) + '/'

    def main(self):
        print(self.characteristic_filename)
        print(self.location_filename)


class FolderStructure(ProjectStructure):

    def start_folder_structure(self):
        self.working_directory = self.confirm_working_directory('accident_route_france')
        self.__create_folder_name()
        self.__create_folders()

    def __create_folder_name(self):
        self.folder_python_script = self.working_directory + 'python_script/'
        self.folder_raw_data = self.working_directory + 'raw_data/'
        self.folder_tsv_data = self.working_directory + '0_tsv/'
        self.folder_join = self.working_directory + '1_join/'
        self.folder_map = self.working_directory + '2_map/'

    def __create_folders(self):
        require = [self.folder_raw_data, self.folder_tsv_data, self.folder_join, self.folder_map]

        for i in require:
            try:
                if not os.path.isfile(i):
                    os.mkdir(i)
            except:
                pass

    def main(self):
        print(self.folder_python_script)


if __name__ == '__main__':
    test = ProjectStructure()
    # test.main()

    start = FolderStructure()
    start.start_folder_structure()
    start.main()
