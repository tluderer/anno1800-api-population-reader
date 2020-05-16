import json

class Population:
    """ DAO that holds the current population of Anno 1800.
    """
    def __init__(self,
     num_farmers=0, num_workers=0, num_artisans=0, num_engineers=0, num_investors=0,
     num_jornaleros=0, num_obreros=0
    ):
        """ Create a new population object from given population.
        """
        self.farmers = num_farmers
        self.workers = num_workers
        self.artisans = num_artisans
        self.engineers = num_engineers
        self.investors = num_investors

        self.jornaleros = num_jornaleros
        self.obreros = num_obreros


    def to_dict(self):
        """ Convert this object to a dictionary
        @returns dict: A dictonary representing the values of this object.
        """
        return {
            'farmers': self.farmers,
            'workers': self.workers,
            'artisans': self.artisans,
            'engineers': self.engineers,
            'investors': self.investors,

            'jornaleros': self.jornaleros,
            'obreros': self.obreros,
        }

    def json(self):
        """ Serialize this object to JSON string.
        @returns string : The JSON representation of this object.
        """
        return json.dumps(self.to_dict())
