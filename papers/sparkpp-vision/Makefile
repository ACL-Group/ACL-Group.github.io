all:
	pdflatex paper.tex
	bibtex paper
	pdflatex paper.tex
	pdflatex paper.tex

clean: 
	rm -f *.bbl *.blg *.aux *.dvi *.log *.ent paper.pdf *.ps
