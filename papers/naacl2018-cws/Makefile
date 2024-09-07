all:
	pdflatex --shell-escape -interaction=nonstopmode paper
	bibtex paper
	pdflatex --shell-escape -interaction=nonstopmode paper
	pdflatex --shell-escape -interaction=nonstopmode paper

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent paper.pdf *.ps *converted-to.pdf *.fdb_latexmk *.fls
