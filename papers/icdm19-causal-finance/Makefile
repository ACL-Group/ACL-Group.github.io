all:
	pip install Pygments
	pdflatex -shell-escape causal
	bibtex causal
	pdflatex -shell-escape causal
	pdflatex -shell-escape causal

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent paper.pdf *.ps *converted-to.pdf
