"""
This program calculates all the sequences that add up to 21 given a list of numbers
E.g. [1,2,3,4,5,6,7,10] -> [[1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 7], [5, 6, 10]]
Written by Daniel Lynch - 07/04/2015
"""

def twentyone(seq):
    if seq == [] or getsum(seq) < 21:
        return []
    else:
        myseq = iteratelist(seq, [])
        item = myseq[-1]
       
        index = (len(seq) - 1) - seq[::-1].index(item)   

        while (index + 1) < len(seq) and getsum(myseq) != 21:
            myseq.pop()            
            myseq = iteratelist(seq[index+1:], myseq)
            item = myseq[-1]
            index = (len(seq) - 1) - seq[::-1].index(item) 
        if getsum(myseq) == 21:
            if len(seq) == 7:
                seq2 = [seq[0], seq[3], seq[-2], seq[-1]]
                return [myseq] + twentyone(seq2) + twentyone(seq[1:])
            else:
                return [myseq] + twentyone(seq[1:])
        else:
            return twentyone(seq[1:])
           
 
def getsum(lst):
    thesum = 0
    for i in lst:
        thesum += i
    return thesum
 
 
def iteratelist(thisseq, workingseq=[]):
    pointer = 0
    thesum = getsum(workingseq)
    while pointer < len(thisseq):
        workingseq.append(thisseq[pointer])
        pointer += 1
        thesum = getsum(workingseq)
        if thesum > 21:
            workingseq.pop()
            thesum = getsum(workingseq)
        if thesum == 21:
            break
    return workingseq

seq = [1,2,3,4,5,6,7,10]
print(sorted(twentyone(seq)))