import matplotlib.pyplot as plt
from textwrap import fill

plt.rcParams.update({'font.size': 15})
# fig, ax = plt.subplots()
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
plt.subplots_adjust(wspace=0.4, hspace=0)

fig.subplots_adjust(right=0.75)
fig.subplots_adjust(top=0.75)

twin2 = ax2.twinx()


x = [1065, 1987, 2632]
y1 = [85.25,88.16,82.48]
y2 = [81.78,84.95,80.53]
y3 = [0.2774,0.5211,0.9994]
y4 = [0.0738,0.0848,0.0959]

p1, = ax1.plot(x, y1, marker='o', ms=7, mew=2, mfc='w', fillstyle='full', linewidth=2.5, color='royalblue', label="TaLR")
p2, = ax1.plot(x, y2, marker='^', ms=7, mew=2, mfc='w', fillstyle='full', linewidth=2.5, color='royalblue', label="Vanilla")
p3, = ax2.plot(x, y4, marker='o', ms=7, mew=2, mfc='w', fillstyle='full', linewidth=2.5, color='darkorange', label="TaLR")
p4, = twin2.plot(x, y3, marker='^', ms=7, mew=2, mfc='w', fillstyle='full', linewidth=2.5, color='seagreen', label="Vanilla")

ax1.set_xlim(600, 3050)
ax1.set_ylim(60, 110)
ax2.set_xlim(600, 3050)
ax2.set_ylim(0, 0.5)
twin2.set_ylim(0, 1.2)

ax1.set_xlabel("The Number Of Classes", fontsize=15)
ax1.set_xticks([1065, 1987, 2632])
ax1.set_xticklabels(['1065', '1987', '2632'], fontsize=14)
ax2.set_xlabel("The Number Of Classes", fontsize=15)
ax2.set_xticks([1065, 1987, 2632])
ax2.set_xticklabels(['1065', '1987', '2632'], fontsize=14)
ax1.set_ylabel("Accuracy (%)", fontsize=15)
ax2.set_ylabel("Time Consumption (sec/it)", fontsize=15)
twin2.set_ylabel("Time Consumption (sec/it)", fontsize=15)

ax1.yaxis.label.set_color(p1.get_color())
ax2.yaxis.label.set_color(p3.get_color())
twin2.yaxis.label.set_color(p4.get_color())

tkw = dict(size=4, width=1.5)
ax1.tick_params(axis='y', colors=p1.get_color(), **tkw)
ax2.tick_params(axis='y', colors=p3.get_color(), **tkw)
twin2.tick_params(axis='y', colors=p4.get_color(), **tkw)
ax1.tick_params(axis='x', **tkw)

plt.xticks(fontsize=12)

for xx, yy in zip(x, y1):
    ax1.text(xx, yy, '%.2f' % yy, ha='center', va='bottom', color='grey')

ax1.text(1065, 61, 'FG', ha='center', rotation=0, fontsize=15)
ax1.text(1987, 61, 'QD', ha='center', rotation=0, fontsize=15)
ax1.text(2632, 61, 'BH', ha='center', rotation=0, fontsize=15)

ax2.text(1065, 0.02, 'FG', ha='center', rotation=0, fontsize=15)
ax2.text(1987, 0.02, 'QD', ha='center', rotation=0, fontsize=15)
ax2.text(2632, 0.02, 'BH', ha='center', rotation=0, fontsize=15)

for xx, yy in zip(x, y2):
    ax1.text(xx, yy, '%.2f' % yy, ha='center', va='top', color='grey')

for xx, yy in zip(x, y3):
    twin2.text(xx, yy, '%.4f' % yy, ha='center', va='bottom', color='grey')

for xx, yy in zip(x, y4):
    ax2.text(xx, yy, '%.4f' % yy, ha='center', va='bottom', color='grey')


ax1.legend(handles=[p1,p2], ncol=1, loc='upper left', fontsize=15)
ax2.legend(handles=[p3,p4], ncol=1, loc='upper left', fontsize=15)

ax1.grid(True, axis='y', linestyle='-.')
ax2.grid(True, axis='y', linestyle='-.')

plt.show()