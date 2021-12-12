with open('input/sonar_sweep.txt') as f:
    sonar_depths = [int(line.rstrip()) for line in f]

#print(sonar_depths)

#single measurement

def single_measure(sonar_signal):
    counter = 0

    for i,depth in enumerate(sonar_signal):
        if i == 0:
            #print(depth)
            continue
        if depth > sonar_signal[i-1]:
            counter += 1
            #print(f'{depth} (increased)')
        #else:
            #print(f'{depth} (decreased)')
    return counter

print(f'Single measurement: {single_measure(sonar_depths)}')

#three-measurement sliding window

windows = [depth + sonar_depths[i+1] + sonar_depths[i+2] for i,depth in enumerate(sonar_depths[:-2])]

#single_measure(windows)

print(f'Three measurement: {single_measure(windows)}')

