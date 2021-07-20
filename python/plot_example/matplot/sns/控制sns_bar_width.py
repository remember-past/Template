#https://stackoverflow.com/questions/34888058/changing-width-of-bars-in-bar-chart-created-using-seaborn-factorplot

import pylab as plt
import seaborn as sns

tips = sns.load_dataset("tips")
fig, ax = plt.subplots()

sns.barplot(data=tips, ax=ax, x="time", y="tip", hue="sex")

def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        # we change the bar width
        patch.set_width(new_value)

        # we recenter the bar
        patch.set_x(patch.get_x() + diff * .5)

change_width(ax, .35)
plt.show()