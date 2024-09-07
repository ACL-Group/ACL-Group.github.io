FILE=paper

.PHONY: all clean

all:
	xelatex $(FILE)
	bibtex $(FILE)
	xelatex $(FILE)
	xelatex $(FILE)

clean:
	rm $(FILE).pdf $(FILE).aux $(FILE).lof $(FILE).log $(FILE).out $(FILE).lot $(FILE).toc body/*.aux $(FILE).bbl $(FILE).blg
