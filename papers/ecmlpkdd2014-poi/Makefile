all:
	latex template
	latex template
	bibtex template
	latex template
	latex template
	dvipdfm -p letter template.dvi
#	dvips -t letter -Ppdf template.dvi -o template.ps
#	ps2pdf template.ps;rm -f template.ps

#pictures:
#	bmeps -c search_kiwi.jpg search_kiwi.eps

clean: 
	rm -f *.bbl *.blg *.aux *.dvi *.log *.ent *.pdf *.ps
