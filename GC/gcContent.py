
class GC:

    def __init__(self, data):
        self.data = data
        self.gcd = dict()
        self.test()

    @staticmethod
    def gcContent(s: str) -> int:
        gc = s.count('C') + s.count('G')
        return (gc / len(s)) * 100

    def highestGC(self):
        assert self.gcd
        gcd = {k: self.gcContent(self.gcd[k]) for k in self.gcd}
        v = list(gcd.values())
        k = list(gcd.keys())
        return k[v.index(max(v))], max(v)

    def test(self):
        with open(self.data, 'r', encoding='UTF-8') as file:
            currID = None
            currStrand = ''
            for line in file:
                if line.startswith('>'):
                    if currID:
                        self.gcd[currID] = currStrand
                        currStrand = ''
                    currID = line.replace('>', '').strip()
                else:
                    currStrand += line.strip()
                self.gcd[currID] = currStrand
        id, content = self.highestGC()
        print("{i}\n{c}".format(i=id, c=content))


test = GC('rosalind_gc.txt')
