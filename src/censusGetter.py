import requests
import censusdata
from us import states



education = censusdata.download('acs5', 2019, censusdata.censusgeo([('county', '*')]),
                                   ['B15003_025E', 'B15003_024E', 'B15003_023E', 'B15003_022E', 'B15003_001E'])
education = education.rename(columns={'B15003_001E': 'population_size', 'B15003_022E': 'bachelors_degree', 'B15003_023E': 'masters_degree', 
                                    'B15003_024E': 'professional_school_degree', 'B15003_025E': 'doctorate_degree ',   })

censusdata.exportcsv('./extracts/education.csv', education)

