import json
from pygal.maps.world import World
from country_codes import get_country_codes



#Load the data into lists.
filename = 'Resources\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
#Build a dictionairy of population data.
cc_populations = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_codes(country_name)
        if code:
            cc_populations[code] = population

wm = World()
wm.title = "World Ppopulation in 2010, by Country"
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')

