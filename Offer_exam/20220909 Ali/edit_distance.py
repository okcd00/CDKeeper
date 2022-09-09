from pprint import pprint


def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    len1 = len(word1)
    len2 = len(word2)

    dist = [
        [0 for _ in range(len2+1)] for _ in range(len1+1)]
    
    # initial
    dist[0][0] = 0
    for _i in range(1, len1+1):
        dist[_i][0] = _i

    for _j in range(1, len2+1):
        dist[0][_j] = _j

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            # i = _i - 1
            # j = _j - 1
            if word1[i-1] == word2[j-1]:
                dist[i][j] = dist[i-1][j-1]  # ab/ab -> abc/abc 
            else:
                dist[i][j] = min(
                    dist[i-1][j-1],
                    dist[i-1][j],  # ab/ac -> abc/acx 
                    dist[i][j-1]  # ab/ac -> abx/abc 
                ) + 1

    pprint(dist)
    return dist[len1][len2]


if __name__ == "__main__":
    ret = minDistance("horse", "hse")
    print(ret)