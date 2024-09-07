all:
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper

appendix:
	pdflatex appendix
	bibtex appendix
	pdflatex appendix
	pdflatex appendix

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent paper.pdf appendix.pdf *.ps *converted-to.pdf
