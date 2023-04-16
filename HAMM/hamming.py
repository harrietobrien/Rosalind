class HAM:

    def __init__(self, data):
        self.data = data
        self.test()

    @staticmethod
    def hammingDistance(s1: str, s2: str) -> int:
        assert len(s1) == len(s2)
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        return count

    def test(self):
        with open(self.data, 'r', encoding='UTF-8') as file:
            s1, s2 = file
            print(self.hammingDistance(s1.strip(), s2.strip()))


test = HAM('rosalind_hamm.txt')
