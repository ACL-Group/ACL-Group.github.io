all:	dvi
		dvipdfm -p letter paper.dvi

dvi:
	latex paper
	latex paper
	bibtex paper
	latex paper
	latex paper
	
clean: 
	rm -f *.bbl *.blg *.aux *.dvi *.log *.ent *.pdf
	

