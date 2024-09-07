.PHONY: all clean

all:
	pdflatex acl2023
	bibtex acl2023
	pdflatex acl2023
	pdflatex acl2023
	# pdflatex appendix
	# pdflatex appendix

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent acl2023.pdf *.ps *converted-to.pdf
