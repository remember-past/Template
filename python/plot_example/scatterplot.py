origin=embedding_plot_df
width=8.3
height=11.7
height=height*0.5
dpi=300
ratio=0.5
large_fontsize=14
small_fontsize=9
output_file_dir=r"D:\Users\scfan\data\CellCycle\experiment\comparision_of_cluster\raw\0.25\figure"
output_file_name="_".join([str(ratio),str(width),str(height),str(dpi),"_scHiCluster.svg"])
output_file=os.path.join(output_file_dir,output_file_name)
hue_order=sim_info.cell_stage_name_FACS
plt.rcParams['font.family']='Arial'
plot_number=1
fig, axes = plt.subplots(nrows=1, figsize=(width, height))
fig.subplots_adjust(wspace=10,hspace=0.5)

ax=axes
plt.sca(ax)
# color_string = ["LightPink", "LightSkyBlue"]
# color_string = ["LightPink", "LightSkyBlue","#90EE90"]
# color_string = ["LightPink", "LightSkyBlue"]
color_string= ["Pink", "Red","Green","Blue"]
color_string = ["LightPink", "LightSkyBlue","#90EE90","#90EE90"]
ax=sns.despine(ax=ax,right=True,top=True,left=False)

# ax = sns.scatterplot(x='x', y='y', data=origin, ax=ax)

ax = sns.scatterplot(x='x', y='y',hue=origin.hue.tolist(),data=origin, ax=ax,palette=color_string,hue_order=hue_order)
# plt.axis('on')

temp=plt.ylabel('Insulation score',fontsize=large_fontsize)
temp=plt.xlabel(None)
temp=plt.xticks(rotation=45)
# temp=plt.title('Marker: '+display_go_name,fontsize=large_fontsize)
temp=plt.title('Insulation score',fontsize=large_fontsize)
temp=ax.set_aspect(1.0/ax.get_data_ratio()*ratio)
plt.legend(loc='best', ncol=1,fancybox=False,shadow=False,frameon=False,fontsize=small_fontsize)

figure_path=output_file
fig=plt.gcf()
plt.show()

# fig.savefig(figure_path,dpi=dpi,format='svg')  