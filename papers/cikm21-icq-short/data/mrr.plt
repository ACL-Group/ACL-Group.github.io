#set term context standalone size 12cm,8cm header '\usemodule[zhfonts]'
#set terminal pdfcairo size 500,450 enhanced font 'Verdana,9'
set terminal pdf color enhanced size 4,2 lw 1 font 'Verdana,15'
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



set style data histogram
set style histogram clustered gap 2

set datafile separator ','
#set key autotitle columnhead
set xtics rotate by -30

set yrange [0.0:0.15]
file = "mrr_res/acc_COPA.csv"
set output 'acc_copa.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.1]
file = "mrr_res/dist_COPA.csv"
set output 'dist_copa.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.1]
file = "mrr_res/acc_ARCT.csv"
set output 'acc_arct.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"


set yrange [0.0:0.1]
file = "mrr_res/dist_ARCT.csv"
set output 'dist_arct.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.1]
file = "mrr_res/acc_ARCT2.csv"
set output 'acc_arct2.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.05]
file = "mrr_res/dist_ARCT2.csv"
set output 'dist_arct2.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.02]
file = "mrr_res/acc_ROC.csv"
set output 'acc_roc.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.02]
file = "mrr_res/dist_ROC.csv"
set output 'dist_roc.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.1]
file = "mrr_res/acc_RECLOR.csv"
set output 'acc_reclor.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.02]
file = "mrr_res/dist_RECLOR.csv"
set output 'dist_reclor.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.002]
file = "mrr_res/acc_QNLI.csv"
set output 'acc_qnli.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.002]
file = "mrr_res/dist_QNLI.csv"
set output 'dist_qnli.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.01]
file = "mrr_res/acc_MNLI_MATCHED.csv"
set output 'acc_mnli.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.005]
file = "mrr_res/dist_MNLI_MATCHED.csv"
set output 'dist_mnli.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.02]
file = "mrr_res/acc_SNLI.csv"
set output 'acc_snli.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
     file u ($5):xtic(1) fs s 1 t "CP"

set yrange [0.0:0.01]
file = "mrr_res/dist_SNLI.csv"
set output 'dist_snli.pdf'
plot file u ($2):xtic(1) fs p 2 t "LMI", \
     file u ($3):xtic(1) fs s 1 t "PMI", \
     file u ($4):xtic(1) fs s 1 t "Freq", \
