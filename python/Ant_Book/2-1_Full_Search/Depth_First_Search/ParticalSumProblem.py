# ParticalSumProblem.py - 部分和問題

n = int(input())
a = list(map(int, input().split()))
k = int(input())

# 深さ優先探索（DFS: Depth-First Search）
# iまででsumを作って，残りi以降を調べる
def dfs(i, sum):
    # n個決め終わったら，今までの和sumがkと等しいかを返す
    if i == n:
        return sum == k
    
    # a[i]を使わない場合
    if dfs(i + 1, sum):
        return True
    
    # a[i]を使う場合
    if dfs(i + 1, sum + a[i]):
        return True
    
    # a[i]を使う使わないにかかわらずkが作れないのでfalseを返す
    return False


if dfs(0, 0):
    print('Yes')
else:
    print('No')

