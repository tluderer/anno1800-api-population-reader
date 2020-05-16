from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from population import Population

app = Flask(__name__)
api = Api(app)

POPULATION = Population()


# Populations
# REST route: Shows a list of all endpoints of the REST API
class Help(Resource):
    def get(self):
        return {
            'GET endpoints': [
                '/populations'
                '/farmers', '/workers', '/artisans', '/engineers', '/investors',
                '/jornaleros', '/obreros'
            ]
        }



# Populations
# REST route: Shows all populations in JSON object
class Populations(Resource):
    def get(self):
        return { "populations": POPULATION.to_dict() }


# Population Details
# REST route: Shows a single value, the number of population
class PopulationDetails(Resource):
    def get(self, population_name):
        # Old world
        if population_name == "farmers":
            return { "farmers": POPULATION.farmers }
        elif population_name == "workers":
            return { "workers": POPULATION.workers }
        elif population_name == "artisans":
            return { "artisans": POPULATION.artisans }
        elif population_name == "engineers":
            return { "engineers": POPULATION.engineers }
        elif population_name == "investors":
            return { "investors": POPULATION.investors }

        # New world
        elif population_name == "jornaleros":
            return { "jornaleros": POPULATION.jornaleros }
        elif population_name == "obreros":
            return { "obreros": POPULATION.obreros }
        
        # 404 Error: Route not found
        else:
            abort(404, message='Population "{}" does not exist'.format(population_name))

##
## Actually setup the Api resource routing here
##
api.add_resource(Help, '/')
api.add_resource(Populations, '/populations')
api.add_resource(PopulationDetails, '/population/<population_name>')


if __name__ == '__main__':
    app.run(debug=True)

