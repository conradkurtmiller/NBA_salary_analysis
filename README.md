Analyzing NBA '21-'22 salaries using advanced stats: Project overview
======

+ Created a linear regression formula to estimate salary in the current market based off advanced stats and metrics

+ Scraped statistics and salary data from basketball-reference using Python and Beautiful Soup

+ Used exploratory data analysis tools to identify relationships

As a lifelong basketball fan, I've always been curious as to how NBA players value is truly assessed. It is obviously a league driven by superstars, and the huge salaries that come along with being one of those stars. The emergence of advanced analytics in the NBA for the past 2 to 3 decades has also been huge for tons of serious fans (and some casual) to gain further insights to a players true impact on the court. Most conversations surrounding the NBA MVP race, and player evaluation as a whole, use stats like player efficiency rating(PER), value over replacement player(VORP), true shooting percentages(TS%), usage percentages(USG%), etc etc. 

__In this project, I aim to see how accurately we can estimate how players (especially "role players") are paid in the NBA using these advanced metrics.__

Code and resources used
------

+ __Python 3.7__

+ __Packages:__ urllib, bs4, pandas, numpy, seaborn, statsmodels, matplotlib

+ __Data:__ https://www.basketball-reference.com/

Web Scraping
------

Created a beautiful soup table scraper that utilized the urllib.urlopen function to pull all advanced stats and salaries from our data source online.

Data Cleaning
------

After pulling our data, I merged the two dataframes together, dropped unnecesary variables, dropped duplicated information, parsed salary information, and converted all numeric variables to workable data types. There were some issues with how the tables were formatted on their website, and it is commented in the code. I had to manually format the second dataframe for further analysis.

EDA
------

I ran analysis on the _full data set_(including all players currently in the NBA with available salary data), noticing a decent amount of colinearity for certain advanced statistics and how they affected players salaries. Here are some highlights on the total data set.

_I created a correlation heatmap to view the correlation of salary (represented by 'sal') and advanced stats_
![alt text](https://github.com/conradkurtmiller/NBA_salary_analysis/blob/main/hm2.png)

_I created pairplots to view colinearity between salary and certain advanced stats_
![alt text](https://github.com/conradkurtmiller/NBA_salary_analysis/blob/main/pairplots_pervorp.png)

As you can see, there's some notable colinearity between salary and stats like Player Efficiency Rating(PER), Offensive Box Plus/Minus(OBPM), Value over replacement player(VORP), Minutes per game(MPG), Usage percentage (USG), and a players age. 

__*As I explored the data further,*__ I wanted to isolate the NBA's role players. (Role players being non-star players, often with a higher variance in salary, and high variance in overall impact, while usually playing ~25 minutes or less a game.) With salaries for role players being somewhat unpredictable every time the free agency period comes around, I think these are even more interesting to dissect. Below are the same correlation plots ran on the isolated data set. Once I had taken out the stars and starters from the data, you can see the relationship on salary is much less correlated on these advanced metrics. 

![alt text](https://github.com/conradkurtmiller/NBA_salary_analysis/blob/main/hm1.png)
![alt text](https://github.com/conradkurtmiller/NBA_salary_analysis/blob/main/pairplots_pervorp2.png)


Model Building
------

I built a couple of models based on this data and its correlation. I quickly recognized that this dataset is quite small, and with multiple stats having somewhat colinear correlation, it would best benefit from a linear regression. I was able to create a formula that ended up with an R-squared value of 0.580, and the formula is as follows

<h3 align="center"> Player salary = -17792054 + 261874(MPG) -224237(PER) + 2724038(VORP) + 440007(USG) + 529313(OBPM) + 557604(Age) </h3>

However, when I attempted to draw up a formula to estimate role players' salaries, the highest R-squared value I could return was 0.243

Conclusions
======

My conclusion from this analysis is somewhat gratifying as well as frustrating.

The NBA being a star driven league plays a huge part in how a player is paid. Different market sizes of different organizations, attempting to hold on to talent in certain roles, past performance, perceived potentional, and traditional stats all play a huge role in how players (and their agents) negotiate their contracts. Advanced metrics in the NBA have been used to try to equalize a player's stats across positions and roles on the floor. They are also the number 1 thing that Nikola Jokic fans love to brag about on twitter. While I think they are extremely useful in the modern nba to help steer a teams strategy and explain a players impact on a game, I've identified from my analysis that there's obviously much more needed than advanced metrics to identify a player's value in the current market. 



