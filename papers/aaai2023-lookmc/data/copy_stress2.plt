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
set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Voice" 5)

file = "data2.dat"
#file = "test.txt"

set style data histogram
set style histogram clustered gap 2

set datafile separator ','
#set key autotitle columnhead
#set xtics rotate by 0
#set yrange [50: 100]
#set xtics center offset 0, -1
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

set xtics center offset 0, -1
set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Voice" 5)
set yrange [50: 100]
plot file every ::1::7 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                 "" every ::1::7 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                 "" every ::1::7 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                 "" every ::1::7 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                 "" every ::1::7 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 


set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Voice" 5)
#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
set yrange [40: 100]
plot file every ::9::15 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                 "" every ::9::15 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                 "" every ::9::15 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                 "" every ::9::15 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                 "" every ::9::15 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 
set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Voice" 5)
#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
set yrange [40: 100]
plot file every ::17::23 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                 "" every ::17::23 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                 "" every ::17::23 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                 "" every ::17::23 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                 "" every ::17::23 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 



#COPA

set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Voice" 3)
set yrange [40: 100]
plot file every ::25::29 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                "" every ::25::29 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                "" every ::25::29 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                "" every ::25::29 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                "" every ::25::29 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"

#set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Adv" 3, "Voice" 4, "Syn" 5)
set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Voice" 3)
set yrange [20: 100]
plot file every ::31::35 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                "" every ::31::35 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                "" every ::31::35 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                "" every ::31::35 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                "" every ::31::35 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"

#set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Adv" 3, "Voice" 4, "Syn" 5)
set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Voice" 3)
set yrange [40: 100]
plot file every ::37::41 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                "" every ::37::41 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                "" every ::37::41 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                "" every ::37::41 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                "" every ::37::41 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"

# ARCT
#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Voice" 5)
set yrange [30: 100]
plot file every ::43::49 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                 "" every ::43::49 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                 "" every ::43::49 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                 "" every ::43::49 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                 "" every ::43::49 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 

#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
set yrange [20: 100]
plot file every ::51::57 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                 "" every ::51::57 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                 "" every ::51::57 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                 "" every ::51::57 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                 "" every ::51::57 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 

set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Voice" 5)
set yrange [20: 100]
plot file every ::59::65 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                 "" every ::59::65 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                 "" every ::59::65 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                 "" every ::59::65 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                 "" every ::59::65 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M" 

##RECLOR
#set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Adv" 4, "Voice" 5, "Syn" 6)
set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Voice" 4)
set yrange [0: 100]
set xtics center offset 0, -1
plot file every ::67::72 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
                 "" every ::67::72 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
                 "" every ::67::72 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
                 "" every ::67::72 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
                 "" every ::67::72 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"
##
##set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Adv" 4, "Voice" 5, "Syn" 6)
#set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Voice" 4)
#set yrange [0: 100]
#set xtics center offset 0, -1
#plot file every ::74::79 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                 "" every ::74::79 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                 "" every ::74::79 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                 "" every ::74::79 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                 "" every ::74::79 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"
#
#set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Voice" 4)
#set yrange [0: 100]
#set xtics center offset 0, -1
#plot file every ::81::86 using 2 w lp  lw 3.4 pt 2 ps 1.3 title "w/o", \
#                 "" every ::81::86 using 3 w lp  lw 3.4 pt 4 ps 1.3 title "+B",\
#                 "" every ::81::86 using 4 w lp  lw 3.4 pt 6 ps 1.3 title "+C",\
#                 "" every ::81::86 using 5 w lp  lw 3.4 pt 8 ps 1.3 title "+M",\
#                 "" every ::81::86 using 6 w lp  lw 3.4 pt 12 ps 1.3 lc 'red' title "+C+M"

