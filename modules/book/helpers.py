def readBook(path:str) -> str:
    with open(path) as f:
        return f.read()

def countWords(string:str) -> int:
    return len(string.split())

def countEachLetter(string:str) -> dict:
    string = string.lower()
    counts = {l: string.count(l) for l in set(chr(ord('a') + i) for i in range(1, 26))}
    counts = {k: v for k, v in sorted(counts.items(), key=lambda tup: tup[1], reverse=True)}
    return counts