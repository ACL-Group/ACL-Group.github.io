set output "exp_dcmlda.eps"
set terminal postscript eps enhanced monochrome font 'Helvetica,25'
set boxwidth 1 absolute
set style fill  pattern 1 border lt -1
set key nobox outside bottom center vertical noenhanced reverse
set key autotitle columnhead
set grid noxtics noytics
set style histogram clustered gap 1 title textcolor lt -1 offset character 2, -2, 0
set style data histograms
set xtics border in scale 1,0.5 mirror rotate by 0  autojustify
set xtics  norangelimit
set xtics   () nomirror
set ytics font "Helvetica"
set ylabel "Total running time (second)" offset 0,0
set datafile missing '-'
set macros
ymax="3e4"
set yrange [0:@ymax]
plot for [COL=2:3] 'dcmlda.dat' using COL:xtic(1) fs pattern COL==2?0:3 lt -1 title columnheader,\
	'' using (2):(1e1):("{/ZapfDingbats \070") with labels font ",36" offset 0,1 , \
   for [COL=2:3] '' using (column(0)-1.25+(COL-2)*0.4):(@ymax):((column(0)>0 && column(COL)>@ymax)?sprintf("{/Symbol \245}"):"") with labels font "Helvetica-Bold,38" offset 0,0.5

