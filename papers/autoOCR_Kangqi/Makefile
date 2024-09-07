all:
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper
	# dvipdfm -p letter paper.dvi

clean: 
	rm -f *.bbl *.blg *.aux *.dvi *.log *.ent *.pdf
