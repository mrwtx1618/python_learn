#encoding:utf-8
oracle_list = [{'backip':'76.81.241.164','ip':'84.81.241.164','hostname':'bifsdb12','pri_sta':'PRIMARY'},
               {'backip': '76.81.241.228', 'ip': '84.81.241.228', 'hostname': 'bifsdb30', 'pri_sta': 'PRIMARY'},
               {'backip': '76.84.241.132', 'ip': '84.81.241.132', 'hostname': 'bifsdb6', 'pri_sta': 'PRIMARY'},
               {'backip': '76.81.241.36', 'ip': '84.81.241.38', 'hostname': 'bifsdb11', 'pri_sta': 'PRIMARY'},
               {'backip': '76.81.241.32', 'ip': '84.81.241.32', 'hostname': 'bifsdb08', 'pri_sta': 'PRIMARY'}]



rac_list = [{'ip':'84.81.241.32','RELATION_GROUP':'group_1'},
            {'ip':'84.81.241.132','RELATION_GROUP':'group_2'},
            {'ip':'84.81.241.164','RELATION_GROUP':'group_3'}]


# d1 = {'backip': '76.81.241.36', 'ip': '84.81.241.38', 'hostname': 'bifsdb11', 'pri_sta': 'PRIMARY'}
# d2 = {'ip':'84.81.241.38','RELATION_GROUP':'group_1'}

oracle_rac_list = []
def get_oracle_rac_list(list_1,list_2):
    for ele1 in list_1:
    #     print(ele1)
        for ele2 in list_2:
            if ele1['ip'] == ele2['ip']:
                # print('matched')
                oracle_rac_ele = dict(ele1.items()+ele2.items())
                oracle_rac_list.append(oracle_rac_ele)
                break
            # else:
            #     print('unmatched')
        else:
            oracle_rac_ele = ele1
            oracle_rac_list.append(oracle_rac_ele)
    return oracle_rac_list

test_list = get_oracle_rac_list(oracle_list,rac_list)
print(len(test_list))

for ele in test_list:
    print(ele)





# matched_oracle_rac_list = [dict(ele1.items()+ele2.items()) for ele1 in oracle_list for ele2 in rac_list if ele1['ip'] == ele2['ip']]
# # oracle_rac_list2 = [dict(ele1.items()+ele2.items()) if ele1['ip'] == ele2['ip'] else dict(ele1.items()) for ele1 in oracle_list for ele2 in rac_list]
#
#
# print(len(matched_oracle_rac_list))
# # print(len(oracle_rac_list2))
#
#
# # print(oracle_rac_list)
#
#
#
# for ele in matched_oracle_rac_list:
#     print(ele)
#
#
#
# for ele in oracle_list:
#     print(ele)
# # l1 = d1.items()
# # l2 = d2.items()
# # print(len(dict(l1+l2)))
#
#
# all_oracle_rac_list = [ele1 in matched_oracle_rac_list if ele1['ip'] == ele2['ip'] for ele1 in matched_oracle_rac_list else ele2 for ele2 in oracle_list]
# # print(len(all_oracle_rac_list))
# print('*************************')
# for ele in all_oracle_rac_list:
#     print(ele)
