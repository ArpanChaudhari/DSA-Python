def frequencySort(s: str) -> str:
    freq = {}
    result = ""

    # Count frequency of each character
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Sort by frequency descending, then character ascending
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Add each character according to its frequency
    for ch, count in sorted_freq:
        result += ch * count

    return result

s = "Aabb"
print(frequencySort(s))