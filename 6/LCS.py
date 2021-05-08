'''
Longest Common Subsequence
输入: str1 = "abcde", str2 = "ace"
输出: 3
解释: 最长公共子序列是 "ace"，它的长度是 3
'''
# 递归法，无优化，存在重复计算
def LCS(str1, str2) -> int:
    def dp(i, j):
        # 空串的 base case
        if i == -1 or j == -1:
            return 0
        if str1[i] == str2[j]:
            # 这边找到一个 lcs 的元素，继续往前找
            return dp(i - 1, j - 1) + 1
        else:
            # 当前元素不在lcs中，要舍弃其中一个
            # 谁能让 lcs 最长，就听谁的
            return max(dp(i - 1, j), dp(i, j - 1))

    # i 和 j 初始化为最后一个索引
    return dp(len(str1) - 1, len(str2) - 1)

# 用DP Table进行优化
def longestCommonSubsequence(str1, str2) -> int:
    m, n = len(str1), len(str2)
    # 构建 DP table 和 base case
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # 进行状态转移
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # 找到一个 lcs 中的字符
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # print matrix
        for row in dp:
            print(row)
        print()
    return dp[-1][-1]


if __name__ == '__main__':
    print(LCS('babcde', 'ace'))
    print('============================================')
    print(longestCommonSubsequence('ace', 'babcde'))