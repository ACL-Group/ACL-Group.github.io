.PHONY: all clean

all:
	pdflatex rebuttal
	bibtex rebuttal
	pdflatex rebuttal
	pdflatex rebuttal

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent paper.pdf *.ps *converted-to.pdf
