#set terminal pdfcairo size 500,450 enhanced font 'Verdana,9'
#set size 1,1
set encoding utf8
set xlabel font ",28"
set ylabel font ",28"
set title font ",35"
set key font ",25"
set yrange [0:100]
set ylabel "Percentage (%)"
set xlabel "Models"
set output "end.png"
unset tics
set xtics font ",25"
set ytics font ",25"

set ytics 0,10,100

set origin 0,0
set lmargin 14
set rmargin 3
set tmargin 2
set bmargin 6
set boxwidth 1
set xlabel offset 0,-2
set ylabel offset -4,0
set xtics ('Rf' 0, 'FT' 1, 'ES' 2, 'BT' 3, 'RB' 4)

#set xtics center offset 0,-1
set style histogram clustered gap 1   #//gap 2表示裂隙宽等于矩形宽度的2倍
set style fill pattern border -1 #//fill solid表示完全填充柱体，后面跟0-1的参数，1表示完全填充，border 表示柱体的边线颜色，-1表示黑色。这里还可以加参数pattern
#set style fill pattern 1
set palette rgbformulae 7,5,15
#plot 'no_mnli.txt' using 2 with histogram ls 3 fill pattern 3 title 'Contradiction', \
#    "" using 3 with histogram ls 2 fill pattern 3 title 'Neutral', \
#    "" using 4 with histogram ls 4 fill pattern 3 title 'Entailment'
#plot 'above_arct.txt' using 2 with histogram ls 3 fill pattern 3 title 'True', \
#    "" using 3 with histogram ls 4 fill pattern 3 title 'False'
#plot 'threw_roc.txt' using 2 with histogram ls 3 fill pattern 3 title 'True', \
#   "" using 3 with histogram ls 4 fill pattern 3 title 'False'
plot 'speaking_snli.txt' using 2 with histogram ls 3 fill pattern 3 title 'Contradiction', \
    "" using 3 with histogram ls 2 fill pattern 3 title 'Neutral', \
    "" using 4 with histogram ls 4 fill pattern 3 title 'Entailment'
