#set term context standalone size 12cm,8cm header '\usemodule[zhfonts]'
set encoding utf8
#set terminal pdfcairo size 500,450 enhanced font 'Verdana,9'
#set terminal pdf color enhanced size 4,3 lw 1 
#set size 1,1
#set terminal pdfcairo enhanced font 'Verdana,10'
#set size square 
#set size 0.9, 0.9
set origin 0,0
set lmargin 10
set rmargin 6
set tmargin 6
set bmargin 4
set key font ",20"
set xtics font ",25"
set ytics font ",25"
set xlabel font ",25"
set ylabel font ",25"
set title font ",16"

#set output 'copa.pdf'
#set key left reverse Left spacing 1.2
#set key center at 1.4, 0.37
set key top outside horizontal center
#set key bottom
# set key left
#set xlabel "Accuracy Test"
#set ylabel "Distribution"

#set xtics ('Neg+' 1, 'Neg-' 2, 'NER' 3, 'PR' 4, 'PI' 5, "Adv" 6, "Voice" 7)
set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)

file = "data.dat"
#file = "test.txt"

set style data histogram
set style histogram clustered gap 2

set datafile separator ','
#set key autotitle columnhead
#set xtics rotate by 0
#set yrange [50: 100]
#set xtics center offset 1, -1
#plot file every ::2::10 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                 "" every ::1::10 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                 "" every ::1::10 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                 "" every ::1::10 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                 "" every ::1::10 using 6 w lp  lw 3.4 pt 12 ps 1.3 title "+C+M"
#set term pdfcairo
#set output 'roc_bert.pdf'
#replot
#unset output
#unset terminal

set xtics center offset 1, -1
set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
set yrange [50: 100]
plot file every ::1::9 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                 "" every ::1::9 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                 "" every ::1::9 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                 "" every ::1::9 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                 "" every ::1::9 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 


set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
set yrange [40: 100]
plot file every ::11::19 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                 "" every ::11::19 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                 "" every ::11::19 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                 "" every ::11::19 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                 "" every ::11::19 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 

#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
#set yrange [40: 100]
#plot file every ::21::29 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                 "" every ::21::29 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                 "" every ::21::29 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                 "" every ::21::29 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                 "" every ::21::29 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 

##COPA

#set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Adv" 3, "Voice" 4, "Syn" 5)
#set yrange [40: 100]
#plot file every ::31::37 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                "" every ::31::37 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                "" every ::31::37 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                "" every ::31::37 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                "" every ::31::37 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"
#
#set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Adv" 3, "Voice" 4, "Syn" 5)
#set yrange [20: 100]
#plot file every ::39::45 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                "" every ::39::45 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                "" every ::39::45 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                "" every ::39::45 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                "" every ::39::45 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"
#
#set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Adv" 3, "Voice" 4, "Syn" 5)
#set yrange [40: 100]
#plot file every ::47::53 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                "" every ::47::53 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                "" every ::47::53 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                "" every ::47::53 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                "" every ::47::53 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"
#
## ARCT
#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
#set yrange [30: 100]
#plot file every ::55::63 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                 "" every ::55::63 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                 "" every ::55::63 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                 "" every ::55::63 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                 "" every ::55::63 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 
#
##set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
#set yrange [20: 100]
#plot file every ::65::73 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                 "" every ::65::73 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                 "" every ::65::73 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                 "" every ::65::73 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                 "" every ::65::73 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 
#
#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
#set yrange [20: 100]
#plot file every ::75::83 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                 "" every ::75::83 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                 "" every ::75::83 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                 "" every ::75::83 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                 "" every ::75::83 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 
#
###RECLOR
#set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Adv" 4, "Voice" 5, "Syn" 6)
#set yrange [0: 100]
#set xtics center offset 1, -1
#plot file every ::85::92 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                 "" every ::85::92 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                 "" every ::85::92 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                 "" every ::85::92 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                 "" every ::85::92 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"
##
#set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Adv" 4, "Voice" 5, "Syn" 6)
#set yrange [0: 100]
#set xtics center offset 1, -1
#plot file every ::94::101 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                 "" every ::94::101 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                 "" every ::94::101 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                 "" every ::94::101 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                 "" every ::94::101 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"
#
#set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Adv" 4, "Voice" 5, "Syn" 6)
#set yrange [0: 100]
#set xtics center offset 1, -1
#plot file every ::103::110 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                 "" every ::103::110 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                 "" every ::103::110 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                 "" every ::103::110 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                 "" every ::103::110 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"
#
