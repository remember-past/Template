A4_width=8.25
A4_height=11.75

width=A4_width*0.5
height=A4_width*0.5
dpi=300
mode=2

time=1
fontsize_base=10
fontsize=fontsize_base*time
output_file_dir=r"E:\Users\scfan\data\CellCycle\experiment\distance_stratified_sim\pool\Jaccard"
output_file_name="_".join(["Insulation_Strength_NoTEXT_2021_02_19.png"])
output_file=os.path.join(output_file_dir,output_file_name)

plt.rcParams['font.family']='Arial'

# plt.figure(figsize=(10,8))
plt.figure(figsize=(width,height))

sns.set_context("paper",font_scale=1,rc={"lines.linewidth":1,"lines.color":'black'})
color_string=["LightPink","LightSkyBlue"]
color_string=["#FBBA84","#97A1A1"]
color_string=["LightPink","LightSkyBlue"]

color_string=["#1F71A6","#C483A9"]
color_string=["#F8766D","#00BFC4"]
ax = sns.boxplot(x="stage_name", y="IS", hue="raw_or_sim",
                 data=insulation_score_df, width=0.8,palette=color_string,showfliers=True,dodge=True,fliersize=0.1)
# plt.axis('on')

title_name=""
sns.despine(right=True,top=True)
plt.title(title_name,fontsize=fontsize)
plt.legend(title=None)
plt.xticks(rotation=90,fontsize=fontsize)
plt.yticks(fontsize=fontsize)
plt.ylim(top=3,bottom=0)
plt.xlabel(None)
plt.ylabel("",fontsize=fontsize)
temp=ax.set_yticks([0,1,2,3])

temp=ax.set_xticklabels([])
temp=ax.set_yticklabels([])

# plt.legend(loc='upper center', bbox_to_anchor=(0.5,-0.1),ncol=2,fancybox=False,shadow=False,frameon=False,fontsize=6)
plt.legend(loc='best', ncol=2,bbox_to_anchor=(0.5,1.1),fancybox=False,shadow=False,frameon=False,fontsize=6)
# ax.get_legend().remove()
ax.set_aspect(mode)
# forceAspect(ax,aspect=mode)

figure_path=output_file
fig=plt.gcf()
plt.show()

fig.savefig(figure_path,dpi=dpi,format='png')