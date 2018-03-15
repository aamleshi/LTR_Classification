import csv
import os 
import subprocess
import sys
from tqdm import tqdm

def main():
	queries_dir = os.path.join(os.getcwd(), 'pquery_fastas');
	query_files = os.listdir(queries_dir) 
	query_paths = [os.path.join('pquery_fastas', qfile) for qfile in query_files]

	out_paths = []
	for i in tqdm(range(len(query_paths))):
		with open(query_paths[i], 'r') as qfile:
			first_line = qfile.readline().split()
			query_id = 'pse_hmmer_' + first_line[0][1:] 
		cur_out_path = os.path.join('pseudo_hmmer_csv', query_id)
		out_paths.append(cur_out_path)
	# print(query_paths[:5])
	# print(out_paths[:5])
	for i in tqdm(range(len(query_paths))):
		# print(query_paths[i])
		subprocess.call(['./phmmer', '-o', '/dev/null', '--tblout', out_paths[i], query_paths[i], "../pseq_db.fa"])
	

if __name__ == "__main__":
	main()