def prepare_data(data, categorical_indicator, score_type):
    for c, t in zip(data.columns, categorical_indicator):
        if t:
            data[c] = data[c].astype("category").cat.codes.astype("int")
            if data[c].values.max() > 10 or "xgb" in score_type:
                data[c] = data[c].astype("float")
            else:
                data[c] = data[c].astype("int" if "2.5" in score_type else "category")
        else:
            data[c] = data[c].astype("float")
    return data
