import random
from modules.measurement import getCosineSimilarity

def PrototypeClustering(x_data, th, remain_flag):

    ready_list = [i for i in range(0, len(x_data))]
    label_list = [-1] * len(x_data)

    cluster_idx = 0
    nxt_idx = 0

    while len(ready_list) != 0:
        temp_ready_list = []
        src_idx = nxt_idx
        nxt_score = -1
        cluster_count = 0

        for trg_idx in ready_list:

            score = getCosineSimilarity(x_data[src_idx], x_data[trg_idx])

            if score >= th:
                label_list[trg_idx] = cluster_idx
                cluster_count += 1
            else:
                temp_ready_list.append(trg_idx)

                if nxt_score < score:
                    nxt_score = score
                    nxt_idx = trg_idx

        if cluster_count == 1 and remain_flag != 0:
            label_list[src_idx] = -1
            cluster_idx -= 1

        ready_list = temp_ready_list
        cluster_idx += 1

    return label_list

def Sampling(cluster_dict, n):
    
    res = []
    for label in cluster_dict.keys():
        indices = cluster_dict[label]
        res += random.sample(indices, n)

    return res