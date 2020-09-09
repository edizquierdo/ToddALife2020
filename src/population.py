import numpy as np
import matplotlib.pyplot as plt

class Population():
    def __init__(self, popsize, genesize, landscape, recombProb, mutatProb, eliteprop, lamarckian, steep_checks):
        self.popsize = popsize
        self.genesize = genesize
        self.elite = int(eliteprop*popsize)
        self.recombProb = recombProb
        self.mutatProb = mutatProb
        self.landscape = landscape

        self.genotypes = np.random.randint(2,size=popsize*genesize).reshape(popsize,genesize)
        self.phenotypes = self.genotypes.copy()

        # Initial fitness eval
        self.fitness = np.zeros(self.popsize)
        for i in range(self.popsize):
            self.fitness[i] = self.landscape.fitness(self.phenotypes[i])

        self.lamarckian = lamarckian

        # The number of genes to check in the steepest-ascent condition
        self.steep_checks = steep_checks

    def steepLearn(self):
        """ Everyone in the population takes a steepest hill-climb step """

        # Iterate through each member of the population
        for i in range(self.popsize):
            best_fitness = self.landscape.fitness(self.phenotypes[i])
            best_n = -1

            # Select a set of loci to test randomly from the full set of all possible
            # locations. Note that if self.steep_checks = self.genesize, all locations
            # will be tested
            loci_to_flip = np.random.choice(np.arange(self.genesize), size=self.steep_checks, 
                                            replace=False)

            # Try flipping each bit, in ascending order of location
            for n in sorted(loci_to_flip):
                new_phenotype = self.phenotypes[i].copy()
                new_phenotype[n] = (new_phenotype[n]+1)%2

                # Record the best single flip
                new_fitness = self.landscape.fitness(new_phenotype)
                if new_fitness >= best_fitness:
                    best_fitness = new_fitness
                    best_n = n

            # If any of the flips improved the fitness, then make
            # that edit to the phenotype
            if best_n >= 0:
                self.phenotypes[i][best_n] = (self.phenotypes[i][best_n]+1)%2
                self.fitness[i] = best_fitness

            # If we're Lamarckian, then the current phenotype
            # becomes the genotype
            if self.lamarckian:
                self.genotypes[i] = self.phenotypes[i]


    def learn(self):
        """ Everyone in the population takes a hill-climb step if better """

        # Iterate through each member of the population
        for i in range(self.popsize):
            # Evaluate the current phenotype
            current_fitness = self.landscape.fitness(self.phenotypes[i])
            new_phenotype = self.phenotypes[i].copy()

            # Flip a random bit of the phenotype
            n = np.random.randint(self.genesize)
            new_phenotype[n] = (new_phenotype[n]+1)%2

            # If the new phenotype is better, we remember this update
            new_fitness = self.landscape.fitness(new_phenotype)
            if new_fitness >= current_fitness:
                self.phenotypes[i] = new_phenotype
                self.fitness[i] = new_fitness

            # If we're Lamarckian, then the current phenotype
            # becomes the genotype
            if self.lamarckian:
                self.genotypes[i] = self.phenotypes[i]

    def reproduce(self):
        """ Population reproduces to produce a new generation """

        # Rank individuals by fitness
        rank = np.zeros(self.popsize,dtype=int)
        for i in range(self.popsize):
            rank[i]=int(np.argmax(self.fitness))
            self.fitness[rank[i]]=0.0

        # Create new generation
        new_genotypes = np.zeros((self.popsize,self.genesize))
        for i in range(self.elite):
            new_genotypes[i] = self.genotypes[rank[i]]
            self.fitness[i] = self.landscape.fitness(new_genotypes[i])

        for i in range(self.elite,self.popsize):
            # Pick parents based on rank probability
            a = rank[int(np.random.triangular(0, 0, self.popsize))]
            b = rank[int(np.random.triangular(0, 0, self.popsize))]

            # Recombine and mutate
            for k in range(self.genesize):
                if np.random.random() < self.recombProb:
                    new_genotypes[i][k] = self.genotypes[a][k]
                else:
                    new_genotypes[i][k] = self.genotypes[b][k]
                if np.random.random() < self.mutatProb:
                    new_genotypes[i][k] = np.random.randint(2)
            self.fitness[i] = self.landscape.fitness(new_genotypes[i])

        self.genotypes = new_genotypes.copy()
        self.phenotypes = self.genotypes.copy()

    def stats(self):
        return np.max(self.fitness), np.mean(self.fitness)

    def bestsol(self):
        return self.genotypes[np.argmax(self.fitness)]
