
def calculate_wer(reference: str, hypothesis: str) -> dict:

    reference_words = reference.lower().split()
    hypothesis_words = hypothesis.lower().split()

    n = len(reference_words)
    m = len(hypothesis_words)

    if n == 0:
        if m == 0:
            return {
                "wer": 0.0,
                "substitutions": 0,
                "deletions": 0,
                "insertions": 0,
                "reference_words": 0
            }
        raise ValueError("Еталонний текст не повинен бути порожнім.")

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if reference_words[i - 1] == hypothesis_words[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,      
                dp[i][j - 1] + 1,       
                dp[i - 1][j - 1] + cost 
            )

   
    i, j = n, m
    substitutions = 0
    deletions = 0
    insertions = 0

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            cost = (
                0 if reference_words[i - 1] == hypothesis_words[j - 1]
                else 1
            )

            if dp[i][j] == dp[i - 1][j - 1] + cost:
                if cost == 1:
                    substitutions += 1
                i -= 1
                j -= 1
                continue

        if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            deletions += 1
            i -= 1
        else:
            insertions += 1
            j -= 1

    wer = (
        (substitutions + deletions + insertions) / n
    ) * 100

    return {
        "wer": round(wer, 2),
        "substitutions": substitutions,
        "deletions": deletions,
        "insertions": insertions,
        "reference_words": n
    }
