.PHONY: all clean

all:
	pdflatex sample-sigconf
	bibtex sample-sigconf
	pdflatex sample-sigconf
	pdflatex sample-sigconf

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent acl2023.pdf *.ps *converted-to.pdf
