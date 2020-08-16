def get_indices_of_item_weights(weights, _, limit):
    indices_by_weight = {}
    for (index, weight) in enumerate(weights):
        if weight not in indices_by_weight:
            indices_by_weight[weight] = [index]
        else:
            indices_by_weight[weight].append(index)
    for (index, weight) in enumerate(weights):
        target = limit - weight
        if target in indices_by_weight:
            for cur_index in indices_by_weight[target]:
                if index is not cur_index:
                    return (index, cur_index)\
                        if max(index, cur_index) == index\
                        else (cur_index, index)
    return None
