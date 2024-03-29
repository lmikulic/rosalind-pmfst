def string_to_int(text):
    return [int(x) for x in text.split(" ")]

def rosalind_input(text):
    chromosomes = text.split(")")
    chromosomes = [string_to_int(chrom[1:]) for chrom in chromosomes[:-1]]
    return chromosomes

def chromosome_to_cycle(chromosome):
    cycle = []
    for x in chromosome:
        if x > 0:
            cycle.extend([2 * x - 1, 2 * x])
        if x < 0:
            x = abs(x)
            cycle.extend([2 * x, 2 * x - 1])
    return cycle

def get_colored_edges(chromosomes):
    edges = []
    for chrom in chromosomes:
        nodes = chromosome_to_cycle(chrom)
        for j in range(1, len(nodes) - 1, 2):
            edges.append((nodes[j], nodes[j + 1]))
        edges.append((nodes[-1], nodes[0]))
    return edges

def get_n_cycles(edges):
    edges = edges.copy()
    n_cycles = 0
    starting = edges[0][1]
    del edges[0]
    while True:
        found = False
        for i in range(0, len(edges)):
            if starting == edges[i][0]:
                starting = edges[i][1]
                found = True
                break
            if starting == edges[i][1]:
                starting = edges[i][0]
                found = True
                break
        if found:
            del edges[i]
        else:
            n_cycles += 1
            if len(edges) == 0:
                break
            starting = edges[0][1]
            del edges[0]

    return n_cycles

if __name__=="__main__":
    with open("../Downloads/rosalind_ba6c.txt", "r") as f:
        linije=[line.strip() for line in f.readlines()]
    genome_P = linije[0]
    genome_Q = linije[1]

    chromosomes_P = rosalind_input(genome_P)
    chromosomes_Q = rosalind_input(genome_Q)

    colored_edges_P = get_colored_edges(chromosomes_P)
    colored_edges_Q = get_colored_edges(chromosomes_Q)

    colored_edges_breakpoint_PQ = colored_edges_P + colored_edges_Q

    n_cycles = get_n_cycles(colored_edges_breakpoint_PQ)

    n_syn_blocks = 0
    for chrom in chromosomes_P:
        n_syn_blocks += len(chrom)

    print(n_syn_blocks - n_cycles)
