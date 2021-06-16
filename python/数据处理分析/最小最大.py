from sklearn.preprocessing import minmax_scale

fea_data = minmax_scale(feature_data, feature_range=(0.01, 1), axis=0, copy=True)
feature_data = pd.DataFrame(fea_data, columns=feature_data.columns, index=feature_data.index)