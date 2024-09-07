.PHONY: all clean

all:
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent paper.pdf *.ps *converted-to.pdf
