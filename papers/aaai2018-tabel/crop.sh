#########################################################################
# File Name: crop.sh
# Author: Xusheng Luo
# mail: freefish_6174@126.com
# Created Time: 2017-02-19
#########################################################################
#!/bin/bash

#epstopdf $1.eps
pdfcrop $1.pdf
pdf2ps $1-crop.pdf $1-crop.eps
