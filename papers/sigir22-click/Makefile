all:
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper

rebuttal: rebuttal.tex 
	pdflatex rebuttal
	pdflatex rebuttal

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent paper.pdf *.ps *converted-to.pdf
