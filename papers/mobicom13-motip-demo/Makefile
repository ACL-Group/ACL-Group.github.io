all:
	latex paper
	bibtex paper
	latex paper
	latex paper
#	dvipdf paper.dvi
	dvips -t letter -Ppdf paper.dvi -o paper.ps
	ps2pdf paper.ps
dvi:
	latex paper
	bibtex paper
	latex paper
	latex paper
#pictures:
#	bmeps -c search_kiwi.jpg search_kiwi.eps

clean: 
	rm -f *.bbl *.blg *.aux *.dvi *.log *.ent *.pdf *.ps
