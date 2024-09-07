set terminal postscript eps color lw 2 solid
set output "isa.eps"
set size 2.0,1.1
set origin 0,0
set key font ",26"
set tics font ",26"
set xlabel font ",30"
set ylabel font ",30"
set title font ",36"


set multiplot layout 2,1 rowsfirst

set size 1.0,1.0
set origin 0,0.03
set yrange [0:0.6]      
set ytic 0.2                                          
set xtics ('10'1, '20'2, '40'3, '60'4, '80'5, '100'6, '200'7) offset 0, -0.5
set xlabel "1:N" offset 0, -1.5
set ylabel "MAP" 
set title ""
plot "isa_ret.txt" using 1:2 title "" w lp lc 7 lw 2 pt 5 ps 2


set size 1.0,1.0
set origin 1,0.03
set yrange [0.3:0.6]      
set ytic 0.1       
set xtics offset 2.5, -0.5 
set xlabel "sampling strategy"               
set title ""
set style data histograms
set style histogram cluster
set boxwidth 1
set style fill solid 0.25 border
plot "isa_ret2.txt" using 2:xtic(1) title '' lc rgb "turquoise"

unset multiplot

set output
