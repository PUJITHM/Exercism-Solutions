data = {
		'G' : 'C',
		'C' : 'G',
		'T' : 'A',
		'A' : 'U'
		}


def to_rna(dna_strand):
	result = str()
	for dna in dna_strand:
		try:
			result += data[dna]
		except Exception as e:
			raise ValueError("dna_strand not recognised!")
	return result