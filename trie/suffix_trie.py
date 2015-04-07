# from CMU suffix trie slides
class SuffixNode:
    def __init__(self, suffix_link = None):
        self.children = {}
        if suffix_link is not None:
            self.suffix_link = suffix_link
        else:
            self.suffix_link = self

    def addLink(self, c, v):
        ''' link this node to node v via string c '''
        self.children[c] = v

def buildSuffixTrie(s):
    ''' construct a suffix trie '''
    assert s

    # explicitly build the two-node suffix tree
    root = SuffixNode()
    longest = SuffixNode(suffix_link = root)
    root.addLink(s[0], longest)

    # for every char left in the string
    for c in s[1:]:
        cur = longest; prev = None
        while c not in cur.children:
            # create new node r1 with transition Current -c->r1
            r1 = SuffixNode()
            cur.addLink(c, r1)

            # if we came from some previous node, make that
            # node's suffix link point here
            if prev is not None:
                prev.suffix_link = r1

            # walk down the suffix links
            prev = r1
            cur = cur.suffix_link

        # make the last suffix link
        if cur is root:
            prev.suffix_link = root
        else:
            prev.suffix_link = cur.children[c]
        
        # move to the newly added child of the longest path
        # (which is the new longest path)
        longest = longest.children[c]

    return root

if __name__ == '__main__':
    root = buildSuffixTrie('abaaba')
