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


#  place mcmc algorithm here
def mcmc():
    pass
    
def main(n):
    print("Part A. The sampling probabilities")
    print("C|-s,r = <,>")
    print("C|-s,-r = <,>")
    print("R|c,-s,w = <,>")
    print("R|-c,-s,w = <,>")
    
    print("Part B. The transition probability matrix")
    
    print("Part C. The probability for the query")
    print("C|-s,r = <,>")

if __name__ == "__main__":
    n = 1000000
    main(n)
    