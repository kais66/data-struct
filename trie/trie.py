# http://www.geeksforgeeks.org/trie-insert-and-search/
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.child = [None for i in range(256)] # Used to hold TrieNode pointers

    def add(self, s):
        if not s: return
        nd = self
        for i in range(len(s)):
            ind = ord(s[i])
            if not nd.child[ind]:
                nd.child[ind] = TrieNode()
                #print 'child isEnd: %s, i= %d' % (str(self.child[ind].isEnd), i) 
            nd = nd.child[ind]
        nd.isEnd = True

    def search(self, s):
        if not s: return True
        nd = self
        for i in range(len(s)):
            ind = ord(s[i])
            if not nd.child[ind]: return False
            nd = nd.child[ind]
            #print 'nd isEnd: %s, i= %d' % (str(nd.isEnd), i) 
        return nd.isEnd

if __name__ == '__main__':
    trie = TrieNode()
    for w in ['abc', 'acd', 'bzz', 'aa' ]:
        trie.add(w)
    print trie.search('abc')
    print trie.search('acd')
    print trie.search('bzz')
    print trie.search('aa')

    print trie.search('xzd')
    print trie.search('bc')
    print trie.search('bz')
    print trie.search('b')
 



