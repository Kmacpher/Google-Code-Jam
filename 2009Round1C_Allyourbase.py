

#returns the number of unique characters in an argument   
def uniqcharset (message):
    uniq = []
    for c in message:
        if c not in uniq:
            uniq.append(c)
    return uniq 
    

def solve(t):
    sec = 0
    message = raw_input()
    uniq = list(uniqcharset(message))
    decoded = []
    code = {uniq[0] : '1'}
    abc = '23456789abcdefghijklmnopqrstuvwxyz'


    if len(uniq) > 1: 
        code[uniq[1]] = '0'
    if len(uniq) > 2:
        for c in uniq[2:]:
            for x in xrange(len(uniq)-2):
                code[uniq[x+2]] = abc[x]            
    

    
    if len(uniq) == 1:
        base = 2
    else:
        base = len(uniq)

    if len(message) == 1:
        sec = 1
    else:
        for c in message:
            decoded.append(code.get(c))
        sec = int(''.join(decoded),base)
   
    
    print "Case #%d: %d"%(t, sec)


cases = int(raw_input())
for t in xrange(cases):
    solve(t+1)

