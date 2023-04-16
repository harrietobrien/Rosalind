# https://rosalind.info/problems/dna/
from collections import Counter


class DNA:

    def __init__(self, data):
        self.data = data
        print(self.data)
        self.test()

    @staticmethod
    def countingNucleotides(s: str) -> int:
        """
        :return: A C G T occurrences
        """
        dna = Counter(s)
        counts = "{a} {c} {g} {t}"
        return counts.format(a=dna['A'], c=dna['C'], g=dna['G'], t=dna['T'])

    def test(self):
        with open(self.data, 'r', encoding='UTF-8') as file:
            for line in file:
                print(self.countingNucleotides(line))


test = DNA('rosalind_dna.txt')
