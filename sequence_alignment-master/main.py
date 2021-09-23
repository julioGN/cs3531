import numpy as np

S1 = 'ACGU'
S2 = 'CGAU'


def seq_alignment(seq1, seq2):
    m = np.zeros((len(S1) + 1, len(S2) + 1))

    i = 0
    for matching in m:
        j = 0
        for cells in matching:
            if i != 0 and j != 0:
                if S1[i-1] == S2[j-1]:
                    m[i][j] = m[i-1][j-1] + 1
                if S1[i-1] != S2[j-1]:
                    if m[i-1][j] > m[i][j]:
                        m[i][j] = m[i-1][j]
                    if m[i][j-1] > m[i][j]:
                        m[i][j] = m[i][j-1]
            j += 1
        i += 1

    max_align_score = m[i-1][j-1]
    print("Maximum alignment score: ", end='')
    print(max_align_score)


def main():
    seq_alignment(S1, S2)


if __name__ == '__main__':
    main()
