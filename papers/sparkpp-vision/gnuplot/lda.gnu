set terminal postscript eps enhanced monochrome font 'Helvetica,25'
set output "exp_lda.eps"
set boxwidth 1 absolute
set style fill  pattern 1 border lt -1
set key center vertical noenhanced autotitle columnhead nobox Left bmargin reverse
set key samplen 4 width 0 height 0
set grid noxtics noytics
set style histogram clustered gap 1 title textcolor lt -1 offset character 2, -2, 0
set datafile missing '-'
set style data histograms
set xtics border in scale 1,0.5 mirror rotate by 0  autojustify
set xtics  norangelimit
set xtics   () nomirror
set ylabel "Total running time (second)" offset 0, 0
set macros
ymax="3e4"
set yrange [0:@ymax]
plot for [COL=2:3] 'lda.dat' using (column(COL)==0?@ymax:(column(COL)>0.01*@ymax?column(COL):column(COL)*5)):xtic(1) fs pattern COL==2?0:3 lt -1, \
	for [COL=2:3] '' using (column(0)-1.25+(COL-2)*0.4):(@ymax):(column(0)>0 && column(COL)>@ymax? sprintf("{/Symbol \245}"):"") with labels font "Helvetica-Bold,38" offset 0,0.5

