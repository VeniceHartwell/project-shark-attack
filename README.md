# Cultural influence on Shark Attacks, Globally

## Contents:
1. Abstract
2. Setup
3. Hypothesis Development
4. Data Filtering
5. Dataframe creation
6. Visualization
7. Conclusion
8. References

## 1. Abstract
Geert Hofstede has developed an index of cultural insights which demonstrate a country's varying levels of indulgence, individualism, uncertainty avoidance, risk aversion, etc. One might expect a country with a high level of risk aversion to engage less in dangerous activities like swimming in shark-infested waters. This paper will prove or disprove whether there is a correlation between the two data sets. Shark attack data in this paper comes from Kaggle, a free online resource, and has poor readability – it is difficult data to work with. The Kaggle data provided includes over 6,300 unique shark attacks ranging from eater sports to accidents. Geert Hofstede is a well-funded company and so their data is easy to work with. 

## 2. Setup
- Import libraries
- first visualization of data

## 3. Hypothesis development
Is there a correlation between a country's individualism or uncertainty avoidance score and the number of shark attacks in the area?

## 4. Data filtering
Clean the data using regex and pandas dataframes.

## 5. Dataframe creation
### Countries Under Attack
A clean and concise dataset is necessary to properly visualize the number of shark attacks in a given country.

### Per Capita
Given the variance in country size, there were several options to balance the curve of shark attacks: KM of coastline, number of surfers, or population size. Population size proved to have the most complete dataset. 

### Cultural Insights 
Import a list of cultural insights from Geert Hofstede's Country Comparison tool.

## 6. Visualization
Charts include the original dataset. All figures are listed below:
1. Original Dataset
2. Cleanup: Missing Values (before)
3. Cleanup: Missing Values (after)
4. Shark Attack Frequency by Country
5. Shark Attack Frequency by Country (per capita)
6. Geert Hofstede Insights by Country
7. Comparison: Shark Attacks vs Country Insights

## 7. Conclusion
### Hypothesis Disproven
There is not a correlation between a country's individualism or even uncertainty avoidance and the number of shark attacks in the area.
The correlation between the data can almost be seen because America has the highest of these scores with the most shark attacks, but South Africa skews the data with a lower score and a relatively large number of attacks.

### Knowledge Gained
The purpose of this paper was to test my knowledge as a Data Analyst, which I have succeeded in. I have built deeper understandings of the tools I am working with and developed new techniques and code to use in future projects. Some of the libraries and skills I applied here are:
- Python
- regex
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Business Communications

In the future I am looking forwar dto learning how to use web scraping to pull source code data fro mwebsites like Geert Hofstede's country comparison tool, an interactive tool that I could not copy+paste into my project.

## 8. References
- Kaggle
- Geert Hofstede
- Stack Overflow