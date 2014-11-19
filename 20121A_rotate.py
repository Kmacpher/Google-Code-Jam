#Round 1A 2010: Rotate
#10/10/2014
#https://code.google.com/codejam/contest/544101/dashboard#s=p0
#Correct!!!
#!usr/bin/python

def solve(case):
    m, k = raw_input().split()
    m = int(m)
    k = int(k)
    matrix = []
    new = []
    newline = []
    Bwin = False
    Rwin = False

    #takes raw_input and makes in into a matrix (list of lists)

    for i in xrange(m):
        matrix.append(list(raw_input()))
        
            
    #instead of rotating matrix, this moves all the letter to the right, as if 'gravity' pulled them that way
    #makes new matrix, inserting '.' up to the matrix dimensions

    for y in xrange(m):
        for i in xrange(len(matrix[y])):
            if matrix[y][i] != '.':
                newline.append(matrix[y][i])
        if not newline:
            for x in xrange(m):
                newline.insert(0, '.')
        else:
            for x in xrange(m-len(newline)):
                newline.insert(0, '.')
        new.append(newline)
        newline = []

    #This wonderful solution is from FMc on stack overflow
    #http://stackoverflow.com/questions/3311119/determining-three-in-a-row-in-python-2d-array

    left = [[0] * i for i in xrange(m)]
    right = list(reversed(left))

    #Adds padding to offset for diag, then uses zip to put that diag into a list. 
    #0 is a space holder, meaning that it is off the board

    transpositions = {
        'horizontal' : new,
        'vertical'   : zip(*new),
        'diag_forw'  : zip(* [left[i] + new[i] + right[i] for i in xrange(m)]),
        'diag_back'  : zip(* [right[i] + new[i] + left[i] for i in xrange(m)]),
    }
    
    Bstr = "B"*k
    Rstr = "R"*k
    for dir, transp in transpositions.iteritems():
        for row in transp:
           strings = ''.join(map(str, row))
           if Bstr in strings:
               Bwin = True
           if Rstr in strings:
               Rwin = True
    
    if Bwin and Rwin:
        print "Case #%d: Both"%case
    elif Bwin:
        print "Case #%d: Blue"%case
    elif Rwin: 
        print "Case #%d: Red"%case
    else:
        print "Case #%d: Neither"%case


T=int(raw_input())
for case in xrange(T):
    solve(case+1)
