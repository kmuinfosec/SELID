# import module
import pickle

from modules.utils import AEchunking, FeatureHashing
from modules.algorithm import PrototypeClustering, Sampling
from conf import config

def main(data_path, save_path):

    # load dataset
    with open(data_path, 'rb') as f:
        payloads = pickle.load(f)

    # deduplication
    payload_dict = dict()
    for idx, payload in enumerate(payloads):
        if payload not in payload_dict.keys():
            payload_dict[payload] = []
        payload_dict[payload].append(idx)
    deduplicated_payloads = list(set(payload_dict.keys()))

    # preprocessing
    chunks_list = [AEchunking(payload, window_size=config['window size']) for payload in deduplicated_payloads]
    vectors = [FeatureHashing(chunks, vec_size=config['vector size']) for chunks in chunks_list]

    # clustering
    _cluster_labels = PrototypeClustering(vectors, th=config['th'], remain_flag=config['remain flag'])

    # release deduplication
    cluster_dict = dict()
    for payload, label in zip(deduplicated_payloads, _cluster_labels):
        if label not in cluster_dict.keys():
            cluster_dict[label] = []
        cluster_dict[label] += payload_dict[payload]

    if config['remain flag']==2 and -1 in cluster_dict.keys():
        del cluster_dict[-1]

    # sampling
    sample_info = Sampling(cluster_dict, n=config['sampling n'])

    # save result
    with open(save_path, 'wb') as f:
        pickle.dump(sample_info, f)

if __name__ == '__main__':
    main(data_path='payloads.pkl', save_path='sample.pkl')
