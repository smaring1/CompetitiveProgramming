class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        phrase = {x: 0 for x in sentence}
        return len(phrase) == 26