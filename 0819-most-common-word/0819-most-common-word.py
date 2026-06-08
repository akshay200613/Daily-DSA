class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        # extract words, lowercased
        words = re.findall(r'\w+', paragraph.lower())
        # count only non-banned words
        counts = collections.Counter(
            w for w in words if w not in banned_set
        )
        # most_common(1) returns [(word, freq)]
        return counts.most_common(1)[0][0]