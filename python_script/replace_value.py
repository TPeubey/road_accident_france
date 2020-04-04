

class ReplaceValue:

    @staticmethod
    def replace_categorie_usager(df_usager):
        df_usager['catu'] = df_usager['catu'].replace(1, 'Conducteur')
        df_usager['catu'] = df_usager['catu'].replace(2, 'Passager')
        df_usager['catu'] = df_usager['catu'].replace(3, 'Piéton')
        df_usager['catu'] = df_usager['catu'].replace(4, 'Piéton en roller ou en trottinette')

    @staticmethod
    def replace_accident_severity(df_usager):
        df_usager['grav'] = df_usager['grav'].replace(1, 'Indemne')
        df_usager['grav'] = df_usager['grav'].replace(2, 'Tué')
        df_usager['grav'] = df_usager['grav'].replace(3, 'Blessé hospitalisé')
        df_usager['grav'] = df_usager['grav'].replace(4, 'Blessé léger')

    @staticmethod
    def replace_gender(df_usager):
        df_usager['sexe'] = df_usager['sexe'].replace(1, 'Masculin')
        df_usager['sexe'] = df_usager['sexe'].replace(2, 'Féminin')

    @staticmethod
    def replace_journey(df_usager):
        df_usager['trajet'] = df_usager['trajet'].replace(1, 'Domicile – travail')
        df_usager['trajet'] = df_usager['trajet'].replace(2, 'Domicile – école')
        df_usager['trajet'] = df_usager['trajet'].replace(3, 'Courses – achats')
        df_usager['trajet'] = df_usager['trajet'].replace(4, 'Utilisation professionnelle')
        df_usager['trajet'] = df_usager['trajet'].replace(5, 'Promenade – loisirs')
        df_usager['trajet'] = df_usager['trajet'].replace(9, 'Autre')

    @staticmethod
    def replace_localisation(df_usager):
        df_usager['locp'] = df_usager['locp'].replace(1, 'Sur chaussée : A + 50 m du passage piéton')
        df_usager['locp'] = df_usager['locp'].replace(2, 'Sur chaussée : A – 50 m du passage piéton')
        df_usager['locp'] = df_usager['locp'].replace(3, 'Sur passage piéton : Sans signalisation lumineuse')
        df_usager['locp'] = df_usager['locp'].replace(4, 'Sur passage piéton : Avec signalisation lumineuse')
        df_usager['locp'] = df_usager['locp'].replace(5, 'Sur trottoir')
        df_usager['locp'] = df_usager['locp'].replace(6, 'Sur accotement')
        df_usager['locp'] = df_usager['locp'].replace(7, 'Sur refuge ou BAU')
        df_usager['locp'] = df_usager['locp'].replace(8, 'Sur contre allée')

    @staticmethod
    def replace_pedestrian_action(df_usager):
        df_usager['actp'] = df_usager['actp'].replace(0, 'Se déplaçant: non renseigné ou sans objet')
        df_usager['actp'] = df_usager['actp'].replace(1, 'Se déplaçant: Sens véhicule heurtant')
        df_usager['actp'] = df_usager['actp'].replace(2, 'Se déplaçant: Sens inverse du véhicule')
        df_usager['actp'] = df_usager['actp'].replace(3, 'Traversant')
        df_usager['actp'] = df_usager['actp'].replace(4, 'Masqué')
        df_usager['actp'] = df_usager['actp'].replace(5, 'Jouant – courant')
        df_usager['actp'] = df_usager['actp'].replace(6, 'Avec animal')
        df_usager['actp'] = df_usager['actp'].replace(9, 'Autre')

    @staticmethod
    def replace_pedestrian_alone_or_not(df_usager):
        df_usager['etatp'] = df_usager['etatp'].replace(1, 'Seul')
        df_usager['etatp'] = df_usager['etatp'].replace(2, 'Accompagné')
        df_usager['etatp'] = df_usager['etatp'].replace(3, 'En groupe')

    @staticmethod
    def replace_road_category(df_location):
        df_location['catr'] = df_location['catr'].replace(1, 'Autoroute')
        df_location['catr'] = df_location['catr'].replace(2, 'Route Nationale')
        df_location['catr'] = df_location['catr'].replace(3, 'Route Départementale')
        df_location['catr'] = df_location['catr'].replace(4, 'Voie Communale')
        df_location['catr'] = df_location['catr'].replace(5, 'Hors réseau public')
        df_location['catr'] = df_location['catr'].replace(6, 'Parc de stationnement ouvert à la circulation publique')
        df_location['catr'] = df_location['catr'].replace(9, 'autre')

    @staticmethod
    def replace_traffic_regime(df_location):
        df_location['circ'] = df_location['circ'].replace(1, 'A sens unique')
        df_location['circ'] = df_location['circ'].replace(2, 'Bidirectionnelle')
        df_location['circ'] = df_location['circ'].replace(3, 'A chaussées séparées')
        df_location['circ'] = df_location['circ'].replace(4, 'Avec voies d’affectation variable')

    @staticmethod
    def replace_existence_reserved_lane(df_location):
        df_location['vosp'] = df_location['vosp'].replace(1, 'Piste cyclable')
        df_location['vosp'] = df_location['vosp'].replace(2, 'Banque cyclable')
        df_location['vosp'] = df_location['vosp'].replace(3, 'Voie réservée')

    @staticmethod
    def replace_road_gradient(df_location):
        df_location['prof'] = df_location['prof'].replace(1, 'Plat')
        df_location['prof'] = df_location['prof'].replace(2, 'Pente')
        df_location['prof'] = df_location['prof'].replace(3, 'Sommet de côte')
        df_location['prof'] = df_location['prof'].replace(4, 'Bas de côte')

    @staticmethod
    def replace_plan_layout(df_location):
        df_location['plan'] = df_location['plan'].replace(1, 'Partie rectiligne')
        df_location['plan'] = df_location['plan'].replace(2, 'En courbe à gauche')
        df_location['plan'] = df_location['plan'].replace(3, 'En courbe à droite')
        df_location['plan'] = df_location['plan'].replace(4, 'En « S »')

    @staticmethod
    def replace_surface(df_location):
        df_location['surf'] = df_location['surf'].replace(1, 'normale')
        df_location['surf'] = df_location['surf'].replace(2, 'mouillée')
        df_location['surf'] = df_location['surf'].replace(3, 'flaques')
        df_location['surf'] = df_location['surf'].replace(4, 'inondée')
        df_location['surf'] = df_location['surf'].replace(5, 'enneigée')
        df_location['surf'] = df_location['surf'].replace(6, 'boue')
        df_location['surf'] = df_location['surf'].replace(7, 'verglacée')
        df_location['surf'] = df_location['surf'].replace(8, 'corps gras - huile')
        df_location['surf'] = df_location['surf'].replace(9, 'autre')

    @staticmethod
    def replace_development_infrastructure(df_location):
        df_location['infra'] = df_location['infra'].replace(1, 'Souterrain - tunnel')
        df_location['infra'] = df_location['infra'].replace(2, 'Pont - autopont')
        df_location['infra'] = df_location['infra'].replace(3, 'Bretelle d’échangeur ou de raccordement')
        df_location['infra'] = df_location['infra'].replace(4, 'Voie ferrée')
        df_location['infra'] = df_location['infra'].replace(5, 'Carrefour aménagé')
        df_location['infra'] = df_location['infra'].replace(6, 'Zone piétonne')
        df_location['infra'] = df_location['infra'].replace(7, 'Zone de péage')

    @staticmethod
    def replace_accident_situation(df_location):
        df_location['situ'] = df_location['situ'].replace(1, 'Sur chaussée')
        df_location['situ'] = df_location['situ'].replace(2, "Sur bande d’arrêt d’urgence")
        df_location['situ'] = df_location['situ'].replace(3, 'Sur accotement')
        df_location['situ'] = df_location['situ'].replace(4, 'Sur trottoir')
        df_location['situ'] = df_location['situ'].replace(5, 'Sur piste cyclable')
