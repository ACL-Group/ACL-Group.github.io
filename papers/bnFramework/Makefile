all:
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper
#	pdflatex paper
#	dvipdfm -p letter paper.dvi
#	dvips -t letter -Ppdf paper.dvi -o paper.ps
#	ps2pdf paper.ps;rm -rf paper.ps

clean: 
	rm -f *.bbl *.bst *.blg *.aux *.dvi *.log *.ent paper.pdf paper.ps
