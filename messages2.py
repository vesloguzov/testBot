import numpy as np

def to_constant_volume(d, V_max, weight_pos=None, lower_bound=None, upper_bound=None):
    if lower_bound is not None and upper_bound is not None and lower_bound < upper_bound:
        get_valid_weight_ndcs = lambda a: np.nonzero(np.logical_and(a > lower_bound, a < upper_bound))[0]
    elif lower_bound is not None:
        get_valid_weight_ndcs = lambda a: np.nonzero(a > lower_bound)[0]
    elif upper_bound is not None:
        get_valid_weight_ndcs = lambda a: np.nonzero(a < upper_bound)[0]
    elif lower_bound is None and upper_bound is None:
        get_valid_weight_ndcs = lambda a: np.arange(len(a), dtype=int)
    elif lower_bound >= upper_bound:
        raise Exception("lower_bound is greater or equal to upper_bound")

    isdict = isinstance(d, dict)
    is_tuple_list = (not isdict) and (hasattr(d[0], 'len'))

    if is_tuple_list:
        if weight_pos is not None:

            new_dict = {i: tup for i, tup in enumerate(d)}
            d = {i: tup[weight_pos] for i, tup in enumerate(d)}
            isdict = True
        else:
            raise Exception("no weight axis provided for tuple list")

    if isdict:

        # get keys and values (weights)
        keys_vals = d.items()
        keys = np.array([k for k, v in keys_vals])
        vals = np.array([v for k, v in keys_vals])

        # sort weights decreasingly
        ndcs = np.argsort(vals)[::-1]

        weights = vals[ndcs]
        keys = keys[ndcs]

        bins = [{}]
    else:
        weights = np.sort(np.array(d))[::-1]
        bins = [[]]

    # find the valid indices
    valid_ndcs = get_valid_weight_ndcs(weights)
    weights = weights[valid_ndcs]

    if isdict:
        keys = keys[valid_ndcs]

    # the total volume is the sum of all weights
    V_total = weights.sum()

    # prepare array containing the current weight of the bins
    weight_sum = np.array([0.])

    # iterate through the weight list, starting with heaviest
    for item, weight in enumerate(weights):

        if isdict:
            key = keys[item]

        # find candidate bins where the weight might fit
        candidate_bins = np.where(weight_sum + weight <= V_max)[0]

        # if there are candidates where it fits
        if len(candidate_bins) > 0:

            # find the fullest bin where this item fits and assign it
            candidate_index = np.argmax(weight_sum[candidate_bins])
            b = candidate_bins[candidate_index]

        # if this weight doesn't fit in any existent bin
        else:
            # open a new bin
            b = len(weight_sum)
            weight_sum = np.append(weight_sum, 0.)
            if isdict:
                bins.append({})
            else:
                bins.append([])

        # put it in
        if isdict:
            bins[b][key] = weight
        else:
            bins[b].append(weight)

        # increase weight sum of the bin and continue with
        # next item
        weight_sum[b] += weight

    if not is_tuple_list:
        return bins
    else:
        new_bins = []
        for b in range(len(bins)):
            new_bins.append([])
            for key in bins[b]:
                new_bins[b].append(new_dict[key])
        return new_bins


items = [100, 33.33, 100, 41.67, 100, 8.33, 100, 100, 66.67, 100, 100, 33, 23, 69]

bins = to_constant_volume(items, 100)
print(bins)