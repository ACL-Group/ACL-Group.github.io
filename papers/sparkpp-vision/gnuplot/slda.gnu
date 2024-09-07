set output "exp_slda.eps"
set terminal postscript eps enhanced monochrome font 'Helvetica,25'
set boxwidth 1 absolute
set style fill  solid border -1
set key center vertical noenhanced autotitle columnhead nobox Left bmargin reverse
set key samplen 4 width 0 height 0
set grid noxtics noytics
set style histogram clustered gap 1 title textcolor lt -1 offset character 2, -2, 0
set datafile missing '-'
set style data histograms
set xtics border in scale 1,0.5 mirror rotate by 0  autojustify
set xtics  norangelimit
set xtics   () nomirror
set ytics font "Helvetica"
set ylabel "Total running time (second)" offset 0,0
# set logscale y 10
# set format "10^{%L}"
set datafile missing '-'
set macros
ymax="3e4"
set yrange [0:@ymax]
plot for [COL=2:3] 'slda.dat' using COL:xtic(1) fs pattern COL==2?0:3 lt -1, \
    for [COL=2:3] '' using (column(0)-1.25+(COL-2)*0.4):(@ymax):(column(0)>0 && column(COL)>@ymax?sprintf("{/Symbol \245}"):"") with labels font "Helvetica-Bold,38" offset 0,0.5, \
	'' using (2):(1e1):("{/ZapfDingbats \070") with labels font ",36" offset 0,1
