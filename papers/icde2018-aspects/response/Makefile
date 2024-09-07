all:
	pdflatex response
	# bibtex response
	pdflatex response
	pdflatex response
#	dvipdfm -p letter response.dvi
#	dvips -t letter -Ppdf response.dvi -o response.ps
#	ps2pdf response.ps;rm -rf response.ps

#pictures:
#	bmeps -c search_kiwi.jpg search_kiwi.eps

clean: 
	rm -f *.synctex.gz *.bbl *.blg *.aux *.dvi *.log *.ent response.pdf *.ps *converted-to.pdf *.out
