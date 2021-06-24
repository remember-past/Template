label=np.array([sim_info.KeyCellName_ValueStage_dic[cell_name] for cell_name in cell_name_list]).astype('U8')
#     embedding_array=result_dic['embedding']
if(is_dim2_dim3):
    embedding_plot=np.array([one_vector[1:3] for one_vector in embedding_array])
else:
    embedding_plot=np.array([one_vector[0:2] for one_vector in embedding_array])

embedding_plot_df=pd.DataFrame(embedding_plot,columns=['x','y'])
embedding_plot_df['hue']=label
origin=embedding_plot_df
width=8
height=9
#     height=height*0.5
dpi=300
ratio=1
large_fontsize=18
small_fontsize=12
output_file_dir=target_dir
sim_info.recursive_mkdir(output_file_dir)
output_file_name="_".join([plot_title,str(ratio),str(width),str(height),str(dpi),"_embedding.jpg"])
output_file=os.path.join(output_file_dir,output_file_name)
{'lS_G2': "LS/G2", 'G1': 'G1', 'mS': 'MS', 'eS': 'ES'}
label_name=['G1','ES','MS',"LS/G2"]
hue_order=['G1','eS','mS','lS_G2']
plt.rcParams['font.family']='Arial'
plot_number=1
fig, axes = plt.subplots(nrows=1, figsize=(width, height))
fig.subplots_adjust(wspace=10,hspace=0.5)

ax=axes
plt.sca(ax)
# color_string = ["LightPink", "LightSkyBlue"]
# color_string = ["LightPink", "LightSkyBlue","#90EE90"]
# color_string = ["LightPink", "LightSkyBlue"]
color_string= [ "Red","Green","Blue","Pink"]
# color_string = ["LightPink", "LightSkyBlue","#90EE90","#90EE90"]
temp=sns.despine(ax=ax,right=True,top=True,left=False)
temp=sns.set_style("white") 
# ax = sns.scatterplot(x='x', y='y', data=origin, ax=ax)

temp = sns.scatterplot(x='x', y='y',hue=origin.hue.tolist(),data=origin, ax=ax,palette=color_string,hue_order=hue_order)
#     temp = sns.scatterplot(x='x', y='y',hue=origin.hue.tolist(),data=origin, ax=ax,palette=color_string,hue_order=hue_order)
# plt.axis('on')

#     if(is_dim2_dim3):
#         temp=plt.ylabel('PC3',fontsize=large_fontsize)
#         temp=plt.xlabel('PC2',fontsize=large_fontsize)
#     else:
#         temp=plt.ylabel('PC2',fontsize=large_fontsize)
#         temp=plt.xlabel('PC1',fontsize=large_fontsize)
if(is_dim2_dim3):
    temp=plt.ylabel('tSNE3',fontsize=large_fontsize)
    temp=plt.xlabel('tSNE2',fontsize=large_fontsize)
else:
    temp=plt.ylabel('tSNE2',fontsize=large_fontsize)
    temp=plt.xlabel('tSNE1',fontsize=large_fontsize)

#     temp=plt.ylabel(None)
#     temp=plt.xlabel(None)
handles,labels=ax.get_legend_handles_labels()
# ax.legend(labels=label_name,handles=handles)
temp=plt.xticks(None)
temp=plt.yticks(None)
# temp=plt.title('Marker: '+display_go_name,fontsize=large_fontsize)
temp=plt.title(plot_title,fontsize=large_fontsize)
temp=ax.set_aspect(1.0/ax.get_data_ratio()*ratio)
plt.legend(labels=label_name,handles=handles,loc='best',ncol=1,bbox_to_anchor=(1.11,1.1),borderaxespad = 0.,fancybox=False,shadow=False,frameon=False,fontsize=small_fontsize)


figure_path=output_file
fig=plt.gcf()
plt.show()

fig.savefig(figure_path,dpi=dpi,format='jpg')  