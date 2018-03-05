import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import PyPDF2

supplement = "Supplementary_Material_S1.pdf"
pdfFileObj = open(supplement, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
text = '';
for i in tqdm(np.arange(pdfReader.numPages)):
    pageObj = pdfReader.getPage(i)
    text += pageObj.extractText()
text = text.replace('\n', '')
text = text.replace('i>', '')
text = text.replace('>p', '')
raw_proteins = text.split('>')
ID = []
family = []
thingy = []
info = []
sequence = []
for i in tqdm(np.arange(len(raw_proteins)-1)):
    record = raw_proteins[i+1].split(' ', maxsplit = 1)
    ID.append(record[0])
    record = record[1].split(' ', maxsplit = 1)
    family.append(record[0])
    record = record[1].split(' ', maxsplit = 1)
    thingy.append(record[0])
    record = record[1].split('}', maxsplit = 1)
    info.append(record[0]+ '}')
    sequence.append(record[1])
records = [list(a) for a in zip(ID, family, thingy, info, sequence)]
labels = ["ID", 'Family', 'Thingy', 'Info', 'Sequence']
df =  pd.DataFrame.from_records(records, columns=labels)
df.to_csv('sequences.csv')
