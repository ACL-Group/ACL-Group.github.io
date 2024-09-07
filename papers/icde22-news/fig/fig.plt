set terminal pdf color lw 2 solid
#set size 1.1,1.1
set origin 0,0
set key font ",15"
set key top left
set xtics rotate by 45 right
set xtics font ",15"
set ytics font ",15"
set xlabel font ",15"
set ylabel font ",15"
set title font ",20"
set grid ytics
set style histogram clustered gap 3
set style fill solid border -1
#set boxwidth 1.5 relative 

set output "hr.pdf"
set yrange [0:20]      
set ylabel "HR (%)"                                           
set xlabel "Methods"
set title ""
plot 'hr.dat' using 2:xtic(1) with histogram title 'Addressa', \
'hr.dat' using 3:xtic(1) with histogram title 'Globo', \
'hr.dat' using 4:xtic(1) with histogram lc rgb 'blue' title 'MIND' 

set output "ndcg.pdf"
set yrange [0:10]      
set ylabel "NDCG (%)"                                           
set xlabel "Methods"
set title ""
plot 'ndcg.dat' using 2:xtic(1) with histogram title 'Addressa', \
'ndcg.dat' using 3:xtic(1) with histogram title 'Globo', \
'ndcg.dat' using 4:xtic(1) with histogram lc rgb 'blue' title 'MIND'

set output "ild.pdf"
set yrange [0:1.2]      
set ylabel "ILD"                                           
set xlabel "Methods"
set title ""
plot 'ild.dat' using 2:xtic(1) with histogram title 'Addressa', \
'ild.dat' using 3:xtic(1) with histogram title 'Globo', \
'ild.dat' using 4:xtic(1) with histogram lc rgb 'blue' title 'MIND'

set output "unexp.pdf"
set yrange [0:1.2]      
set ylabel "unEXP"                                           
set xlabel "Methods"
set title ""
plot 'unexp.dat' using 2:xtic(1) with histogram title 'Addressa', \
'unexp.dat' using 3:xtic(1) with histogram title 'Globo', \
'unexp.dat' using 4:xtic(1) with histogram lc rgb 'blue' title 'MIND'
