all:	*.cls *.tex 
	latex paper
	latex paper
	bibtex paper
	latex paper
	latex paper
	dvipdfm -p letter paper.dvi

clean:
	rm -f *.dvi *.bbl *.aux *.log *.blg
	rm -f paper.ps paper.pdf
