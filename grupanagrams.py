from collections import defaultdict

from dropbox.file_requests import list_v2


def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()



words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))