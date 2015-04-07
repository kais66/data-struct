import sys

def parent(i):
    return (i-1)//2
def left(i):
    return i*2 + 1
def right (i):
    return i*2 + 2

def siftdown(h, start, end):
    ''' h is essentially a python list, which tries to maintain the heap property:
        min heap: h[parent[i]] <= h[i]. 
        This considers the heap to be min-heap. '''
    ind = start 
    while left(ind) <= end:
        minind = left(ind) # tentative
        # need to replace the parent with child with min value
        if minind+1 <= end and h[minind] > h[minind+1]: minind += 1
        if h[ind] > h[minind]:
            h[ind], h[minind] = h[minind], h[ind]
            ind = minind
        else:
            return 
def siftup(h, ind):
    ''' move an element up, if it's parent violates heap property with it. Unlike siftdown, no need to worry about
        the sibling, as it's guaranteed to be no less than the original parent. ''' 
    while parent(ind) >= 0:
        prind = parent(ind)
        if h[ind] < h[prind]:
            h[ind], h[prind] = h[prind], h[ind]
            ind = prind 
        else:
            return
        
def heapify(h):
    for i in reversed(xrange(len(h)//2)):
        siftdown(h, i, len(h)-1)
        #print h
    #print ' '

def heapsort(h):
    heapify(h)
    for i in reversed(xrange(len(h)-1)):
        h[0], h[i+1] = h[i+1], h[0]
        siftdown(h, 0, i)
    # min-heap will produce reversed sorted order
    h.reverse()

def heappush(h, e):
    h.append(e)
    siftup(h, len(h)-1) 

def heappop(h):
    h[0], h[len(h)-1] = h[len(h)-1], h[0]
    siftdown(h, 0, len(h)-2) 
    return h.pop()

if __name__ == '__main__':
    h = [13, 14, 94, 33, 82, 25, 59, 65, 23, 45, 27, 73, 25, 39, 10] 
    #h = [5, 4, 3, 2, 1]
    heapsort(h)
    print h

    hnew = []
    for x in h: 
        heappush(hnew, x)
        print hnew
    l = len(h)
    for i in xrange(l-1):
        print heappop(hnew)
