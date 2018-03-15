import csv
from tqdm import tqdm

def main():
	lines = []
	with open('pseqs.csv', 'r') as pseq_file:
		pseq_reader = csv.reader(pseq_file)
		headers = next(pseq_reader)
		for row in pseq_reader:
			if row[7] != 'NA':
				cur_header = row[2:6]
				cur_header[0] = '>'+cur_header[0]
				lines.append(' '.join(cur_header) + '\n')
				lines.append(row[7] + '\n')
	
	with open('../pseq_db.fa', 'w') as pseq_db_fasta:
		for line in lines:
			pseq_db_fasta.write(line)

if __name__ == "__main__":
	main()