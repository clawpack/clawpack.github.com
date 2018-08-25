
from pylab import *

import glob
max_levels = 9

outdir = '_output'
tfiles = glob.glob(outdir + '/fort.t*')
ntimes = len(tfiles)
time = zeros(ntimes)
total_cpu = zeros(ntimes)
wtime = zeros((ntimes, max_levels))
cpu = zeros((ntimes, max_levels))
cells = zeros((ntimes, max_levels))

for j,fname in enumerate(tfiles):
    lines = open(fname).readlines()
    time[j] = float(lines[0].split()[0])
    total_cpu[j] = float(lines[11].split()[0])
    print j, 'total cpu: ',total_cpu[j]
    for level in range(max_levels):
        lineno = 14+level
        if len(lines) < lineno+1:
            break
        print j, level, lines[lineno]
        tokens = lines[lineno].split()
        if len(tokens)==0:
            break
        wtime[j, level] = float(tokens[1])
        cpu[j, level] = float(tokens[2])
        cells[j, level] = float(tokens[3])
    
figure(21)
clf()
plot(time/3600, total_cpu/3600)
title('Total CPU time')
xlabel('Simulation hours')
ylabel('CPU hours')

figure(22)
clf()
sum_cells_over_levels = zeros(ntimes)
for j in range(max_levels):
    if max(cells[:,j]) == 0:
        break
    #plot(time/3600, cells[:,j], label='Level %s' % (j+1))
    last_sum_cells = sum_cells_over_levels.copy()
    sum_cells_over_levels = cells[:,j]
    fill_between(time/3600, last_sum_cells, sum_cells_over_levels, 
                 label='Level %s' % (j+1))

gca().ticklabel_format(useOffset=False,style='sci',axis='y')
title('Grid cells updated on each level')
xlabel('Simulation hours')
ylabel('Grid cell updates')
legend(loc='upper left')


figure(23)
clf()
sum_cells_over_levels = zeros(ntimes)
for j in range(max_levels):
    if max(cells[:,j]) == 0:
        break
    #plot(time/3600, cells[:,j], label='Level %s' % (j+1))
    last_sum_cells = sum_cells_over_levels.copy()
    sum_cells_over_levels = cells[:,j]
    d1 = diff(last_sum_cells, axis=0)
    d2 = diff(sum_cells_over_levels, axis=0)
    fill_between(time[1:]/3600, d1, d2, label='Level %s' % (j+1))

gca().ticklabel_format(useOffset=False,style='sci',axis='y')
title('Cells updated since last output')
xlabel('Simulation hours')
ylabel('Grid cell updates')
legend(loc='upper left')


