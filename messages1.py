import random


class Bin():
    def __init__(self, max_capa):
        self.bin_list = []
        self.capacity = 0
        # Max_capa of each bin
        self.max_capa = max_capa

    def bin_append(self, item):
        self.bin_list.append(item)
        self.capacity += item

    def __str__(self):
        return 'Bin (current_capacity=%d, items=%s, max_capacity=%s)' % (
        self.capacity, str(self.bin_list), self.max_capa)


def item_assignment(demand, max_capa):
    '''
    Demand is the list of the requested capacities that need to be fitted in to bins. Each requested capacity is not bigger than 10
    In this simulation, there are 4 bin with different maximum capacity.
    We will see how the demand will fit these 4 bins in BFD.
    '''

    # Sorting the demand list
    values = sorted(demand, reverse=True)
    bins = []
    for i in range(12):
        bins.append(Bin(max_capa))
    for index, bin in enumerate(bins):
        print("Index: %s, bin: %s" % (index + 1, bin))
    print("\nThe list of demands: %s \n" % values)

    from collections import OrderedDict
    fittable_bins = OrderedDict()

    for item in values[:]:

        # Starts fitting each requested capa to bin
        print("\n%s Starting a new fitting %s" % (('*' * 30), ('*' * 30)))
        print("\nThe requested capacity is going to be checked: %s" % item)

        for index, bin in enumerate(bins):
            print("\n******** BEFORE FITTING")
            print("Bin: %s, Value:%s" % (index + 1, bin))
            if bin.capacity + item <= bin.max_capa:
                # Calculate the current capa of each bin
                current_capa = bin.capacity + item
                # Store the fittable to the fittable_bins
                fittable_bins[bin] = (current_capa, index)

        if fittable_bins:
            print("\nThe fittable_bins:")
            for bin, value in fittable_bins.items():
                print("Bin: %s, Value:%s" % (value[1] + 1, bin))
        else:
            print("\nThere is NO fittable_bins")

        if fittable_bins:
            max_current_capa = max(fittable_bins.values(), key=lambda x: x[0])[0]
            for bin, value in fittable_bins.items():
                if value[0] == max_current_capa:
                    bin.bin_append(item)
                    values.remove(item)
                    fittable_bins.clear()
                    print("\n******** AFTER FITTING")
                    print("Bin: %s, Value:%s" % (value[1] + 1, bin))
                    print("\nThe demaining requested capacities: %s \n" % values)
                    break
    return bins


def testing(demand_list, max_capa=None):
    print("%s Starting %s \n " % (('*' * 30), ('*' * 30)))
    bins = item_assignment(demand_list, max_capa)
    print('\n%s RESULT SUMMARY %s' % (('*' * 30), ('*' * 30)))
    print('The simulation using', len(bins), 'bins:')
    for bin in bins:
        print(bin)


if __name__ == '__main__':
    random_demand_list = [random.randint(i, 11) for i in range(1, 10)]
    random_demand_list = [100, 18.75, 68.75, 100, 31.25, 81.25]
    random_demand_list = [5, 4, 4, 3, 2, 2]
    random_demand_list = [100, 33.33, 100, 41.67, 100, 8.33, 100, 100, 66.67, 100, 100, 25]
    # In this testing, maximum capacity of each bin is 11
    testing(random_demand_list, 100)