import time
import pandas as pd
from library import structure


class LoadToBigquery:

    def __init__(self):
        self.st = structure.FolderStructure()
        self.st.start_folder_structure()

        self.dataset_id = 'road_accident_france'
        self.project_id = 'my-project-34577'

    @staticmethod
    def tsv2bigquery(path, file, dataset_id, table_id, project_id, table_schema):
        df = pd.read_csv(path + file, sep='\t')
        df.to_gbq(dataset_id + '.' + table_id, project_id=project_id, table_schema=table_schema, if_exists='replace')

    def merge_table_to_bigquery(self):

        merge_table_schema = [
            {'name': 'Num_Acc', 'type': 'INTEGER', 'description': 'Accident identification number'},
            {'name': 'road_category',   'type': 'STRING', 'description': 'Category of road'},
            {'name': 'voie', 'type': 'STRING', 'description': 'Number of the road'},
            {'name': 'v1', 'type': 'FLOAT', 'description': 'Numerical index of route number'},
            {'name': 'v2', 'type': 'STRING', 'description': 'Alphanumeric road index letter'},
            {'name': 'traffic_regime', 'type': 'STRING', 'description': 'Circulation regime'},
            {'name': 'total_number_of_traffic_lanes', 'type': 'FLOAT', 'description': 'Total number of traffic lanes'},
            {'name': 'pr', 'type': 'FLOAT',
             'description': 'Number of the connecting PR (number of the upstream terminal)'},
            {'name': 'pr1', 'type': 'FLOAT',
             'description': 'Distance in metres to the PR (from the upstream terminal)'},
            {'name': 'existence_of_reserved_lane', 'type': 'STRING',
             'description': 'Indicates the existence of a reserved lane, regardless of whether or'
                            'not the accident takes place in that lane.'},
            {'name': 'road_gradient', 'type': 'STRING',
             'description': 'Longitudinal profile describes the gradient of the road at the accident site.'},
            {'name': 'plan', 'type': 'STRING', 'description': 'Plan layout'},
            {'name': 'width_central_solid_ground', 'type': 'FLOAT',
             'description': 'Width of the central solid earth (TPC) if it exists'},
            {'name': 'width_roadway_used_for_traffic', 'type': 'FLOAT',
             'description': 'Width of roadway used for vehicular traffic excluding hard shoulder,'
                            'TPCs and parking spaces'},
            {'name': 'surface_condition', 'type': 'STRING', 'description': 'Etat de la surface'},
            {'name': 'Infrastructure', 'type': 'STRING', 'description': 'Development - Infrastructure'},
            {'name': 'accident_situation', 'type': 'STRING', 'description': 'Accident situation'},
            {'name': 'school_proximity', 'type': 'FLOAT', 'description': 'school point: proximity to a school'},
            {'name': 'date', 'type': 'STRING', 'description': 'accident date'},
            {'name': 'hour_minutes_accident', 'type': 'INTEGER', 'description': 'hours and minutes of the accident'},
            {'name': 'light', 'type': 'INTEGER',
             'description': 'Light: lighting conditions in which the accident occurred.'},
            {'name': 'outside_in_areas', 'type': 'INTEGER', 'description': 'Location: Out of town or In town '},
            {'name': 'intersection', 'type': 'INTEGER', 'description': 'Intersection'},
            {'name': 'weather_conditions', 'type': 'FLOAT', 'description': 'Weather conditions'},
            {'name': 'collision_type', 'type': 'FLOAT', 'description': 'Type of collision'},
            {'name': 'commune_number', 'type': 'INTEGER',
             'description': 'Commune: The commune number is a code given by INSEE.'
                            'The code has 3 digits on the right.'},
            {'name': 'address', 'type': 'STRING',
             'description': 'Postal address: variable filled in for accidents occurring in built-up areas.'},
            {'name': 'gps', 'type': 'STRING', 'description': 'GPS coding: 1 character origin indicator'},
            {'name': 'latitude', 'type': 'FLOAT', 'description': 'Geographical coordinates in decimal degrees'},
            {'name': 'longitude', 'type': 'FLOAT', 'description': 'Geographical coordinates in decimal degrees'},
            {'name': 'department', 'type': 'INTEGER',
             'description': 'Department: Code INSEE (Institut National de la Statistique etdes Etudes Economiques)'
                            'of the department followed by a 0 (201 Corse-du-Sud - 202 Haute-Corse)'},
            {'name': 'place', 'type': 'FLOAT',
             'description': 'Allows you to locate the space occupied in'
                            'the vehicle by the user at the time of the accident.'},
            {'name': 'user_category', 'type': 'STRING', 'description': 'User category'},
            {'name': 'accident_severity', 'type': 'STRING',
             'description': 'Severity of the accident: Accident victims are classified into'
                            'three categories of victims plus those who are not injured'},
            {'name': 'gender', 'type': 'STRING', 'description': 'Gender of user'},
            {'name': 'journey', 'type': 'STRING', 'description': 'Reason for displacement at the time of the accident'},
            {'name': 'security', 'type': 'FLOAT', 'description': """
            on 2 characters :
            the first concerns the existence of a Safety Equipment
            1 - Belt
            2 - Helmet
            3 - Children's device
            4 - Reflective equipment
            9 - Other
            the second concerns the use of Safety Equipment
             1 - Yes
             2 - No
             3 - Not determinable
            """},
            {'name': 'pedestrian_location', 'type': 'STRING', 'description': 'Location of the pedestrian'},
            {'name': 'pedestrian_action', 'type': 'STRING', 'description': 'Pedestrian action'},
            {'name': 'pedestrian_alone_or_not', 'type': 'STRING',
             'description': 'This variable specifies whether or not the injured pedestrian was alone.'},
            {'name': 'year_of_birth', 'type': 'FLOAT', 'description': 'Year of birth of the user'},
            {'name': 'num_veh', 'type': 'STRING',
             'description': 'Identifier of the vehicle taken over for each of the users occupyingthat vehicle'
                            '(including pedestrians attached to the vehicles that hit them) - Alphanumeric code '}
        ]

        self.tsv2bigquery(self.st.folder_join, 'merge.tsv',
                          self.dataset_id, 'summary_table', self.project_id, merge_table_schema)

    def main(self):
        self.merge_table_to_bigquery()


if __name__ == '__main__':

    start_time = time.time()

    test = LoadToBigquery()
    test.main()

    end_time = time.time()

    print("Execution time: ", end_time - start_time)
