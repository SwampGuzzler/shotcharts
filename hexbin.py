import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from IPython.display import display
from matplotlib.patches import Circle, Rectangle, Arc
from alpha import draw_court



shot_chart_url = 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPARAMS=2014-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=101108&PlusMinus=N&Position=&Rank=N&RookieYear=&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=East&VsDivision=&mode=Advanced&showDetails=0&showShots=1&showZones=0'

pd.set_option('display.width', 200)

response = requests.get(shot_chart_url)
headers = response.json()['resultSets'][0]['headers']
shots = response.json()['resultSets'][0]['rowSet']
 
shot_df = pd.DataFrame(shots, columns=headers)

sns.set_style("white")
sns.set_color_codes()

# matplotlib.pyplot.hexbin(x, y, C=None, gridsize=100, bins=None, xscale=u'linear', yscale=u'linear', extent=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=u'none', reduce_C_function=<function mean at 0x7f177f68a140>, mincnt=None, marginals=False, hold=None, **kwargs)
# matplotlib.pyplot.scatter(x, y, s=20, c=u'b', marker=u'o', cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, hold=None, **kwargs)

plt.figure(figsize=(6,5.5))
plt.hexbin(shot_df.LOC_X, shot_df.LOC_Y, gridsize=[20,7])


draw_court(outer_lines=True)
# plt.axis('off')
plt.xlim(-300,300)
plt.ylim(-100,500)
plt.show()

