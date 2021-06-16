region_names = np.array([_n for _n in sorted(np.unique(rep1_info_dict['Genomic coordinate']),
                                             key=lambda s:int(s.split(':')[1].split('-')[0]))])
region_starts = np.array([int(_n.split(':')[1].split('-')[0]) for _n in region_names])
region_ends = np.array([int(_n.split(':')[1].split('-')[1]) for _n in region_names])[np.argsort(region_starts)]
region_starts = np.sort(region_starts)

mid_positions = ((region_starts + region_ends)/2).astype(np.int)
mid_positions_Mb = np.round(mid_positions / 1e6, 2)
start_position_Mb = np.round(region_starts / 1e6, 2)
end_position_Mb = np.round(region_ends / 1e6, 2)