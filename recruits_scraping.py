from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd


def get_recruits(URL):
    """ Returns a dataframe of an ESPN recruiting class """
    
    # Load ESPN rankings

    class_response = requests.get(URL)
    class_rankings = class_response.content

    soup = BeautifulSoup(class_rankings, "html.parser")


    # Get list of players and their attributes

    stat_list = []
    all_stats = soup.find_all("td")
    for stat in all_stats:
        stat_list.append(stat.get_text())
    stats = stat_list[9:]
    classyear = soup.find_all("h2")[2].get_text()

    rank = []
    name = []
    position = []
    hometown = []
    homestate = []
    highschool = []
    grade = []
    height = []
    weight = []
    college = []
    rec_class = []
    test = []
    
    # Not all classes have data for 100 recruits, so we take the top 99
    for i in range(99):
        rank.append(stats[9*i])
        name.append(stats[9*i+1].split("Video")[0])
        position.append(stats[9*i+2])
        home_info = stats[9*i+3]
        foreign_states = ['EU', 'Se', 'SP', 'Fr', 'On', 'N.', 'MB', 'Qu']
        if home_info.split(",")[1][1:3] in foreign_states:
            hometown.append(home_info.split(",")[0])
            homestate.append(home_info.split(", ")[1])
            highschool.append(home_info.split(",")[1][3:])
        else:
            hometown.append(home_info.split(",")[0])
            homestate.append(home_info.split(",")[1][1:3])
            highschool.append(home_info.split(",")[1][3:])
        grade.append(stats[9*i+7][:2])
        height.append(stats[9*i+4])
        weight.append(stats[9*i+5])
        rec_class.append(str(classyear).split(" ")[0])
        if "Committed" in stats[9*i+8]:
            college.append(stats[9*i+8].split("Committed")[0])
        elif "Signed" in stats[9*i+8]:
            college.append(stats[9*i+8].split("Signed")[0])
        else:
            college.append("Undeclared")

    height_inches = [(int(ht[0]) * 12) + int(ht.split("'")[1]) for ht in height]

    player_links = soup.find_all("a")
    links = []
    for a in player_links:
        links.append(a["href"])
    links_list = []
    for link in links:
        if "rankings" not in link and "videos" not in link and \
        "evaluation" not in link and "class" not in link and \
        link not in links_list:
            links_list.append(link)
    links = links_list[:99]

    # Create dataframe
    stats_dic = {"Rank": rank, "Name": name, "Position": position, \
                 "Town": hometown, "State": homestate, "Grade": grade,\
                 "School": highschool, "Height": height, \
                 "Height_Inches": height_inches, "Weight": weight, \
                 "College": college, "Link": links, "Class": rec_class}

    recruiting_class = pd.DataFrame(stats_dic)
    
    return recruiting_class


# Recruiting class links

link2007recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2007/order/true"
link2008recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2008/order/true"
link2009recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2009/order/true"
link2010recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2010/order/true"
link2011recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2011/order/true"
link2012recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2012/order/true"
link2013recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2013/order/true"
link2014recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2014/order/true"
link2015recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2015/order/true"
link2016recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2016/order/true"
link2017recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2017/order/true"
link2018recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2018/order/true"
link2019recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2019/order/true"
link2020recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2020/order/true"
link2021recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/class/2021/order/true"
link2022recruits = "http://www.espn.com/college-sports/basketball/recruiting/playerrankings/_/order/true"



# Recruiting class dataframes

class2007 = get_recruits(link2007recruits)
class2008 = get_recruits(link2008recruits)
class2009 = get_recruits(link2009recruits)
class2010 = get_recruits(link2010recruits)
class2011 = get_recruits(link2011recruits)
class2012 = get_recruits(link2012recruits)
class2013 = get_recruits(link2013recruits)
class2014 = get_recruits(link2014recruits)
class2015 = get_recruits(link2015recruits)
class2016 = get_recruits(link2016recruits)
class2017 = get_recruits(link2017recruits)
class2018 = get_recruits(link2018recruits)
class2019 = get_recruits(link2019recruits)
class2020 = get_recruits(link2020recruits)
class2021 = get_recruits(link2021recruits)
class2022 = get_recruits(link2022recruits)


# Create full dataset

classes = [class2007, class2008, class2009, class2010, class2011, \
           class2012, class2013, class2014, class2015, class2016, \
           class2017, class2018, class2019, class2020, class2021, class2022]

recruits = pd.concat(classes).reset_index(drop=True)
recruits.to_csv("recruiting_classes.csv")


