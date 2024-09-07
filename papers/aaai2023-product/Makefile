.PHONY: all clean

all:
	pdflatex main
	bibtex main
	pdflatex main
	pdflatex main

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent main.pdf *.ps *converted-to.pdf
