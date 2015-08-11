import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from IPython.display import display

# inital stats Query player == Chris Paul
# shot_chart_url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPAR'\
#                 'AMS=2014-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&D'\
#                 'ateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Loca'\
#                 'tion=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&'\
#                 'PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=101108&Plu'\
#                 'sMinus=N&Position=&Rank=N&RookieYear=&Season=2014-15&Seas'\
#                 'onSegment=&SeasonType=Regular+Season&TeamID=0&VsConferenc'\
#                 'e=&VsDivision=&mode=Advanced&showDetails=0&showShots=1&sh'\
#                 'owZones=0'



shot_chart_url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPARAMS=2014-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=101108&PlusMinus=N&Position=&Rank=N&RookieYear=&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=East&VsDivision=&mode=Advanced&showDetails=0&showShots=1&showZones=0'

# Set the pandas display frame wider so we can see more of the table
pd.set_option('display.width', 200)

# Hit the public API w/ this query string
response = requests.get(shot_chart_url)
# Grab the headers to be used as column headers for our DataFrame
headers = response.json()['resultSets'][0]['headers']
# Grab the shot chart data
shots = response.json()['resultSets'][0]['rowSet']

print headers

#Create the data frame we'll use 
shot_df = pd.DataFrame(shots, columns=headers)


# Print out the first 5 field goals attempted
with pd.option_context('display.max_columns', None):
    display(shot_df.head())

# open up a python image where we chart the location of each shot based of their x/y values from the LOC_Y & LOC_X fields
sns.set_style("white")
sns.set_color_codes()
plt.figure(figsize=(6,5.5)) # w,h in inches
# plt.set_tight_layout(True)
plt.scatter(shot_df.LOC_X, shot_df.LOC_Y)
plt.show()

