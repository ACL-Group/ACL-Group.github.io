all:
	lualatex 论文
	#bibtex 论文
	lualatex 论文
	lualatex 论文
	#pdflatex appendix
	#pdflatex appendix

#check: checklist.tex
#    pdflatex checklist
#    pdflatex checklist

rebuttal: rebuttal.tex 
	pdflatex cover
	pdflatex cover

response: appendix.tex 
	pdflatex appendix
	pdflatex appendix

clean: 
	rm -f *.out *.bbl *.synctex.gz *.blg *.aux *.dvi *.log *.ent paper.pdf *.ps *converted-to.pdf
