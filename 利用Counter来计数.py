from collections import Counter
import json


path = '/home/wtx/Desktop/利用python进行数据分析/pydata-book/datasets/bitly_usagov/example.txt'

with open(path) as f:
    the_dict_list = [json.loads(ele) for ele in f.readlines()]

for the_dict in the_dict_list:
    time_zones = [the_dict['tz'] for the_dict in the_dict_list if 'tz' in the_dict]

time_zones_counts = Counter(time_zones)
print(time_zones_counts)
print(time_zones_counts.most_common(10))#最常出现的10个











