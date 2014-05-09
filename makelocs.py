#!/usr/bin/env python
import codecs
import os

# Generate localized properties files from a tab-delimited master input file

inFilePath = 'master-strings.txt'

files = []
locales = []
	
# input file		
ix = 0
for line in codecs.open(inFilePath, "r", "utf-8"): 
	ix = ix + 1
	line = line.replace('\r\n', '')	
	line = line.replace('\n', '')
	#print line
	values = line.split('\t')
	
	if ix == 1:
		# create output files based on input file headers
		ix_inner = 0;
		for val in values:
			ix_inner = ix_inner + 1
			if ix_inner == 1:
				continue
			if os.path.exists(val + "/strings.properties"):
				os.remove(val + "/strings.properties")		
			if os.path.exists(val):
				pass	
			else:
				os.mkdir(val)	
			f = codecs.open(val + "/strings.properties", "w", "utf-8")
			files.append(f)
			locales.append(val)
		continue;
	
	# values contains the key and translations for each lang	
	r = range(1, len(files) + 1)
	for vals_ix in r:
		# in case we don't have translations yet
		if vals_ix >= len(values):
			# make sure there are at least two tab-delimited tokens per line
			if len(values) < 2:
				print "Fatal error parsing " + inFilePath + " line " + str(ix) + ": " + str(values) + ".  Perhaps you forgot to separate translations with tabs?"
				exit()
			#print values[1]
			val = values[1] + '_NO_LOC_' + locales[vals_ix-1][3:]
		else:
			val = values[vals_ix]
			val = val.replace('"', '')
		s = values[0] + "=" + val + "\n"		
		files[vals_ix-1].write(s) 			
		
for f in files:
	f.close()	