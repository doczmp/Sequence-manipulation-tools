#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:40:35 2021

@author: zmp
"""

import random 
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Introduce mutations in string.')
parser.add_argument("--fasta", help="Input Fasta file location")
parser.add_argument("--nMut", default=1, type=int, help="Input number of substitutions in string per 100 bp")
parser.add_argument("--output", help="Input number of substitutions in string")

args = parser.parse_args()

nmut = args.nMut








def draw(discrete_probdist):
    """
    Draw random value from discrete probability distribution
    represented as a dict: P(x=value) = discrete_probdist[value].
    """
    # Method:
    # http://en.wikipedia.org/wiki/Pseudo-random_number_sampling
    limit = 0
    r = random.random()
    for value in discrete_probdist:
        limit += discrete_probdist[value]
        if r < limit:
            return value


def mutate_via_markov_chain(dna2, markov_chain,N):
    dna2 = np.array(dna2, dtype='c')  # array of characters
    mutation_sites = np.random.choice(range(len(dna2)), size = N, replace = False)
    from_base = dna2[mutation_sites]
    from_base = from_base.astype('U13')
    i = 0
    for f in from_base:
        to_base = draw(markov_chain[f])
        dna2[mutation_sites[i]] = to_base
        i = i + 1
    dna2 = ''.join(map(bytes.decode, dna2))
    return dna2



mc = {}

mc ['A'] = {'A': 0, 'C': 1/3, 'G': 1/3, 'T': 1/3}
mc ['C'] = {'A': 1/3, 'C': 0, 'G': 1/3, 'T': 1/3}
mc ['G'] = {'A': 1/3, 'C': 1/3, 'G': 0, 'T': 1/3}
mc ['T'] = {'A': 1/3, 'C': 1/3, 'G': 1/3, 'T': 0}


from Bio import SeqIO

dna = []
NameID = []


for seq_record in SeqIO.parse(args.fasta, "fasta"):
    dna.append(str(seq_record.seq))
    NameID.append(seq_record.id)

    
dna = [item.upper() for item in dna]


mutated = []
length = []
mutations = []

#49,27,6

for x in dna:
    length.append(len(x))
    nmutations = round((nmut/100) * len(x))
    mutations.append(nmutations)
    Y = mutate_via_markov_chain(x,mc,nmutations)
    mutated.append(Y)
    

ofile = open(args.output, "w")

for i in range(len(mutated)):
    ofile.write(">" + NameID[i] + "\n" + mutated[i] + "\n")

ofile.close()
