all:
	latex paper
	bibtex paper
	latex paper
	latex paper
	latex paper
	dvipdfm -p letter paper.dvi

clean: 
	rm -f *.bbl *.blg *.aux *.dvi *.log *.ent *.pdf
