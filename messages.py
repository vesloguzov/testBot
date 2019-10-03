class Bin:
    def __init__(self):
        self.list = []

    def addItem(self, item):
        self.list.append(item)

    def removeItem(self, item):
        self.list.remove(item)

    def sum(self):
        total = 0
        for elem in self.list:
            total += elem
        return total

    def show(self):
        return self.list


def first_fit(list_items, max_size):
    """ Returns list of bins with input items inside. """
    list_bins = []
    list_bins.append(Bin())  # Add first empty bin to list

    for item in list_items:

        alloc_flag = False

        for bin in list_bins:
            if bin.sum() + item <= max_size:
                bin.addItem(item)
                alloc_flag = True
                break

        # If item not allocated in bins in list, create new bin
        # and allocate it to it.
        if alloc_flag == False:
            newBin = Bin()
            newBin.addItem(item)
            list_bins.append(newBin)

    # Turn bins into list of items and return
    list_items = []
    for bin in list_bins:
        list_items.append(bin.show())

    return (list_items)


def first_fit_dec(list_items, max_size):
    """ Returns list of bins with input items inside. """
    # Sort list in decreasing order
    list_items.sort(reverse=True)

    # Apply first-fit algorith
    return (first_fit(list_items, max_size))


items = [8, 16, 12, 8, 45, 18, 30, 7, 10, 14, 9, 9, 52, 88]
bin_height = 60


items = [100, 18.75, 68.75, 100, 31.25, 81.25]

items = [100, 33.33, 100, 41.67, 100, 8.33, 100, 100, 66.67, 100, 100, 25]

bin_height = 100

# First-fit Algorithm
print(first_fit(items, bin_height))

# First-fit Decreasing Algorithm
print(first_fit_dec(items, bin_height))