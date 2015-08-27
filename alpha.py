import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from IPython.display import display
from matplotlib.patches import Circle, Rectangle, Arc

def draw_court(ax=None, color='black', lw=2, outer_lines=False):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    # Create the various parts of an NBA basketball court

    # Create the basketball hoop
    # Diameter of a hoop is 18" so it has a radius of 9", which is a value
    # 7.5 in our coordinate system
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)

    # Create backboard
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)

    # The paint
    # Create the outer box 0f the paint, width=16ft, height=19ft
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                          fill=False)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                          fill=False)

    # Create free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                         linewidth=lw, color=color, fill=False)
    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')
    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                     color=color)

    # Three point line
    # Create the side 3pt lines, they are 14ft long before they begin to arc
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
                               color=color)
    corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    # I just played around with the theta values until they lined up with the 
    # threes
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                    color=color)

    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                           linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                           linewidth=lw, color=color)

    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc]

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                color=color, fill=False)
        court_elements.append(outer_lines)

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    return ax


# [u'GRID_TYPE', u'GAME_ID', u'GAME_EVENT_ID', u'PLAYER_ID', u'PLAYER_NAME', u'TEAM_ID', u'TEAM_NAME', u'PERIOD', u'MINUTES_REMAINING', u'SECONDS_REMAINING', u'EVENT_TYPE', u'ACTION_TYPE', u'SHOT_TYPE', u'SHOT_ZONE_BASIC', u'SHOT_ZONE_AREA', u'SHOT_ZONE_RANGE', u'SHOT_DISTANCE', u'LOC_X', u'LOC_Y', u'SHOT_ATTEMPTED_FLAG', u'SHOT_MADE_FLAG']
# [u'Shot Chart Detail', u'0021400154', 222, 101108, u'Chris Paul', 1610612746, u'Los Angeles Clippers', 2, 4, 26, u'Made Shot', u'Pullup Jump shot', u'2PT Field Goal', u'Mid-Range', u'Left Side Center(LC)', u'16-24 ft.', 16, -87, 138, 1, 1]

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
if __name__ == '__main__':

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

	

	# matplotlib.pyplot.hexbin(x, y, C=None, gridsize=100, bins=None, xscale=u'linear', yscale=u'linear', extent=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, edgecolors=u'none', reduce_C_function=<function mean at 0x7f177f68a140>, mincnt=None, marginals=False, hold=None, **kwargs)
	# matplotlib.pyplot.scatter(x, y, s=20, c=u'b', marker=u'o', cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, hold=None, **kwargs)

	# plt.figure(figsize=(6,5.5))
	# # plt.hexbin(shot_df.LOC_X, shot_df.LOC_Y, gridsize=[20,7])
	# # plt.scatter(shot_df.LOC_X, shot_df.LOC_Y)

	# draw_court(outer_lines=True)
	# plt.axis('off')
	# plt.xlim(-300,300)
	# plt.ylim(-100,500)
	# plt.show()

def cp3_url():
	return 'http://stats.nba.com/stats/shotchartdetail?CFID=33&CFPARAMS=2014-15&ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerID=101108&PlusMinus=N&Position=&Rank=N&RookieYear=&Season=2014-15&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&VsConference=East&VsDivision=&mode=Advanced&showDetails=0&showShots=1&showZones=0'




