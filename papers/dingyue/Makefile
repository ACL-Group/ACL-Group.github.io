all:
	pdflatex dingyue
	bibtex dingyue
	pdflatex dingyue
	pdflatex dingyue
#	dvipdfm -p letter dingyue.dvi
#	dvips -t letter -Ppdf dingyue.dvi -o dingyue.ps
#	ps2pdf dingyue.ps;rm -rf dingyue.ps

#pictures:
#	bmeps -c search_kiwi.jpg search_kiwi.eps

clean: 
	rm -f dingyue.bbl dingyue.blg dingyue.aux dingyue.dvi dingyue.log dingyue.pdf dingyue.ps
