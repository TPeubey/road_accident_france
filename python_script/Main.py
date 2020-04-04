import pandas as pd
import time
import folium
from folium.plugins import MarkerCluster
import replace_value
import structure


class DataProcessing:

    def __init__(self):

        self.rv = replace_value.ReplaceValue()
        self.st = structure.FolderStructure()
        self.st.start_folder_structure()

        pd.set_option('display.max_columns', 100)

    def data_filtering(self):

        df = pd.read_csv(self.st.folder_tsv_data + self.st.loc_tsv_file, sep='\t')
        print(df)

    def join_data(self):
        df_location = pd.read_csv(self.st.folder_tsv_data + self.st.loc_tsv_file, sep='\t')
        df_characteristic = pd.read_csv(self.st.folder_tsv_data + self.st.charac_tsv_file, sep='\t')
        df_usager = pd.read_csv(self.st.folder_tsv_data + self.st.usager_tsv_file, sep='\t')

        self.data_processing(df_characteristic, df_usager, df_location)

        df_merge = df_location.merge(df_characteristic, how='inner', left_on='Num_Acc', right_on='Num_Acc')
        df_merge = df_merge.merge(df_usager, how='inner', left_on='Num_Acc', right_on='Num_Acc')

        self.df2csv(df_merge)

    def data_processing(self, df_characteristic, df_usager, df_location):
        self.latitude_longitude_processing(df_characteristic)
        self.replace_data(df_usager, df_location)
        self.rename_header(df_characteristic, df_usager, df_location)

    @staticmethod
    def latitude_longitude_processing(df_characteristic):
        df_characteristic['lat'] = df_characteristic['lat'] / 10**5
        df_characteristic['long'] = df_characteristic['long'] / 10**5

    def replace_data(self, df_usager, df_location):
        self.replace_value_usager(df_usager)
        self.replace_value_location(df_location)

    def replace_value_usager(self, df_usager):
        self.rv.replace_categorie_usager(df_usager)
        self.rv.replace_accident_severity(df_usager)
        self.rv.replace_gender(df_usager)
        self.rv.replace_journey(df_usager)
        self.rv.replace_localisation(df_usager)
        self.rv.replace_pedestrian_action(df_usager)
        self.rv.replace_pedestrian_alone_or_not(df_usager)

    def replace_value_location(self, df_location):
        self.rv.replace_road_category(df_location)
        self.rv.replace_traffic_regime(df_location)
        self.rv.replace_existence_reserved_lane(df_location)
        self.rv.replace_road_gradient(df_location)
        self.rv.replace_plan_layout(df_location)
        self.rv.replace_surface(df_location)
        self.rv.replace_development_infrastructure(df_location)
        self.rv.replace_accident_situation(df_location)

    @staticmethod
    def rename_header(df_characteristic, df_usager, df_location):
        df_characteristic.rename(columns={"hrmn": "hour_minutes_accident", "lum": "light", "dep\n": "department",
                                          "com": "commune_number", "agg": "outside_in_areas", "int": "intersection",
                                          "atm": "weather_conditions", "col": "collision_type",
                                          "adr": "address", "lat": "latitude", "long": "longitude"}, errors="raise",
                                 inplace=True)

        df_usager.rename(columns={"num_veh\n": "num_veh", "catu": "user_category", "grav": "accident_severity",
                                  "sexe": "gender", "an_nais": "year_of_birth", "trajet": "journey", "secu": "security",
                                  "locp": "pedestrian_location", "actp": "pedestrian_action",
                                  "etatp": "pedestrian_alone_or_not"}, errors="raise", inplace=True)

        df_location.rename(columns={"catr": "road_category", "circ": "traffic_regime",
                                    "nbv": "total_number_of_traffic_lanes",
                                    "vosp": "existence_of_reserved_lane", "prof": "road_gradient",
                                    "lartpc": "width_central_solid_ground",
                                    "larrout": "width_roadway_used_for_traffic", "surf": "surface_condition",
                                    "infra": "Infrastructure", "situ": "accident_situation",
                                    "env1\n": 'school_proximity'}, errors="raise", inplace=True)

    def df2csv(self, df_merge):
        df_merge.to_csv(self.st.folder_join + 'merge.tsv', sep='\t', index=None)

    @staticmethod
    def color_producer(gravite):
        if gravite == 1:  # 1 = Indemne (Indemned)
            return 'green'
        elif gravite == 2:  # 2 = Tué (Killed)
            return 'red'
        elif gravite == 3:  # 3 = Blessé hospitalisé (Injured in hospital)
            return 'orange'
        else:  # 4 = Blessé léger (Minor injury)
            return 'yellow'

    def create_map(self):
        data = pd.read_csv(self.st.folder_join + 'merge.tsv', sep='\t')
        # for speed purposes
        max_records = 500

        map1 = folium.Map(location=[46.7, 2], zoom_start=6)

        mc = MarkerCluster()

        # add a marker for every record in the filtered data, use a clustered view
        for row in data[0:max_records].iterrows():
            mc.add_child(folium.CircleMarker(location=[row[1]['latitude'], row[1]['longitude']],
                                             radius=5,
                                             fill=True,
                                             fill_opacity=1,
                                             fill_color=self.color_producer(row[1]['accident_severity']),
                                             color=self.color_producer(row[1]['accident_severity'])
                                             ))

        map1.add_child(mc)

        map1.save(self.st.folder_map + 'road_accident_france.html')

    def main(self):
        # self.data_filtering()
        self.join_data()
        self.create_map()


if __name__ == '__main__':

    start_time = time.time()

    test = DataProcessing()
    test.main()

    end_time = time.time()

    print("Execution time: ", end_time - start_time)
