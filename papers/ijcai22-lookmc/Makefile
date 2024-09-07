all:
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper
	pdflatex appendix
	pdflatex appendix

rebuttal: rebuttal.tex 
	pdflatex cover
	pdflatex cover

response: response.tex 
	pdflatex response
	pdflatex response

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent paper.pdf *.ps *converted-to.pdf
