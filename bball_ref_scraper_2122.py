## Webscraping 21-22 season data from basketball-reference.com to analyze
## further for this project, using advanced statistics and salary data.


# import packages used
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

## Normally here I would define a function to pass in the url and pull data,
## however, the formatting of tables on the site we're scraping from can be 
## inconsistent, and we're only looking to pull 2 dataframes.

# url to scrape for advanced stats
url = "https://www.basketball-reference.com/leagues/NBA_2022_advanced.html"

# collect HTML data
html = urlopen(url)
        
# create beautiful soup object from HTML
soup = BeautifulSoup(html, features="lxml")

# using getText()to extract the headers into a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
headers = headers[1:]

# get rows from table
rows = soup.findAll('tr')[2:]
rows_data = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]

# creating data frame
df = pd.DataFrame(rows_data, columns = headers)

# url to scrape for salary info
url2 = "https://www.basketball-reference.com/contracts/players.html"

# collect HTML data
html2 = urlopen(url2)

# create beautiful soup object from HTML
soup2 = BeautifulSoup(html2, features="lxml")

# using getText() to extract the headers into a list
headers2 = [th.getText() for th in soup2.findAll('tr', limit=2)[0]
                 .findAll('th')]
headers2 = headers2

# get rows from table
rows2 = soup2.findAll('tr')
rows_data2 = [[td.getText() for td in rows2[i].findAll('td')]
                  for i in range(len(rows2))]

# creating 2nd data frame and merging
# note, the inconsistency of the tables on the site, causing me to have to 
# label the individual columns
df2 = pd.DataFrame(rows_data2, columns = ['Player', 'Tm', '22','23','24','25',
                                           '26','27','',''])
df_adv_sal = pd.merge(df, df2, on=['Player'])

# data cleaning and preparation for exploratory analysis
df_adv_sal = df_adv_sal.drop(columns=['23','24','25','26','27','',''])
df_adv_sal = df_adv_sal.replace(r'^\s*$', np.nan, regex=True)
df_adv_sal.dropna(axis=0, how='all', inplace=True)
adv_sal = df_adv_sal.drop_duplicates(subset=['Player','G'])
adv_sal.dropna(axis=1, how='all', inplace=True)
adv_sal = adv_sal.drop(columns = 'Tm_y')
adv_sal = adv_sal[pd.notnull(adv_sal['22'])]
adv_sal[adv_sal.columns[-1:]] = adv_sal[adv_sal.columns[-1:]].replace('[\$,]', 
                                    '', regex=True).astype(int)
adv_sal[['Age', 'G' ,'MP', 'PER', 'TS%', '3PAr','FTr', 'ORB%', 'DRB%', 'TRB%', 
         'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 
         'OBPM', 'DBPM', 'BPM', 'VORP']] = (
             adv_sal[['Age', 'G' ,'MP', 'PER', 'TS%', '3PAr','FTr', 'ORB%', 
                      'DRB%', 'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 
                      'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP'
                      ]].astype(float))

# export dataframe to a CSV 
adv_sal.to_csv("nba_2122_stats.csv", index=False)


