with open('input/binarydiagnostics.txt') as f:
    diagnostics = [line.rstrip() for line in f]

#print(diagnostics)

def bin_to_int(binary):
    integ = 0
    binary = binary[::-1]
    for i,num in enumerate(binary):
        integ += int(num) * 2**i
    return integ

def checksum(diagnostics):
    total_number = len(diagnostics[0])
    check_sum = [0] * total_number

    for binary in diagnostics:
        for i,bin in enumerate(binary):
            check_sum[i] += int(bin)
    return check_sum

def first_part(diagnostics):

    total_number = len(diagnostics[0])
    maximal_number = len(diagnostics)   
    check_sum = checksum(diagnostics)

    gamma_rate = [0] * total_number
    epsilon_rate = [0] * total_number 

    for i,val in enumerate(check_sum):
        if val > maximal_number//2:
            gamma_rate[i] = 1
        else:
            epsilon_rate[i] = 1

    power = bin_to_int(gamma_rate) * bin_to_int(epsilon_rate)
    print(f'Power consumption is {power}')

    return power

first_part(diagnostics)

def most_common(check_sum,bin,maximal_number):
    if check_sum[bin] >= maximal_number/2:
        return 1
    else:
        return 0

def least_common(check_sum,bin,maximal_number):
    if check_sum[bin] >= maximal_number/2:
        return 0
    else:
        return 1

def oxygen_generator(diagnostics,n):

    maximal_number = len(diagnostics)
    tot_number = len(diagnostics[0])

    if len(diagnostics) == 1:
        return bin_to_int(diagnostics[0])
    else:
        diagnostics_new = []
        check_sum = checksum(diagnostics)
        bin = tot_number-n
        ref = most_common(check_sum,tot_number-n,maximal_number)
        for val in diagnostics:
            if int(val[bin]) == ref:
                diagnostics_new.append(val)
        return(oxygen_generator(diagnostics_new,n-1))

def co2_scrubber(diagnostics,n):

    maximal_number = len(diagnostics)
    tot_number = len(diagnostics[0])

    if len(diagnostics) == 1:
        return bin_to_int(diagnostics[0])
    else:
        diagnostics_new = []
        check_sum = checksum(diagnostics)
        bin = tot_number-n
        ref = least_common(check_sum,tot_number-n,maximal_number)
        for val in diagnostics:
            if int(val[bin]) == ref:
                diagnostics_new.append(val)
        return(co2_scrubber(diagnostics_new,n-1))

oxy = oxygen_generator(diagnostics,len(diagnostics[0]))
co2 = co2_scrubber(diagnostics,len(diagnostics[0]))

print(f'Oxygen generator is {oxy}')
print(f'CO2 scrubber is {co2}')

life = oxy * co2
print(f'Life support rating is {life}')


