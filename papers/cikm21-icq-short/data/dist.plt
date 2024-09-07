#set term context standalone size 12cm,8cm header '\usemodule[zhfonts]'
#set terminal pdfcairo size 500,450 enhanced font 'Verdana,9'
set terminal pdf color enhanced size 4,3 lw 1 font 'Verdana,15'
#set size 1,1
#set terminal pdfcairo enhanced font 'Verdana,10'
#set size square 
set origin 0,0
set rmargin 2
#set key font ",25"
#set xtics font ",25"
#set ytics font ",22"
#set xlabel font ",25"
#set ylabel font ",25"
#set title font ",36"

#set output 'copa.pdf'
set key left reverse Left spacing 1.2
#set key center at 1.4, 0.37
set key top outside horizontal center

#set xlabel "Accuracy Test"
#set ylabel "Distribution"

set yrange [0.0:1.0]

file = "dist.csv"

set style data histogram
set style histogram clustered gap 2

set datafile separator ','
#set key autotitle columnhead
set xtics rotate by -30

set output 'roc.pdf'
plot file u ($22):xtic(1) fs p 1 t "Rf", \
     file u ($23):xtic(1) fs p 2 t "fastText", \
     file u ($24):xtic(1) fs s 1 t "ESIM", \
     file u ($25):xtic(1) fs s 1 t "BERT", \
     file u ($25):xtic(1) fs s 1 t "RoBERTa"

