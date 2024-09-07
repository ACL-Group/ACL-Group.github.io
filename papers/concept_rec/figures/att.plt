set terminal postscript eps color lw 2 solid
set output "att.eps"
set size 1.0,1.0
set origin 0,0

set multiplot layout 2,2 rowsfirst

set size 0.5,0.5
set origin 0,0.5
set xlabel "(a) Metapath" font ",14"
set ylabel "Attteion Weight" font ",14"
#set xtics rotate by 15 offset -1.5,-0.5
set yrange [0:0.5]
set ytics 0.1
set mytics 5
set grid
set boxwidth 0.9 absolute
set style fill solid 1.00 border -1
set style histogram clustered gap 1 title offset character 0, 0, 0
set style data histograms
plot 'att_p.txt' using 2:xtic(1) notitle col linecolor rgb "#FFC0CB" 

set size 0.5,0.5
set origin 0.5,0.5
set xlabel "\n(b) User Profile"
set xtics rotate by 15 offset -3.25,-1.5
set ylabel "Attteion Weight"
set yrange [0:0.6]
set ytics 0.1
set mytics 5
set grid
set boxwidth 0.9 absolute
set style fill solid 1.00 border -1
set style histogram clustered gap 1 title offset character 0, 0, 0
set style data histograms
plot 'att_u.txt' using 2:xtic(1) notitle col linecolor rgb "#FFC0CB"

set size 0.5,0.5
set origin 0,0
set xlabel "\n (c) Concept Schema"
set ylabel "Attteion Weight"
set xtics rotate by 15 offset -2.5,-1.00
set yrange [0:0.7]
set ytics 0.1
set mytics 5
set grid
set style fill solid 1.00 border -1
set style histogram clustered gap 1 title offset character 0, 0, 0
set style data histograms
plot 'att_c.txt' using 2:xtic(1) notitle col lc rgb "#FFC0CB"

set size 0.5,0.5
set origin 0.5,0
set ylabel "Attteion Weight"
set xlabel "\n (d)"
set yrange [0:1]
set ytics 0.25
set xtics rotate by 5 offset -2.5,-1.00
set mytics 5
set grid
set style fill solid 1.00 border -1
set style histogram clustered gap 1 title offset character 0, 0, 0
set style data histograms
plot 'att_g.txt' using 2:xtic(1) notitle col lc "#FFE4B5"

unset multiplot

set output
