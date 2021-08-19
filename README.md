# High School Recruits in the NBA - Exploratory Data Analysis
---
### Background
* NBA scouts, team managers, and fans are always on the lookout for the next big star in the league. While it's sometimes clear when a young NBA phenom is on this kind of trajectory, it's not always obvious and often misleading when trying to predict the careers of high school basketball prospects, as they're still early in their development as players and as people. This analysis explores some trends in the careers of these players, specifically how their high school ranking, college, and other attributes are related to their performance as a professional.
---
## Usage
* The full notebook for this project should be accessed through a jupyter notebook viewer, found [here](https://nbviewer.jupyter.org/github/j-s-russell/High-School-Recruits-in-NBA---EDA/blob/main/NBA_RECRUITS_PROJECT.ipynb).
---
## Data
* The dataset includes data from high school basketball players and their stats in the NBA. The high school player data was scraped from the ESPN 100 Basketball Recruiting website, which includes each player's class rank, as well as their height, weight, position, hometown, and overall player grade for all top 100 recruits from 2007 to 2017. The NBA data was gathered from the nba_api client package provided by Swar Patel, found [here](https://github.com/swar/nba_api). 
---
## Prospects in High School
### High School and Home State
* The first main step in their basketball career is high school competition. Below are some of the most popular schools for recruits:
![](/images/img1.png)
* While the majority of high school teams are based around local players, some prep schools are known for consistently recruiting top prospects from around the country to provide the kind of resources and training to college and professional competition.
* What areas produce the most prospects? The map below represents the distribution of top prospects throughout the country. For simplicity, it only includes American prospects:
![](/images/img2.png)
* Unsurprisingly, the two most populous states in the U.S., California and Texas, have the largest number of recruits. For other states, however, the East Coast and South are dominant. Georgia and Florida both are highly productive, as well as Illinois.
### College
* As most players' last step before turning professional, college can greatly assist or offset their career trajectory. Certain colleges, such as Kentucky and Duke, are highly focused on developing high-level players for the NBA, while others are more focused on the college game and developing four-year players.

![](/images/img3.png)
![](/images/img4.png)
* Kentucky and Duke are clear leaders as destinations for top recruits. As their programs specialize in developing players who will only play in college for a year or two, most incoming prospects will get immediate playing time with other high-level recruits and working with coaches who have experience with some of the most successful NBA players. 
* Let's take a look at player positions over time:

![](/images/img5.png)
* While guards and forwards seem to be fairly balanced, the center position is consistently underrepresented among top 100 recruits. The late 2000s and 2010s have seen drastic changes in the NBA game, with traditional low-block centers becoming increasingly uncommon in favor of more ball handlers and three point shooters. Additionally, while American high schools produce some of the best guards and forwards in the game today, many of the top NBA centers come from overseas, such as Nikola Jokic, Rudy Gobert, Domantas Sabonis and Nikola Vucevic.
---
## Prospects in the NBA
### The Impact of College Programs
* In order to evaluate a player's NBA career success, this analysis uses a modified version of Game Score, which is a statistic created by John Hollinger as an estimation of a player's overall statistical performance, averaged for all NBA games they've played. The chart below shows the average Game Scores of NBA players by their college:
![](/images/img6.png)
* Kentucky's dominance is further emphasized here, as the efficiency of its alumni outclasses that of nearly every other college. Texas players hold the highest average Game Score, but with only 6 recruits, this is less significant. Powerhouse universities Duke, UCLA, and Kansas also show consistent NBA success.
![](/images/img7.png)
* Another important metric to consider for each college is the percentage of recruits who actually played in the NBA. Although the Texas alumni who played in the NBA were much more successful on average, Texas players have the lowest odds of making the league out of the major colleges. Additionally, while recent North Carolina players have not seen major success in the NBA, UNC is one of the most productive universities in sending college players to the pros.
### Other NBA Productivity Factors?
![](/images/img8.png)
* words
![](/images/img9.png)
* more words!
