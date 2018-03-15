import csv
import os 
import subprocess
import sys
from tqdm import tqdm

def main():
	queries_dir = os.path.join(os.getcwd(), 'query_fastas');
	query_files = os.listdir(queries_dir) 
	query_paths = [os.path.join('query_fastas', qfile) for qfile in query_files]
		
	out_dir = os.path.join(os.getcwd(), 'query_fastas');
	out_paths = [os.path.join('blast_outputs', 'out_' + str(i)) for i in range(7330)]

	html_paths = [os.path.join('blast_htmls', 'html_' + str(i)) for i in range(7330)]


	for i in tqdm(range(len(query_files))):
		subprocess.call(['psiblast', 
			'-query', query_paths[i], 
			'-db', 'nrdb90', 
			'-num_iterations', '3', 
			'-evalue', '0.001', 
			'-out_ascii_pssm', out_paths[i],
			'-outfmt', '7',
			'-out', html_paths[i],
			'-num_threads', '12',
			'-comp_based_stats', '1'])
	# fasta_tuples = []
	# with open('sequences.csv', 'r') as seq_file:
	# 	seq_reader = csv.reader(seq_file)
	# 	for row in seq_reader:
	# 		fasta_tuple = (row[1:5], row[5])
	# 		fasta_tuples.append(fasta_tuple)

	# for i in range(len(fasta_tuples)):
	# 	cur_header = fasta_tuples[i][0]
	# 	cur_seq	= fasta_tuples[i][1]
	# 	with open('query_' + str(i) +'.fa', 'w') as cur_query_fasta:
	# 		cur_query_fasta.write(' '.join(cur_header) + '\n')
	# 		cur_query_fasta.write(cur_seq + '\n')

if __name__ == "__main__":
	main()