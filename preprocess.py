# Normalize input data for training or testing
# python preprcoss.py [sourcefile] [destfile]
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python preprcoss.py [sourcefile] [destfile]"

    # read sourcefile
    X = [[float(x) for x in xs.strip().split(',')] for xs in open(sys.argv[1])]
    
    # search boundary of each column of X
    get_bounder = lambda c, func: func([xs[c] for xs in X])
    bds = [(get_bounder(c, max), 
            get_bounder(c, min)) for c in xrange(len(X[0]) - 1)]

    # normalize
    with open(sys.argv[2], "w") as output:
        for xs in X:
            output.write(','.join([str((x - bds[c][1]) / (bds[c][0] - bds[c][1])) for c, x in enumerate(xs[:-1])] + [str(xs[-1])]) + '\n')
    
    print '...preprocess successfully!'

