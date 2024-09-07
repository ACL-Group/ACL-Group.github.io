reset
unset log
unset label
set xlabel 'Number of ticket buyer agents'
set key left top
set xtics (10,15,20,25,30,35,40)
#
set ylabel 'Memory cost (MB)'
set terminal postscript eps "Helvetica" 25
set out 'fr-mem.eps'
plot 'fr.dat' using 1:8 title 'Average' with linespoints lw 4 ps 3, 'fr.dat' using 1:9 title 'Maximum' with linespoints lw 4 ps 3, 'fr.dat' using 1:10 title 'Minimum' with linespoints lw 4 ps 3

reset
unset log
unset label
set xlabel 'Number of ticket buyer agents'
set key left top
set xtics (10,15,20,25,30,35,40)
#
set ylabel 'Maximum number of worlds'
set terminal postscript eps "Helvetica" 25
set out 'fr-world.eps'
plot 'fr.dat' using 1:5 title 'Average' with linespoints lw 4 ps 3, 'fr.dat' using 1:6 title 'Maximum' with linespoints lw 4 ps 3, 'fr.dat' using 1:7 title 'Minimum' with linespoints lw 4 ps 3

reset
unset log
unset label
set xlabel 'Number of ticket buyer agents'
set key left top
set xtics (10,15,20,25,30,35,40)
#
set ylabel 'CPU time (sec)'
set terminal postscript eps "Helvetica" 25
set out 'fr-cpu.eps'
plot 'fr.dat' using 1:2 title 'Average' with linespoints lw 4 ps 3, 'fr.dat' using 1:3 title 'Maximum' with linespoints lw 4 ps 3, 'fr.dat' using 1:4 title 'Minimum' with linespoints lw 4 ps 3

reset
unset log
unset label
set key left top
#
set xlabel '% time savings'
set ylabel 'Number of agents'
set xtics (0,10,20,30,40,50,60,70,80,90,100)
set terminal postscript eps "Helvetica" 25
set out 'fr-exit.eps'
plot "fr-exit.dat" u 1:2 with boxes title "" lw 4
