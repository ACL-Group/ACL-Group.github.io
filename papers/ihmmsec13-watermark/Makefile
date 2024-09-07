all:
	latex ih058_jiang
	latex ih058_jiang
	bibtex ih058_jiang
	latex ih058_jiang
	latex ih058_jiang
#	dvipdfm -p letter ih058_jiang.dvi
	dvips -t letter -Ppdf ih058_jiang.dvi -o ih058_jiang.ps
	ps2pdf ih058_jiang.ps;rm -rf *.bbl *.blg *.aux *.dvi *.log *.ent

