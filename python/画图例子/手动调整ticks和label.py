width=3
height=3
dpi=300
time=1
mode_base=1
mode=mode_base*time
fontsize_base=7
fontsize=fontsize_base*time
output_file_dir=sim_basic_info_dir
# output_file_name="_".join([str(mode),str(width),str(height),str(dpi),"_Insulation_Strength.svg"])
output_file_name="_".join([str(mode),str(width),str(height),str(dpi),"_HiCRep_2021_02_08.svg"])

output_file=os.path.join(output_file_dir,output_file_name)

temp=plt.rcParams['font.family']='Arial'

# plt.figure(figsize=(10,8))
temp=plt.figure(figsize=(width,height))

temp=sns.set_context("paper",font_scale=1,rc={"lines.linewidth":1,"lines.color":'black'})
color_string=["LightPink","LightSkyBlue"]
color_string=["#FBBA84","#97A1A1"]
color_string=["gold","#FBBA84","#97A1A1"]
# ax = sns.boxplot(x="mode", y="HiCRep",
#                  data=new_SingleSim_StratifiedSim_RawNeighbor_HiCRep_df, width=1,showfliers=True)
ax = sns.boxplot(x="bin_name", y="HiCRep", hue="mode",
                 data=new_SingleSim_StratifiedSim_RawNeighbor_HiCRep_df, width=0.8,palette=color_string,showfliers=True,dodge=True,fliersize=0.1)
# plt.axis('on')

title_name=""
xmin,xmax=ax.get_xlim()
temp=plt.xlim(-0.42,0.42)
temp=sns.despine(right=True,top=True)
temp=plt.title(title_name,fontsize=fontsize)
temp=plt.legend(title=None)
# plt.xticks(rotation=90,fontsize=fontsize)
# plt.xticks([])
locs,labels=plt.xticks()
print(locs,labels)

temp=ax.set_xticklabels(['a','b','c'])
temp=plt.yticks(fontsize=fontsize)

temp=plt.xlabel(None)
temp=plt.ylabel("HiCRep reproducibility",fontsize=fontsize)
temp=plt.legend(loc='upper center', bbox_to_anchor=(0.5,-0.1),ncol=2,fancybox=False,shadow=False,frameon=False,fontsize=6)
# plt.legend(loc='best', ncol=1,fancybox=False,shadow=False,frameon=False,fontsize=fontsize-3)
# ax.get_legend().remove()
temp=ax.set_aspect(mode)

# forceAspect(ax,aspect=mode)
temp=print(output_file)
figure_path=output_file
fig=plt.gcf()
plt.show()

temp=fig.savefig(figure_path,dpi=dpi,format='svg')