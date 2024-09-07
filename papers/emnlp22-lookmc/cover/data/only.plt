#set term context standalone size 12cm,8cm header '\usemodule[zhfonts]'
set encoding utf8
#set terminal pdfcairo size 500,450 enhanced font 'Verdana,9'
#set terminal pdf color enhanced size 4,3 lw 1 
#set size 1,1
#set terminal pdfcairo enhanced font 'Verdana,10'
#set size square 
#set size 0.9, 0.9
set origin 0,0
set lmargin 7
set rmargin 8
set tmargin 6
set bmargin 8
set key font ",20"
set xtics font ",15"
set ytics font ",20"
set xlabel font ",22"
set ylabel font ",25"
set title font ",10"

#set output 'copa.pdf'
#set key left reverse Left spacing 1.2
#set key center at 1.4, 0.37
set key top outside horizontal center
#set xlabel "Accuracy Test"
#set ylabel "Distribution"

#set xtics ('Neg+' 1, 'Neg-' 2, 'NER' 3, 'PR' 4, 'PI' 5, "Adv" 6, "Voice" 7)
set xtics ('BT(ROC)' 0, 'BT(COPA)' 1, 'BT(ARCT)' 2, 'BT(RECLOR)' 3, 'XL(ROC)' 4, "XL(COPA)" 5, "XL(ARCT)" 6, "XL(RECLOR)" 7, "RB(ROC)" 8, "RB(COPA)" 9, "RB(ARCT)" 10, "RB(RECLOR)" 11)

file = "only.dat"
#file = "test.txt"

set style data histogram
set style histogram clustered gap 2

set datafile separator ','
#set key autotitle columnhead
set xtics rotate by 40
set yrange [20: 80]
set xtics center offset 1, -4
plot file  using 1 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                 ""  using 2 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                 ""  using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+C",\
                 ""  using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+M",\
                 ""  using 5 w lp  lw 3.4 pt 8 ps 1.3 lc "red" title "+C+M"

