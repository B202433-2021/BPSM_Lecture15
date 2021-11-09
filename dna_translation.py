#!/usr/local/bin/python3

gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

dna = input("Enter the dna sequence to translate: ")

# Function which prints the separate codons and returns the translated protein sequence as a list.

def normal_translation(seq, code_table, start = 0):
	translated = []
	codons = ""
	for i in range(start, len(seq), 3):
		# Make sure to not give an error if the sequence length is not divisible by 3
		if i + 1 == len(seq):
                        codon = seq[i]
		elif i + 2 == len(seq):
			codon = seq[i:i+2]
		else:
			codon = seq[i:i+3]
		# Only translate though if the codon length is 3
		if len(codon) == 3:
			amino = code_table[codon]
			translated.append(amino)

		codons += codon + " "
	print(codons)
	return(translated)

# protein = normal_translation(dna, gencode)
# print("".join(protein))


# Doing the translation in all three forward reading frames. 

 #for start_position in range(3):
#	protein = normal_translation(dna, gencode, start_position)
#	print("".join(protein))




def transcribe(sequence):
	transcribed = []
	for base in sequence:
		if base == "A":
			transcribed.append("T")
		elif base == "T":
			transcribed.append("A")
		elif base == "C":
			transcribed.append("G")
		elif base == "G":
			transcribed.append("C")

	return("".join(transcribed))



# Doing the transcription in all 3 reverse reading frames

transcribed_dna = transcribe(dna)
print(transcribed_dna)
reversed_transcribed_dna = []
for i in transcribed_dna[::-1]:
	reversed_transcribed_dna.append(i)
reversed_transcribed = "".join(reversed_transcribed_dna)
print(reversed_transcribed, "\n")

 
for start_position in range(3):
	protein = normal_translation(reversed_transcribed, gencode, start_position)
	print("".join(protein))
