import sys
input = lambda: sys.stdin.readline().rstrip()
from math import floor,ceil,sqrt,factorial,log
from heapq import heapify, heappop, heappush, heappushpop
from collections import Counter,defaultdict,deque
from itertools import accumulate,permutations,combinations,product,combinations_with_replacement
from bisect import bisect_left,bisect_right
from decimal import Decimal
inf = float('inf')
MOD = 1000000007

class ModInt:
    def __init__(self, x):
        if isinstance(x, ModInt):
            self.value = x.value
        else:
            self.value = x % MOD
            if self.value < 0:
                self.value += MOD
    
    def get_mod(self):
        return MOD
    
    # str関数を使用したとき
    def __str__(self):
        return str(self.value)
    
    def __int__(self):
        return self.value
    
    __index__ = __int__
    
    # print関数を使用したとき
    __repr__ = __str__

    ## 四則演算
    def __add__(self, other):
        return ModInt(self.value + ModInt(other).value)
    
    def __sub__(self, other):
        return ModInt(self.value - ModInt(other).value)

    def __mul__(self, other):
        return ModInt(self.value * ModInt(other).value)
    
    def __truediv__(self, other):
        # a * a^(p - 2) ≡ 1 (mod p) 逆元から求める
        return ModInt(self.value * pow(ModInt(other).value, MOD - 2, MOD))
    
    def __floordiv__(self, other):
        return ModInt(self.value * pow(ModInt(other).value, MOD - 2, MOD))

    # 累乗
    def __pow__(self, other):
        return ModInt(pow(self.value, ModInt(other).value, MOD))

    ## 四則演算の順序
    __radd__ = __add__

    def __rsub__(self, other):
        return ModInt(other - self.value)
    
    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return ModInt(other * pow(self.value, MOD - 2, MOD))

    def __rfloordiv__(self, other):
        return ModInt(other // self.value)
    
    # 累乗の順序
    def __rpow__(self, other):
        return ModInt(pow(other, self.value, MOD))
    
    ## 不等号
    def __lt__(self, other):
        return self.value < ModInt(other).value
    
    def __gt__(self, other):
        return self.value > ModInt(other).value

    def __le__(self, other):
        return self.value <= ModInt(other).value
    
    def __ge__(self, other):
        return self.value >= ModInt(other).value
    
    def __eq__(self, other):
        return self.value == ModInt(other).value
    
    def __ne__(self, other):
        return self.value != ModInt(other).value
    
    ## in-place 演算子(+=, -=, *=, /=)
    def __iadd__(self, other):
        self.value += ModInt(other).value
        if self.value >= MOD:
            self.value -= MOD
        return self.value
    
    def __isub__(self, other):
        self.value -= ModInt(other).value
        if self.value < 0:
            self.value += MOD
        return self.value
    
    def __imul__(self, other):
        self.value = ModInt(self.value * ModInt(other).value)
        return self.value

    def __itruediv__(self, other):
        self.value = ModInt(self.value * pow(ModInt(other).value, MOD - 2, MOD))
        return self.value
    
    def __ifloordiv__(self, other):
        self.value = ModInt(self.value * pow(ModInt(other).value, MOD - 2, MOD))
        return self.value
    
    # 逆元
    def modinv(self):
        return ModInt(pow(self.value, MOD - 2, MOD))



    


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

n = int(input())
a, b = [], []
for _ in range(n):
    aa, bb = map(int, input().split())
    a.append(aa)
    b.append(bb)

all = (ModInt(n) - 1) // 2
res = ModInt(0)
for i in range(n):
    def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
        return a[i] * a[arg] == -b[i] * b[arg]
    
    if meguru_bisect(n, 1):
        res += 1

ans = all - res

print(ans, all, res)
