#  mcmc algorithm 451
# (a) (8 points) Show ~P (C|¬s, r), ~P (C|¬s, ¬r), ~P (R|c, ¬s, w), ~P (R|¬c, ¬s, w).
# (b) (16 points) Show the transition probability matrix Q ∈ R4×4where
# qij = transition probability from Si to Sj in Figure 2.
# (c) (20 points) Show the probability of the query ~P (C|¬s, w)
# (d) Please follow the output format. (Fix precisions using "{:.4f}".format)

# Part A. The sampling probabilities
# P(C|-s,r) = <..., ...>
# P(C|-s,-r) = <..., ...>
# P(R|c,-s,w) = <..., ...>
# P(R|-c,-s,w) = <..., ...>

# Part B. The transition probability matrix
# S1 S2 S3 S4
# S1 . . . .
# S2 . . . .
# S3 . . . .
# S4 . . . .
# Part C. The probability for the query
# P(C|-s,w) = <..., ...>

   
def main(n):
    #  .4f format
    print("Part A. The sampling probabilities")
    print("C|-s,r = a<.8780, .1212>")  #  a = 2.4390
    print("C|-s,-r = a<.9863, .0137>")  #  a = 1.3699
    print("R|c,-s,w = a<.3103, .6897>")  #  a = 3.4483
    print("R|-c,-s,w = a<.8182, .1818>")  #  a = 4.5455
    
    print("Part B. The transition probability matrix")
    print("\tS1\t S2\t S3\t S4")
    print("S1\t .\t .\t .\t .\t")
    print("S2\t .\t .\t .\t .\t")
    print("S3\t .\t .\t .\t .\t")
    print("S4\t .\t .\t .\t .\t")
    
    print("Part C. The probability for the query")
    print("C|-s,r = <,>")

if __name__ == "__main__":
    n = 1000000
    main(n)
    