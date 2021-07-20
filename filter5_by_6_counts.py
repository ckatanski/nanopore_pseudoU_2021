import argparse

# import pysam
import pandas as pd
#import time
#import subprocess
#import random
#import os
#from Bio import SeqIO
#import numpy as np
#import time
#np.random.seed(0) #IMPORTANT IMPORTANT IMPORTANT


def filter_by_count_genes(ref_file, n_filer=100):
	data = pd.read_csv(ref_file, sep="\t", header=0)
	data = data[data["count"] >= n_filer]
	# print(data["count"])
	return(set(data["name"]))


def read_filter_print(in_file, allowed_genes):
	with open(in_file) as f:
		with open(in_file[0:-4] + "_filtered.tsv" , "w") as out:
			out.write(f.readline())
			for line in f.readlines():
				# line = f.readline()
				if line.split('\t')[0] in allowed_genes:
					out.write(line)


def main_program(in_file, ref_file, n_filer=100):
	allowed_genes = filter_by_count_genes(ref_file, n_filer)
	read_filter_print(in_file, allowed_genes)



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i") #Input data path
	parser.add_argument("-r")
	parser.add_argument("-n")

	args = parser.parse_args()

	in_file = args.i
	ref_file = args.r
	n_filer = int(args.n)
	main_program(in_file, ref_file, n_filer)




