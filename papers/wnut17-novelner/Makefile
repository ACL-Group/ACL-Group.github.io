all:
	pdflatex paper
	pdflatex paper
	bibtex paper
	pdflatex paper
	pdflatex paper
#	dvipdfm -p letter paper.dvi
#	dvips -t letter -Ppdf paper.dvi -o paper.ps
#	ps2pdf paper.ps;rm -rf paper.ps

#pictures:
#	bmeps -c search_kiwi.jpg search_kiwi.eps

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent paper.pdf *.ps *converted-to.pdf
