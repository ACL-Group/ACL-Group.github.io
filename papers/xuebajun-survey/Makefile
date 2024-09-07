all:
	latex paper
	latex paper
	bibtex paper
#	latex paper
	latex paper
	latex paper
	dvips -t letter paper.dvi 
	ps2pdf paper.ps paper.pdf
#        dvipdfm -p letter paper.dvi
clean:
	rm -f *.bbl *.blg *.aux *.dvi *.log *.ent *.pdf *.gz *.fdb_latexmk
