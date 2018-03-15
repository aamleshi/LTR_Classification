import csv
import os
from tqdm import tqdm

def main():
	fasta_tuples = []
	with open('pseqs.csv', 'r') as pseq_file:
		pseq_reader = csv.reader(pseq_file)
		headers = next(pseq_reader)
		for row in pseq_reader:
			if row[7] != 'NA':
				fasta_tuple = (row[2:6], row[7])
				fasta_tuples.append(fasta_tuple)
				

				cur_header = row[2:6]
				cur_header[0] = '>'+cur_header[0]

	for i in tqdm(range(len(fasta_tuples))):
		cur_header = fasta_tuples[i][0]
		cur_header[0] = '>'+cur_header[0]
		cur_seq	= fasta_tuples[i][1]
		cur_pquery_path = os.path.join('pquery_fastas', 'pquery_' + str(i) +'.fa') 
		with open(cur_pquery_path, 'w') as cur_pquery_fasta:
			cur_pquery_fasta.write(' '.join(cur_header) + '\n')
			cur_pquery_fasta.write(cur_seq + '\n')

if __name__ == "__main__":
	main()