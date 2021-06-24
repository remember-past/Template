temp_ax=sns.heatmap(Insulation_Score_array_list, ax=ax, cmap='Reds')
cbax = temp_ax.figure.axes[-1]
cbax.set_frame_on(True)
cbax.tick_params(labelsize=SMALL_SIZE, width=tick_label_width, length=ticklabel_size - 1, pad=1)
[i[1].set_linewidth(tick_label_width) for i in cbax.spines.items()]