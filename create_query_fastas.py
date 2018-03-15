import csv

def main():
	fasta_tuples = []
	with open('sequences.csv', 'r') as seq_file:
		seq_reader = csv.reader(seq_file)
		for row in seq_reader:
			fasta_tuple = (row[1:5], row[5])
			fasta_tuples.append(fasta_tuple)

	for i in range(len(fasta_tuples)):
		cur_header = fasta_tuples[i][0]
		cur_header[0] = '>'+cur_header[0]
		cur_seq	= fasta_tuples[i][1]
		with open('query_' + str(i) +'.fa', 'w') as cur_query_fasta:
			cur_query_fasta.write(' '.join(cur_header) + '\n')
			cur_query_fasta.write(cur_seq + '\n')

if __name__ == "__main__":
	main()