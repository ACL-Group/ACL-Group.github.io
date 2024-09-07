all:
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper
	pdflatex appendix
	pdflatex appendix

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent paper.pdf *.ps *converted-to.pdf appendix.pdf
