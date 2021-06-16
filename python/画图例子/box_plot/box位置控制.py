import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

dict_a = {'value':[1,2,3,7,8,9],'name':['Group_a']*3+['Group_b']*3}
dataframe = pd.DataFrame(dict_a)
ax=sns.boxplot( y="value" , x="name" , data=dataframe )
xmin,xmax=ax.get_xlim()
print(xmin,xmax)
ax.set_xlim(0, 1)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dict_a = {'value':[1,2,3,7,8,9],'name':['Group_a']*3+['Group_b']*3}
dataframe = pd.DataFrame(dict_a)

fig, (ax, ax2, ax3) = plt.subplots(nrows=3,
                                   gridspec_kw=dict(height_ratios=[4,4,1], hspace=1))

sns.boxplot( y="value" , x="name" , data=dataframe, width=0.1, ax=ax)
dataframe.boxplot("value", by = "name", ax=ax2)


from matplotlib.widgets import Slider
slider = Slider(ax3, "", valmin=0, valmax=3)

def update(val):
    ax.set_xlim(-val, 1+val)
    ax2.set_xlim(1-val, 2+val)

slider.on_changed(update)


plt.show()