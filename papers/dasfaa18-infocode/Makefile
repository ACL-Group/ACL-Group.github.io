all:
	pdflatex infocode.tex
	bibtex infocode
	pdflatex infocode.tex
	pdflatex infocode.tex
#	dvipdfm -p letter infocode.dvi

clean:
	rm -f *.aux *.dvi *.bbl *.blg infocode.pdf

