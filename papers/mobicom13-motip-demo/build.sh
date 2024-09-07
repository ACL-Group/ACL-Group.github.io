#!/bin/bash
bibtex paper
latex paper.tex
dvipdf paper.dvi output.pdf
