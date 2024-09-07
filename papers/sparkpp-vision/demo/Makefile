all:
	pdflatex paper.tex
	bibtex paper
	pdflatex paper.tex
	pdflatex paper.tex
	mv paper.pdf inferspark-demo.pdf

clean: 
	rm -f *.bbl *.blg *.aux *.dvi *.log *.ent inferspark-demo.pdf *.ps
