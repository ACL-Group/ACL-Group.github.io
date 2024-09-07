import glob

def processFeatureF1ForCate_data():
	file = open('FeatureF1ForCate_data.txt')
	title_list = []
	xlabel_list = []
	data_list = []
	line = file.readline()
	tokens = line.strip().split('\t')
	title_list = tokens[1:]
	for i in xrange(len(title_list)):
		data_list.append([])
	for line in file:
		tokens = line.strip().split('\t')
		xlabel_list.append(tokens[0])
		for i in xrange(len(tokens[1:])):
			data_list[i].append(tokens[1:][i])
	file.close()
	for i in xrange(len(data_list)):
		file = open('FeatureF1ForCate_data/{0}_data.txt'.format(title_list[i].replace(' ','_')),'w')
		for j in xrange(len(xlabel_list)):
			file.write('{0}\t{1}\n'.format(xlabel_list[j].replace('_','\\\\_'),data_list[i][j]))
		file.flush()
		file.close()
		
def generateFeatureF1ForCate_plot():
	file_name_list = glob.glob('FeatureF1ForCate_data/*.txt')
	file = open('FeatureF1ForCate_data/plot','w')
	script = """set boxwidth 1 relative
set style data histogram
set style histogram cluster
set style fill pattern 3 border lt -1
set key title ""
set key inside right top
set size ratio 0.618
set xlabel "" offset 0,1
set ylabel "" offset 1.5,0
set xtics rotate by 45 offset 0,0 right
set term post eps enhanced "Helvetica" 25
"""
	file.write(script)
	for file_name in file_name_list:
		file.write('set output "{0}"\n'.format(file_name[file_name.index('\\')+1:].replace('.txt','.eps')))
		file.write('plot "{0}" using 2:xticlabel(1) title ""\n'.format(file_name[file_name.index('\\')+1:]))
	file.flush()
	file.close()
		
processFeatureF1ForCate_data()
generateFeatureF1ForCate_plot()