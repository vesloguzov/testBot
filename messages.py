
def first_fit(list_items, max_size):
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
                total += elem['congestion']
            return total

        def show(self):
            return self.list

    list_items = sorted(list_items, key=lambda i: i['congestion'], reverse=True)
    list_bins = [Bin()]

    for item in list_items:

        alloc_flag = False

        for b in list_bins:
            if b.sum() + item['congestion'] <= max_size:
                b.addItem(item)
                alloc_flag = True
                break

        if not alloc_flag:
            new_bin = Bin()
            new_bin.addItem(item)
            list_bins.append(new_bin)

    list_items = []
    for b in list_bins:
        list_items.append(b.show())

    return list_items


items_lol = [{'type': 'turning', 'workplace_num': 0, 'congestion': 100, 'work_time': 240.0}, {'type': 'turning', 'workplace_num': 1, 'congestion': 18.75, 'work_time': 45.0}, {'type': 'drilling', 'workplace_num': 0, 'congestion': 68.75, 'work_time': 165.0}, {'type': 'milling', 'workplace_num': 0, 'congestion': 100, 'work_time': 240.0}, {'type': 'milling', 'workplace_num': 1, 'congestion': 31.25, 'work_time': 75.0}, {'type': 'grinding', 'workplace_num': 0, 'congestion': 81.25, 'work_time': 195.0}]
items_lol = [{'type': 'turning', 'workplace_num': 0, 'congestion': 100, 'work_time': 240.0}, {'type': 'turning', 'workplace_num': 1, 'congestion': 33.33, 'work_time': 80.0}, {'type': 'turning', 'workplace_num': 0, 'congestion': 100, 'work_time': 240.0}, {'type': 'turning', 'workplace_num': 1, 'congestion': 41.66, 'work_time': 100.0}, {'type': 'drilling', 'workplace_num': 0, 'congestion': 100, 'work_time': 240.0}, {'type': 'drilling', 'workplace_num': 1, 'congestion': 8.33, 'work_time': 20.0}, {'type': 'milling', 'workplace_num': 0, 'congestion': 100, 'work_time': 240.0}, {'type': 'milling', 'workplace_num': 1, 'congestion': 100, 'work_time': 240.0}, {'type': 'milling', 'workplace_num': 2, 'congestion': 66.65, 'work_time': 160.0}, {'type': 'grinding', 'workplace_num': 0, 'congestion': 100, 'work_time': 240.0}, {'type': 'grinding', 'workplace_num': 1, 'congestion': 100, 'work_time': 240.0}, {'type': 'grinding', 'workplace_num': 2, 'congestion': 24.99, 'work_time': 60.0}]





# sorted(items_lol, key=lambda i: i['congestion'], reverse=True)

bin_height = 100

# print(items_lol)
# bin_height = 100

# First-fit Algorithm
for t in first_fit(items_lol, bin_height):
    print(t)

# First-fit Decreasing Algorithm
# print(first_fit_dec(items, bin_height))