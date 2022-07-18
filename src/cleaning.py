import re

# create a new dataframe with the percent of missing values by column
def missing(data):
    temp = data[0:0]
    for i in data:
        temp.at['percent', i] = round(data[i].isnull().sum()/(data[i].count().sum()+data[i].isnull().sum())*100, 2)
    return temp.T

# The following function would not be useful in more than one scenario, and was not included in the final paper
# return the count of each country value in a dataframe
def value_count(data):
    temp = data[0:0]
    for i in data['Country']:
        temp.at['count', i.value_counts()] = data['Country'][i].value_counts()
    temp.T
    return temp.T

# delete data which includes ocean, /, or ? 
def rmv_ocean(data):
    if re.search("(ocean|\/|\?|sea)", str(data)):
        return ""
    else:
        return data
    