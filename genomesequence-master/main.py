import matplotlib.pyplot as p

# read genome stuff line by line

e_count_A = 0
e_count_C = 0
e_count_G = 0
e_count_T = 0

t_count_A = 0
t_count_C = 0
t_count_G = 0
t_count_T = 0

genome_e = 'data/Ecoli-bacteria-complete-genome-low-GC.fasta'
genome_t = 'data/thermophile-thermo-microbium-complete-genome-has-high-CGs.fasta'

# read lines
open_lines_e = open(genome_e, 'r')
open_lines_t = open(genome_t, 'r')

line_e = open_lines_e.readline()
line_t = open_lines_t.readline()

for g in line_e:
    if genome_e.startswith('>'):
        break;
    else:
        print(line_e)

        for i in range(len(line_e)):
            if line_e[i] == 'A':
                e_count_A += 1
            if line_e[i] == 'C':
                e_count_C += 1
            if line_e[i] == 'G':
                e_count_G += 1
            if line_e[i] == 'T':
                e_count_T += 1


for g in line_t:
    if genome_t.startswith('>'):
        break;
    else:
        print(line_t)

        for i in range(len(line_t)):
            if line_t[i] == 'A':
                t_count_A += 1
            if line_t[i] == 'C':
                t_count_C += 1
            if line_t[i] == 'G':
                t_count_G += 1
            if line_t[i] == 'T':
                t_count_T += 1


A_percentage_e = e_count_A / (e_count_A + e_count_C + e_count_G + e_count_G) * 100
print("A%: ", A_percentage_e)
C_percentage_e = e_count_C / (e_count_A + e_count_C + e_count_G + e_count_G) * 100
print("C%: ", C_percentage_e)
G_percentage_e = e_count_G / (e_count_A + e_count_C + e_count_G + e_count_G) * 100
print("G%: ", G_percentage_e)
T_percentage_e = e_count_G / (e_count_A + e_count_C + e_count_G + e_count_G) * 100
print("T%: ", T_percentage_e)

A_percentage_t = t_count_A / (t_count_A + t_count_C + t_count_G + t_count_G) * 100
print("A%: ", A_percentage_t)
C_percentage_t = t_count_C / (t_count_A + t_count_C + t_count_G + t_count_G) * 100
print("C%: ", C_percentage_t)
G_percentage_t = t_count_G / (t_count_A + t_count_C + t_count_G + t_count_G) * 100
print("G%: ", G_percentage_t)
T_percentage_t = t_count_T / (t_count_A + t_count_C + t_count_G + t_count_G) * 100
print("T%: ", T_percentage_t)

#barchart

results_e = {'A': A_percentage_e, 'C': C_percentage_e, 'G': G_percentage_e, 'T': T_percentage_e}
key_e = list(results_e.keys())
val_e= list(results_e.values())

results_t = {'A': A_percentage_t, 'C': C_percentage_t, 'G': G_percentage_t, 'T': T_percentage_t}
key_t = list(results_t.keys())
val_t = list(results_t.values())

figure_e = p.figure(figsize=(5,5))
p.bar(key_e, val_e, color='green', width=0.3)

p.title("Percentage of A, C, G, and T in a Ecoli Genome Sequence")
p.xlabel("A, C, G, and T")
p.ylabel("Percentage of A, C, G, and T")
p.show()

figure_t = p.figure(figsize=(5,5))
p.bar(key_t, val_t, color='blue', width=0.3)

p.title("Percentage of A, C, G, and T in a Thermophile Genome Sequence")
p.xlabel("A, C, G, and T")
p.ylabel("Percentage of A, C, G, and T")
p.show()