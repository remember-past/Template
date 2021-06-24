temp = sns.scatterplot(x='x', y='y',hue=origin.hue.tolist(),data=origin, ax=ax,palette=color_string,
                       hue_order=hue_order,edgecolor=None,alpha=0.8)