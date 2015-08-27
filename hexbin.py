import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from IPython.display import display
import urllib
from matplotlib.patches import Circle, Rectangle, Arc
from matplotlib.offsetbox import  OffsetImage
from alpha import draw_court
from alpha import cp3_url




shot_chart_url = cp3_url()

pd.set_option('display.width', 200)

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

# plt.axis('off')
# plt.figure(figsize=(12,11))
# plt.figure(figsize=(6,5.5))
# cp3 = plt.hexbin(shot_df.LOC_X, shot_df.LOC_Y, gridsize=[20,7])

joint_shot_chart = sns.jointplot(shot_df.LOC_X, shot_df.LOC_Y, size=7.5, stat_func=None,
                                 kind='hex', space=0, gridsize=[20,6], color=cmap(.2), cmap=cmap)

ax = joint_shot_chart.ax_joint

ax.set_xlim(-250,250)
ax.set_ylim(422.5, -47.5)

# Get rid of axis labels and tick marks
ax.set_xlabel('')
ax.set_ylabel('')
ax.tick_params(labelbottom='off', labelleft='off')
draw_court(ax)
ax.set_title('Chris Paul FGA \n2014-15 Reg. Season', 
             y=0.75, fontsize=18)
ax.add_artist(img)

# draw_court(outer_lines=True)
plt.axis('off')
plt.xlim(-300,300)
plt.ylim(-100,500)
# plt.imshow(paul_pic)

plt.show()

