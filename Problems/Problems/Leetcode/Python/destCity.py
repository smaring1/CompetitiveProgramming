class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityMap = {}
        for path in paths:
            cityMap[path[0]] = path[1]
        
        dest = paths[0][1]
        while True:
            if dest in cityMap:
                dest = cityMap[dest]
            else:
                return dest