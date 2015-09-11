import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mpld3
from mpld3 import plugins


import requests
import seaborn as sns

from IPython.display import display
import urllib
from matplotlib.patches import Circle, Rectangle, Arc
from matplotlib.offsetbox import  OffsetImage
from alpha import draw_court
from alpha import cp3_url

# Define some CSS to control our custom labels
css = """
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""


shot_chart_url = cp3_url()

# pd.set_option('display.width', 200)

response = requests.get(shot_chart_url)
headers = response.json()['resultSets'][0]['headers']
shots = response.json()['resultSets'][0]['rowSet']
 
shot_df = pd.DataFrame(shots, columns=headers)

sns.set_style("white")
sns.set_color_codes()
# sns.despine(left=True)

pic = urllib.urlretrieve("http://stats.nba.com/media/players/230x185/101108.png", "101108.png")
paul_pic = plt.imread(pic[0])

img = OffsetImage(paul_pic, zoom=0.6)
img.set_offset((400,350))
cmap=plt.cm.gist_heat_r

# joint_shot_chart = sns.jointplot(shot_df.LOC_X, shot_df.LOC_Y, size=7.5, stat_func=None,
#                                  kind='hex', space=0, gridsize=[20,6], color=cmap(.2), cmap=cmap)

# joint_shot_chart = plt.scatter(shot_df.LOC_X, shot_df.LOC_Y)

# ax = joint_shot_chart.ax_joint

# ax.set_xlim(-250,250)
# ax.set_ylim(422.5, -47.5)

# # Get rid of axis labels and tick marks
# ax.set_xlabel('')
# ax.set_ylabel('')
# ax.tick_params(labelbottom='off', labelleft='off')
draw_court()
# ax.set_title('Chris Paul FGA \n2014-15 Reg. Season', 
#              y=0.75, fontsize=18)
# ax.add_artist(img)

# plt.axis('off')
# plt.xlim(-300,300)
# plt.ylim(-100,500)

x = []
for i in shots:
  if i[20] == 0:
    x.append('b')
  else:
    x.append('r')

bools = np.array(x)


fig, ax = plt.subplots()
points = ax.plot(shot_df.LOC_X, shot_df.LOC_Y, 'o', color=x,
                 mec='k', ms=15, mew=1, alpha=.6)

# points = ax.plot(shot_df.LOC_X, shot_df.LOC_Y, 'o', color=[timeDiffInt[a] for a in timeDiffInt],
#                  mec='k', ms=15, mew=1, alpha=.6)
# ax.grid(True, alpha=0.3)

labels = []
for i in shots:
	label = str(i[10]) + i[10]
	label = ''
	if i[20] == 1:
		label = label + 'Made '
	else :
		label = label + 'Missed '

	label = label + str(i[11]) + ' from ' + str(i[16]) + ' feet'
	labels.append(label)   


# N = 50
# df = pd.DataFrame(index=range(N))
# df['x'] = np.random.randn(N)
# df['y'] = np.random.randn(N)
# df['z'] = np.random.randn(N)

# labels = []
# for i in range(N):
#     label = df.ix[[i], :].T
#     label.columns = ['Row {0}'.format(i)]
#     # .to_html() is unicode; so make leading 'u' go away with str()
#     labels.append(str(label.to_html()))

# points = ax.plot(df.x, df.y, 'o', color='b',
                 # mec='k', ms=15, mew=1, alpha=.6)


# ax.set_title('HTML tooltips', size=20)

# tooltip = plugins.PointHTMLTooltip("points[0]", labels,
#                                    voffset=10, hoffset=10, css=css)
tooltip = plugins.PointHTMLTooltip(points[0], labels,
                                   voffset=10, hoffset=10, css=css)
plugins.connect(fig, tooltip)

mpld3.show()

