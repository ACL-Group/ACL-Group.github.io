all:
	latex paper
	latex paper
	bibtex paper
	latex paper
	latex paper
	dvipdfm -p letter paper.dvi
	dvips -t letter -Ppdf paper.dvi -o paper.ps
	ps2pdf paper.ps

clean: 
# rm -f *.bbl *.blg *.aux *.dvi *.log *.ent paper.pdf *.ps
	rm -f *.bbl *.blg *.aux *.dvi *.log *.ent *.ps *.spl *.pdf
