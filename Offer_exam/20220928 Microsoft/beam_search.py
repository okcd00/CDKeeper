"""
import torch
import random
vocab_size = 1000

vocabulary = [i for i in enumerate(vocab_size)]
index_sos = 0
index_eos = 1
embedding = None


def get_prob(last_repr, inp_i):
    # step i
    # input: decode_i-1 repr, input i-th token
    something = [random.random() for _ in range(len(vocab_size))]  #
    return something


def get_encoding(h_forward, inp_i):
    # assume it is a LSTM cell
    something = None  #
    return something


def translate(source_sentence, beam_size=20, maximum_sentence_length=512):
    outputs = []

    token_last = '<sos>'
    beam_case = []  # a list of top-20 candidates
    repr_in_beam = []  # the repr for each candidate in the beam list
    
    dest_sentence_size = 0
    for i, char in enumerate(source_sentence):
        cur_inp_repr = embedding.lookup(char)
        candidates = []
        if i == 0:
            last_repr = embedding.lookup(token_last)
            beam_case, confidence_scores = torch.argsort(
                get_prob(last_repr, cur_inp_repr))
            beam_case = beam_case[:20]
            confidence_scores = confidence_scores[:20]
            repr_in_beam = [get_encoding(last_repr, inp_i) for inp_i in beam_case]
            continue
        else:
            for prefix, last_repr in zip(beam_case, repr_in_beam):
                # [1 3 2 5 4], [0.9 0.7 0.5 0.2 0.1]  <=  [1,2,3,4,5]
                cur_beam_case, confidence_scores = torch.argsort(get_prob(last_repr, cur_inp_repr))
                cur_beam_case = [prefix + [_char] for _char in cur_beam_case]
                cur_beam_case = cur_beam_case[:20]
                confidence_scores = confidence_scores[:20]
                repr_in_beam = [get_encoding(last_repr, inp_i) for inp_i in beam_case]
                candidates.extend(zip(cur_beam_case, confidence_scores, repr_in_beam))
        candidates.sort(key=lambda x: -x[1])
        candidates = candidates[:beam_size]
        beam_case = [x[0] for x in candidates]
        repr_in_beam = [x[2] for x in candidates]

        if index_eos in beam_case:
            outputs.append()
            
    
    # we allow the dest sentence is longer than the source sentence.
    while beam_size > 0 and dest_sentence_size < maximum_sentence_length:
        

        if vocabulary.index('<eos>') in beam_case:
"""


from math import log
import numpy as np


def beam_search_decoder(data, k):
    sequences = [[list(), 1.0]]

    for row in data:
        all_candidates = list()

        for i in range(len(sequences)):
            seq, score = sequences[i]
            for j in range(len(row)):
                candidate = [seq + [j], score * -log(row[j])]
                all_candidates.append(candidate)

        ordered = sorted(all_candidates, key=lambda tup: tup[1])  # 按score排序
        sequences = ordered[:k]  # 选择前k个最好的
    return sequences


def greedy_decoder(data):

    return [np.argmax(s) for s in data]


if __name__ == '__main__':

    data = [[0.1, 0.5, 0.4],
            [0.3, 0.2, 0.5],
            [0.5, 0.3, 0.2]]
    data = np.array(data)
    result = beam_search_decoder(data, 3)
    print("****use beam search decoder****")
    for seq in result:
        print(seq)

    print("****use greedy decoder****")
    print(greedy_decoder(data))
