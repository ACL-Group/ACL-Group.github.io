reset
unset log
unset label
set xlabel 'Number of dining philosophers'
set xtics (10,20,30,40,50)
set key left top
#
set ylabel 'Memory cost (MB)'
set terminal postscript eps "Helvetica" 25
set out 'dp-mem.eps'
plot 'dp.dat' using 1:8 title 'Average' with linespoints lw 4 ps 3, 'dp.dat' using 1:9 title 'Maximum' with linespoints lw 4 ps 3, 'dp.dat' using 1:10 title 'Minimum' with linespoints lw 4 ps 3

reset
unset log
unset label
set xlabel 'Number of dining philosophers'
set xtics (10,20,30,40,50)
set key left top
#
set ylabel 'Maximum number of worlds'
set terminal postscript eps "Helvetica" 25
set out 'dp-world.eps'
plot 'dp.dat' using 1:5 title 'Average' with linespoints lw 4 ps 3, 'dp.dat' using 1:6 title 'Maximum' with linespoints lw 4 ps 3, 'dp.dat' using 1:7 title 'Minimum' with linespoints lw 4 ps 3

reset
unset log
unset label
set xlabel 'Number of dining philosophers'
set xtics (10,20,30,40,50)
set key left top
#
set ylabel 'CPU time (sec)'
set terminal postscript eps "Helvetica" 25
set out 'dp-cpu.eps'
plot 'dp.dat' using 1:2 title 'Average' with linespoints lw 4 ps 3, 'dp.dat' using 1:3 title 'Maximum' with linespoints lw 4 ps 3, 'dp.dat' using 1:4 title 'Minimum' with linespoints lw 4 ps 3

reset
unset log
unset label
set key left top
#
set xlabel '% time savings'
set ylabel 'Number of agents'
set xtics (0,10,20,30,40,50,60,70,80,90,100)
set terminal postscript eps "Helvetica" 25
set out 'dp-exit.eps'
plot "dp-exit.dat" u 1:2 with boxes title "" lw 4
