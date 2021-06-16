A4_width = 8.25
A4_height = 11.75

width = A4_width * 1
height = A4_height * 1
dpi = 300
ratio = 2

output_file_dir = r"E:\Users\scfan\data\CellCycle\experiment\distance_stratified_sim\pool_five_region\loop\figure\TopN_ratio"
output_file_name = "_".join(
    [str(ratio), str(width), str(height), str(dpi), "_loop_TopN_InTopN_Raw_ratio_TEXT_2021_02_20.png"])
output_file = os.path.join(output_file_dir, output_file_name)

plt.rcParams['font.family'] = 'Arial'
plt.figure(figsize=(width, height))
plot_number = 5
fig, axes = plt.subplots(ncols=plot_number, figsize=(width, height))
fig.subplots_adjust(wspace=0.05)

temp_ratio_array = np.array([])
for i, region_start_end_name in enumerate(sim_info.five_region_start_end_name_list):
    region_start_end_name = sim_info.five_region_start_end_name_list[i]

    region_name = sim_info.five_region_name[i]

    plot_df = raw2simAndAdj_topN_InTopN_raw_ratio_df_dic[region_start_end_name]
    ratio_list = list(plot_df['raw vs. sim'].values) + list(plot_df['raw vs. adjacent stage'].values)
    mode_list = ['raw vs. sim'] * plot_df.shape[0] + ['raw vs. adjacent stage'] * plot_df.shape[0]
    percentage_list = list(plot_df['percentage'].values) + list(plot_df['percentage'].values)

    sns_plot_df = pd.DataFrame({'ratio': ratio_list, 'mode': mode_list, 'percentage': percentage_list})
    temp_ratio_array = np.concatenate([temp_ratio_array, sns_plot_df['ratio'].values])

ybottom = temp_ratio_array.min() - 0.02
ytop = temp_ratio_array.max() + 0.02
for i, ax in enumerate(axes):

    region_start_end_name = sim_info.five_region_start_end_name_list[i]

    region_name = sim_info.five_region_name[i]

    plot_df = raw2simAndAdj_topN_InTopN_raw_ratio_df_dic[region_start_end_name]
    ratio_list = list(plot_df['raw vs. sim'].values) + list(plot_df['raw vs. adjacent stage'].values)
    mode_list = ['raw vs. sim'] * plot_df.shape[0] + ['raw vs. adjacent stage'] * plot_df.shape[0]
    percentage_list = list(plot_df['percentage'].values) + list(plot_df['percentage'].values)

    sns_plot_df = pd.DataFrame({'ratio': ratio_list, 'mode': mode_list, 'percentage': percentage_list})

    if (i == 0):
        plt.sca(ax)
        color_string = ["#FBBA84", "#97A1A1"]
        sns.lineplot(ax=ax, x='percentage', y='ratio', hue='mode', palette=color_string, data=sns_plot_df)
        sns.scatterplot(ax=ax, x='percentage', y='ratio', hue='mode', palette=color_string, data=sns_plot_df,
                        legend=None)
        sns.despine(right=True, top=True, left=False)
        title_name = region_name
        #         ybottom, ytop = ax.get_ylim()
        ax.set_ylim(top=ytop, bottom=ybottom)
        print(ybottom, ytop)
        plt.title(title_name, fontsize=10)

        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        #         plt.xlabel("Top n% significant loops",fontsize=10)
        plt.xlabel(None)
        plt.ylabel("Percentage of loops in Top N raw set", fontsize=10)
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles=handles[1:], labels=labels[1:], loc='best', bbox_to_anchor=(1.8, -0.1), ncol=1,
                  fancybox=False, shadow=False, frameon=False, fontsize=10)
        # plt.legend(title="10",loc='best', ncol=2,fancybox=False,shadow=False,frameon=False,fontsize=10)

        ax.set_aspect(1.0 / ax.get_data_ratio() * ratio)
    else:
        plt.sca(ax)
        color_string = ["#FBBA84", "#97A1A1"]
        sns.lineplot(ax=ax, x='percentage', y='ratio', hue='mode', palette=color_string, data=sns_plot_df, legend=None)
        sns.scatterplot(ax=ax, x='percentage', y='ratio', hue='mode', palette=color_string, data=sns_plot_df,
                        legend=None)
        ax.set_ylim(top=ytop, bottom=ybottom)
        #         ax.set_ylim(ymin=ybottom,ymax=ytop)
        sns.despine(right=True, top=True)
        title_name = region_name
        plt.title(title_name, fontsize=10)

        plt.xticks(fontsize=8)
        #         plt.yticks([])
        ax.axes.yaxis.set_ticklabels([])
        #         plt.yticks(fontsize=8)
        #         plt.xlabel("Top n% significant loops",fontsize=10)
        plt.xlabel(None)
        plt.ylabel(None)

        ax.set_aspect(1.0 / ax.get_data_ratio() * ratio)
fig.text(0.5, 0.35, 'Top N significant loops\nCommon loops come from top N raw set.', ha='center', fontsize=10)
figure_path = output_file
fig = plt.gcf()
plt.show()

fig.savefig(figure_path, dpi=dpi, format='png')
