all:
	latex paper.tex
	bibtex paper
	latex paper.tex
	latex paper.tex
	dvipdf paper.dvi

clean: 
	rm -f *.bbl *.blg *.aux *.dvi *.log *.ent *.ps *.spl
