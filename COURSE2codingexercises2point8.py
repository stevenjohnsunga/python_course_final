import array as arr

from numpy import ones_like

def display_ave():
    print("Average purchased items:")

def get_ave():
    n = len(items)
    get_sum= sum (items)
    mean = get_sum/n
    m = str (mean)
    print(m)

online_pur = [19,27,17,24,16]

sample_data = arr.array('i',online_pur)
items = sample_data[0:5]
sample_data_list = items.tolist()

display_ave()
get_ave()
