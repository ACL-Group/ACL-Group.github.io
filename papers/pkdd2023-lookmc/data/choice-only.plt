#set term context standalone size 12cm,8cm header '\usemodule[zhfonts]'
set encoding utf8
set terminal pdfcairo enhanced font 'Verdana,10'
#set terminal pdf color enhanced size 4,3 lw 1 
set size 1,1
#set terminal pdfcairo enhanced font 'Verdana,10'
#set size square 
#set size 0.9, 0.9
set origin 0,0
set lmargin 10
set rmargin 7
set tmargin 3
set bmargin 4
set key font ",13"
set xtics font ",12"
set ytics font ",15"
set xlabel font ",13"
set ylabel font ",13"
set title font ",12"

#set key left reverse Left spacing 1.2
#set key center at 1.4, 0.37
set key top outside horizontal center
#set key bottom
# set key left
#set xlabel "Accuracy Test"
#set ylabel "Distribution"

#set xtics ('Neg+' 1, 'Neg-' 2, 'NER' 3, 'PR' 4, 'PI' 5, "Adv" 6, "Voice" 7)

file = "only.dat"
file2 = "only2.dat"
#file = "test.txt"

set style data histogram
set style histogram clustered gap 2

set datafile separator ','
#set key autotitle columnhead
#set xtics rotate by 0
#set yrange [50: 100]
#set xtics center offset 0, -1
#plot file every ::2::10 using 2 w lp  lw 3 pt 2 ps 1.0 notitle, \
#                 "" every ::1::10 using 3 w lp  lw 3 pt 4 ps 1.0 notitle,\
#                 "" every ::1::10 using 4 w lp  lw 3 pt 6 ps 1.0 notitle,\
#                 "" every ::1::10 using 5 w lp  lw 3 pt 8 ps 1.0 notitle,\
#                 "" every ::1::10 using 6 w lp  lw 3 pt 12 ps 1.0 notitle
#set term pdfcairo
#set output 'roc_bert.pdf'
#replot
#unset output
#unset terminal

set output 'choice-only.pdf'
set xtics center offset 0, -1
set xtics rotate by 30
set xtics ('BT(ROC)' 0, 'BT(COPA)' 1, 'BT(ARCT)' 2, 'BT(RECLOR)' 3, 'XL(ROC)' 4, "XL(COPA)" 5, "XL(ARCT)" 6, "XL(RECLOR)" 7, "RB(ROC)" 8, "RB(COPA)" 9, "RB(ARCT)" 10, "RB(RECLOR)" 11)
set yrange [25: 80]
plot file every ::1::13 using 2 w lp  lw 2.6 pt 2 ps 1.0 title "w/o", \
                 "" every ::1::13 using 3 w lp  lw 2.6 pt 4 ps 1.0 title "+B",\
                 "" every ::1::13 using 4 w lp  lw 2.6 pt 6 ps 1.0 title "+C",\
                 "" every ::1::13 using 5 w lp  lw 2.6 pt 8 ps 1.0 title "+M", \
                 "" every ::1::13 using 6 w lp  lw 2.6 pt 12 ps 1.0 lc 'red' title "+C+M" 
set output


set output 'only2.pdf'
set xtics center offset 0, -1
set xtics rotate by 30
set xtics ('BT(ROC)' 0, 'BT(COPA)' 1, 'BT(ARCT)' 2, 'BT(RECLOR)' 3, 'XL(ROC)' 4, "XL(COPA)" 5, "XL(ARCT)" 6, "XL(RECLOR)" 7, "RB(ROC)" 8, "RB(COPA)" 9, "RB(ARCT)" 10, "RB(RECLOR)" 11)
set yrange [-10:10]
#plot file2 every ::1::13 using 3 w lp  lw 3 pt 4 ps 1.0 title "+B",\
plot file2 every ::1::13 using 2 w lp  lw 3 pt 2 ps 1.0 title "w/o", \
                 "" every ::1::13 using 3 w lp  lw 3 pt 4 ps 1.0 title "+B",\
                 "" every ::1::13 using 4 w lp  lw 3 pt 6 ps 1.0 title "+C",\
                 "" every ::1::13 using 5 w lp  lw 3 pt 8 ps 1.0 title "+M", \
                 "" every ::1::13 using 6 w lp  lw 3 pt 12 ps 1.0 lc 'red' title "+C+M" 
set output
