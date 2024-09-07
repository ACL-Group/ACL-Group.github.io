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
set tmargin 2
set bmargin 4
set key font ",20"
set xtics font ",28"
set ytics font ",28"
set xlabel font ",28"
set ylabel font ",25"
set title font ",16"

#set key left reverse Left spacing 1.2
#set key center at 1.4, 0.37
set key top outside horizontal center
#set key bottom
# set key left
#set xlabel "Accuracy Test"
#set ylabel "Distribution"

#set xtics ('Neg+' 1, 'Neg-' 2, 'NER' 3, 'PR' 4, 'PI' 5, "Adv" 6, "Voice" 7)
set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Voice" 5)

file = "stress_emnlp.dat"
#file = "test.txt"

set style data histogram
set style histogram clustered gap 2

set datafile separator ','
#set key autotitle columnhead
#set xtics rotate by 0
#set yrange [50: 100]
#set xtics center offset 0, -1
#plot file every ::2::10 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
#                 "" every ::1::10 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
#                 "" every ::1::10 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
#                 "" every ::1::10 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
#                 "" every ::1::10 using 6 w lp  lw 4.5 pt 12 ps 1.0 notitle
#set term pdfcairo
#set output 'roc_bert.pdf'
#replot
#unset output
#unset terminal

set output 'roc_bert.pdf'
set xtics center offset 0, -1
set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Voice" 5)
set yrange [50: 100]
plot file every ::1::7 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                 "" every ::1::7 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                 "" every ::1::7 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                 "" every ::1::7 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                 "" every ::1::7 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle 
set output

set output 'roc_xlnet.pdf'
set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Voice" 5)
#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
set yrange [40: 100]
plot file every ::9::15 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                 "" every ::9::15 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                 "" every ::9::15 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                 "" every ::9::15 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                 "" every ::9::15 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle 
set output

set output 'roc_roberta.pdf'

set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Voice" 5)
#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
set yrange [40: 100]
plot file every ::17::23 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                 "" every ::17::23 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                 "" every ::17::23 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                 "" every ::17::23 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                 "" every ::17::23 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle 


set output

#COPA

set output 'copa_bert.pdf'

set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Voice" 3)
set yrange [40: 100]
plot file every ::25::29 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                "" every ::25::29 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                "" every ::25::29 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                "" every ::25::29 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                "" every ::25::29 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle

set output

set output 'copa_xlnet.pdf'

#set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Adv" 3, "Voice" 4, "Syn" 5)
set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Voice" 3)
set yrange [20: 100]
plot file every ::31::35 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                "" every ::31::35 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                "" every ::31::35 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                "" every ::31::35 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                "" every ::31::35 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle

set output

set output 'copa_roberta.pdf'

#set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Adv" 3, "Voice" 4, "Syn" 5)
set xtics ('Neg+' 0, 'PR' 1, 'PI' 2, "Voice" 3)
set yrange [50: 100]
plot file every ::37::41 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                "" every ::37::41 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                "" every ::37::41 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                "" every ::37::41 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                "" every ::37::41 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle

set output

# ARCT

set output 'arct_bert.pdf'
#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Voice" 5)
set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Voice" 4)
set yrange [10: 100]
plot file every ::43::49 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                 "" every ::43::48 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                 "" every ::43::48 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                 "" every ::43::48 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                 "" every ::43::48 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle 
set output

set output 'arct_xlnet.pdf'

#set xtics ('Neg+' 0, 'Neg-' 1, 'NER' 2, 'PR' 3, 'PI' 4, "Adv" 5, "Voice" 6, "Syn" 7)
set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Voice" 4)
set yrange [10: 100]
plot file every ::50::55 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                 "" every ::50::55 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                 "" every ::50::55 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                 "" every ::50::55 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                 "" every ::50::55 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle 

set output

set output 'arct_roberta.pdf'
set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Voice" 4)
set yrange [10: 100]
plot file every ::57::62 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                 "" every ::57::62 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                 "" every ::57::62 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                 "" every ::57::62 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                 "" every ::57::62 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle 

set output

##RECLOR
set output 'reclor_bert.pdf'

#set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Adv" 4, "Voice" 5, "Syn" 6)
#set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Voice" 4)
set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Voice" 4)
set yrange [0: 80]
#set xtics center offset 0, -1
plot file every ::64::69 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                 "" every ::64::69 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                 "" every ::64::69 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                 "" every ::64::69 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                 "" every ::64::69 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle
set output

set output 'reclor_xlnet.pdf'
#
#set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Adv" 4, "Voice" 5, "Syn" 6)
set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Voice" 4)
set yrange [0: 80]
#set xtics center offset 0, -1
plot file every ::71::76 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                 "" every ::71::76 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                 "" every ::71::76 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                 "" every ::71::76 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                 "" every ::71::76 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle

set output

set output 'reclor_roberta.pdf'
set xtics ('Neg+' 0, 'Neg-' 1, 'PR' 2, 'PI' 3, "Voice" 4)
set yrange [0: 80]
#set xtics center offset 0, -1
plot file every ::78::83 using 2 w lp  lw 4.5 pt 2 ps 1.0 notitle, \
                 "" every ::78::83 using 3 w lp  lw 4.5 pt 4 ps 1.0 notitle,\
                 "" every ::78::83 using 4 w lp  lw 4.5 pt 6 ps 1.0 notitle,\
                 "" every ::78::83 using 5 w lp  lw 4.5 pt 8 ps 1.0 notitle,\
                 "" every ::78::83 using 6 w lp  lw 4.5 pt 12 ps 1.0 lc 'red' notitle
set output
