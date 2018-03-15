import os 
import re
from tqdm import tqdm

def main():
	outs_dir = os.path.join(os.getcwd(), 'blast_outputs');
	outs_files = os.listdir(outs_dir) 
	outs_paths = [os.path.join('blast_outputs', outfile) for outfile in outs_files]

	# acc = ["out_" + str(x) for x in range(1, 7330)]
	# thrown = [file for file in acc if file not in outs_files]
	# print(thrown)
	# fasta_names = ["query_" + str(re.findall(r'\d+', t)[0]) +".fa" for t in thrown]
	# thrown_paths = [os.path.join('query_fastas', fasta) for fasta in fasta_names]
	# for fil in tqdm(thrown_paths):
	# 	f = open(fil, 'r')
	# 	line = f.readline().split()
	# 	print(line[0].lstrip('>'))


	for ofile in tqdm(outs_paths):
		f = open(ofile, 'r')
		save_flag = False
		saved_lines = []
		for line in f:
			words = line.split()

			if save_flag and len(words) > 0:
				if words[0].isalpha():
					saved_lines.append(words[:20])
				else:
					saved_lines.append(words[2:22])
			if len(words) > 0 and words[0] == "Last":
				save_flag = True
			if len(words) == 0:
				save_flag = False
		f.close()

		num = re.findall(r'\d+', ofile)[0]
		out = open('pssms/pssm_' + num, 'w')
		for line in saved_lines:
			out.write('\t'.join(line) + '\n')
		f.close()

if __name__ == "__main__":
	main()