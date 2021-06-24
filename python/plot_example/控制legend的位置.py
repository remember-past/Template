large_name=sim_info.cell_stage_name_FACS_convert_dic[stage_name]


origin=average_auc_plot_df
width=8
height=6
dpi=300
ratio=0.5
large_fontsize=18
small_fontsize=9
output_file_dir=r"D:\Users\scfan\data\CellCycle\experiment\comparision_of_cluster\sim\1\figure"
output_file_name="_".join([dim_name,str(ratio),str(width),str(height),str(dpi),"_average_auc_score.png"])
output_file=os.path.join(output_file_dir,output_file_name)
hue_order=['scHiCluster','Decay','PCA']
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
color_string = ["LightPink", "LightSkyBlue","#90EE90"]
ax=sns.despine(ax=ax,right=True,top=True,left=False)

# ax = sns.scatterplot(x='x', y='y', data=origin, ax=ax)

ax = sns.barplot(x='seqDepth', y='auc_score',hue=origin.method.tolist(),data=origin, ax=ax,palette=color_string,hue_order=hue_order)
# plt.axis('on')

plt.ylim(ymin = 0.30)
temp=plt.ylabel('Average AUC',fontsize=large_fontsize)
temp=plt.xlabel(None)
temp=plt.xticks(rotation=90)
# temp=plt.title('Marker: '+display_go_name,fontsize=large_fontsize)
# temp=plt.title(large_name,fontsize=large_fontsize)
temp=plt.title(None)
temp=ax.set_aspect(1.0/ax.get_data_ratio()*ratio)
plt.legend(loc='best', ncol=3,bbox_to_anchor=(0.95,1.1),borderaxespad = 0.,fancybox=False,shadow=False,frameon=False,fontsize=small_fontsize)

figure_path=output_file
fig=plt.gcf()
plt.show()

fig.savefig(figure_path,dpi=dpi,format='png')