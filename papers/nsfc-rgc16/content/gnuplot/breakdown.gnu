set output "exp_breakdown.eps"
set terminal postscript eps enhanced monochrome font 'Helvetica,25'
set boxwidth 1 absolute
set style fill pattern 1 solid border
set key outside bottom center

set style data histogram
set style histogram rowstacked gap 1

plot for [COL=2:5] 'breakdown.dat' using  COL:xtic(1) fs pattern COL title columnhead
