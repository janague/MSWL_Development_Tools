#!/usr/bin/env python

def main():
    parents, babies = (1, 1)
    # TODO: Complete some functionality
    # FIXME: Solve a bug 
    while babies < 100:
        print 'This generation has {0} babies'.format(babies)
        parents, babies = (babies, parents + babies)

if __name__ == "__main__":
    main()
