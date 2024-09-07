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
#set ylabel "MRR"

set yrange [0.0:0.2]

file = "mrr.csv"

set style data histogram
set style histogram clustered gap 2

set datafile separator ','
#set key autotitle columnhead
set xtics rotate by -30

set yrange [0.0:0.1]
set output 'reclor.pdf'
plot file u ($7):xtic(1) fs p 1 t "LMI", \
     file u ($8):xtic(1) fs p 2 t "PMI", \
     file u ($9):xtic(1) fs s 1 t "Freq", \
     file u ($10):xtic(1) fs s 1 t "CP"
set yrange [0.0:0.15]
set output 'arct.pdf'
plot file u ($12):xtic(1) fs p 1 t "LMI", \
     file u ($13):xtic(1) fs p 2 t "PMI", \
     file u ($14):xtic(1) fs s 1 t "Freq", \
     file u ($15):xtic(1) fs s 1 t "CP"
set output 'arct2.pdf'
plot file u ($17):xtic(1) fs p 1 t "LMI", \
     file u ($18):xtic(1) fs p 2 t "PMI", \
     file u ($19):xtic(1) fs s 1 t "Freq", \
     file u ($20):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.01]
set output 'roc.pdf'
plot file u ($22):xtic(1) fs p 1 t "LMI", \
     file u ($23):xtic(1) fs p 2 t "PMI", \
     file u ($24):xtic(1) fs s 1 t "Freq", \
     file u ($25):xtic(1) fs s 1 t "CP"
set yrange [0.0:0.002]
set output 'qnli.pdf'
plot file u ($27):xtic(1) fs p 1 t "LMI", \
     file u ($28):xtic(1) fs p 2 t "PMI", \
     file u ($29):xtic(1) fs s 1 t "Freq", \
     file u ($30):xtic(1) fs s 1 t "CP"
set yrange [0.0:0.02]
set output 'snli.pdf'
plot file u ($32):xtic(1) fs p 1 t "LMI", \
     file u ($33):xtic(1) fs p 2 t "PMI", \
     file u ($34):xtic(1) fs s 1 t "Freq", \
     file u ($35):xtic(1) fs s 1 t "CP"
set yrange [0.0:0.015]
set output 'mnli.pdf'
plot file u ($37):xtic(1) fs p 1 t "LMI", \
     file u ($38):xtic(1) fs p 2 t "PMI", \
     file u ($39):xtic(1) fs s 1 t "Freq", \
     file u ($40):xtic(1) fs s 1 t "CP"

