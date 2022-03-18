class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        aux = 0
        
        for sentence in sentences:
            aux = max(aux,len(sentence.split(' ')))
            
        return aux
            