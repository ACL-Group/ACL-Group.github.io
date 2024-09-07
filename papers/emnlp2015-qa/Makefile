all:
	latex paper
	bibtex paper
	latex paper
	latex paper
#	dvipdfm -p letter paper.dvi
	dvips -t letter -Ppdf paper.dvi -o paper.ps
	ps2pdf paper.ps;rm -rf paper.ps

#pictures:
#	bmeps -c search_kiwi.jpg search_kiwi.eps

clean: 
	rm -f *.bbl *.blg *.aux *.dvi *.log *.ent *.pdf *.ps
