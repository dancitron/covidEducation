import pandas as pd

coronaDF = pd.read_csv('../extracts/coronaCases.csv')
educationDF = pd.read_csv('../extracts/education.csv')

#educationDF['county']=educationDF['county'].astype(object)

df = pd.merge(coronaDF, educationDF, left_on=['county' ], right_on=['NAME'], how='inner' )

df =  df.drop(['country_code', 'Unnamed: 0', "country_population", 'id'], axis=1)

df['percentCases'] = df['latest.confirmed']/df['population_size']

df['percentDeath'] = df['latest.deaths']/df['population_size']


df['underBach'] = df['population_size'] - (df['Bachelors degree'] + df['Masters degree'] + df['Professional school degree'] + df['Doctorate degree '])

df['underBachPercentage'] = df['underBach'] / df['population_size']


df['bachAndAbove'] = (df['Bachelors degree'] + df['Masters degree'] + df['Professional school degree'] + df['Doctorate degree '])

df['bachAndAbovePercentage'] = df['bachAndAbove'] / df['population_size']


df['postBach'] = (df['Masters degree'] + df['Professional school degree'] + df['Doctorate degree '])

df['postBachPercentage'] = df['postBach'] / df['population_size']



df.to_csv('../extracts/mergedExtract.csv')
