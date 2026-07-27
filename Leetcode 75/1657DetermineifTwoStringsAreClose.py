from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    counter1 = Counter(word1)
    counter2 = Counter(word2)

    if set(word1) != set(word2):
        return False

    return sorted(counter1.values()) == sorted(counter2.values())


word1 = "abc"
word2 = "bca"
print(closeStrings(word1,word2))