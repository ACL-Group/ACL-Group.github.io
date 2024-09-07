set terminal pdf color lw 2 solid
c1 = "#219F94"; c2 = "#C1DEAE";
c3 = "#E8E8A6"
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
set style fill solid border 0
#set boxwidth 1.5 relative 

set output "hr-ild.pdf"
set yrange [0:32]      
set ylabel "F1-(HR×ILD)"                                
set xlabel "Methods"
set title ""
plot 'hr.dat' using 2:xtic(1) with histogram lc rgb c1 title 'Adressa', \
'hr.dat' using 3:xtic(1) with histogram lc rgb c2 title 'Globo', \
'hr.dat' using 4:xtic(1) with histogram lc rgb c3 title 'MIND' 

set output "ndcg-ild.pdf"
set yrange [0:18]      
set ylabel "F1-(NDCG×ILD)"                                           
set xlabel "Methods"
set title ""
plot 'ndcg.dat' using 2:xtic(1) with histogram lc rgb c1 title 'Adressa', \
'ndcg.dat' using 3:xtic(1) with histogram lc rgb c2 title 'Globo', \
'ndcg.dat' using 4:xtic(1) with histogram lc rgb c3 title 'MIND'

set output "hr-unexp.pdf"
set yrange [0:32]      
set ylabel "F1-(HR×unEXP)"                                           
set xlabel "Methods"
set title ""
plot 'ild.dat' using 2:xtic(1) with histogram lc rgb c1 title 'Adressa', \
'ild.dat' using 3:xtic(1) with histogram lc rgb c2 title 'Globo', \
'ild.dat' using 4:xtic(1) with histogram lc rgb c3 title 'MIND'

set output "ndcg-unexp.pdf"
set yrange [0:18]      
set ylabel "F1-(NDCG×unEXP)"                                           
set xlabel "Methods"
set title ""
plot 'unexp.dat' using 2:xtic(1) with histogram lc rgb c1 title 'Adressa', \
'unexp.dat' using 3:xtic(1) with histogram lc rgb c2 title 'Globo', \
'unexp.dat' using 4:xtic(1) with histogram lc rgb c3 title 'MIND'
