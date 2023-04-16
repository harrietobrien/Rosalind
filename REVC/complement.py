class REVC:

    def __init__(self, data):
        self.data = data
        self.test()

    @staticmethod
    def reverseComplement(s: str) -> int:
        pairs = [('A', 'T'), ('C', 'G')]
        d = dict()
        for k, v in pairs:
            d[k], d[v] = v, k
        return ''.join(d[i] for i in s[::-1])

    def test(self):
        with open(self.data, 'r', encoding='UTF-8') as file:
            for line in file:
                print(self.reverseComplement(line.strip()))


test = REVC('rosalind_revc.txt')
