# https://rosalind.info/problems/rna/


class RNA:

    def __init__(self, data):
        self.data = data
        self.test()

    @staticmethod
    def transcribeRNA(u: str) -> int:
        return u.replace('T', 'U')

    def test(self):
        with open(self.data, 'r', encoding='UTF-8') as file:
            rna = None
            for line in file:
                rna = self.transcribeRNA(line)
        print(rna)
        if rna:
            with open('out.txt', 'w') as file:
                file.write(rna)


test = RNA('rosalind_rna_1.txt')