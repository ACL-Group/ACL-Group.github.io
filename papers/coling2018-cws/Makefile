all:
	make clean
	pdflatex --shell-escape -interaction=nonstopmode paper
	bibtex paper
	pdflatex --shell-escape -interaction=nonstopmode paper
	pdflatex --shell-escape -interaction=nonstopmode paper
	make clean
view:
	okular coling2018.pdf
clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent *.ps *converted-to.pdf *.fdb_latexmk *.fls