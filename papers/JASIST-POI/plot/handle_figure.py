import glob

filename_list = glob.glob('raw/*.txt')
run_file = open('run','w')

for filename in filename_list:
	data_list = []
	class_list = []
	file = open(filename)
	for line in file:
		tokens  = line.rstrip().split('\t')
		data_list.append(tokens[1:])
		class_list.append(tokens[0])
	file.close()
	file = open(filename[filename.find('/')+1:],'w')
	for i in range(len(data_list[0])):
		file.write('{0}'.format(data_list[0][i]))
		for j in range(len(data_list)-1):
			file.write('\t{0}'.format(data_list[j+1][i]))
		file.write('\n')
	file.flush()
	file.close()
	
	head = '''
set boxwidth 1 relative
set style data histogram
set style histogram cluster
set style fill pattern 3 border lt -1
set key title ""
set key inside right top
set size ratio 0.618
set xlabel "DIY" offset 0,-1.5
set ylabel "DIY" offset 1.5,0
set xtics rotate by 45 offset -1.5,-2.5
set term post eps enhanced "Helvetica" 25
	'''
	
	file  = open('{0}_plot'.format(filename[filename.find('/')+1:-4]),'w')
	run_file.write('load "{0}_plot"\n'.format(filename[filename.find('/')+1:-4]))
	file.write(head)
	file.write('\n')
	file.write('set output "{0}.eps"\n'.format(filename[filename.find('/')+1:-4].replace(' ','_')))
	file.write('plot "{0}" using {1}:xticlabel(1) title "{2}"'.format(filename[filename.find('/')+1:],2,class_list[1]))
	index = 3
	for cls in class_list[2:]:
		file.write(', "{0}" using {1}:xticlabel(1) title "{2}"'.format(filename[filename.find('/')+1:],index,cls))
		index += 1
	file.write('\n')
	file.flush()
	file.close()
	
run_file.flush()
run_file.close()