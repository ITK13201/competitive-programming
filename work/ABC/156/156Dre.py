MOD = 10**9 + 7

class ModInt:
    def __init__(self, x):
        if isinstance(x, ModInt):
            self.x = x.x
        else:
            self.x = x % MOD
            if self.x < 0:
                self.x += MOD
    
    def get_mod(self):
        return MOD
    
    def inv(self, other):
        return ModInt(pow(ModInt(other).x, MOD - 2, MOD))
    
    # str関数を使用したとき
    def __str__(self):
        return str(self.x)
    
    def __int__(self):
        return self.x
    
    __index__ = __int__
    
    # print関数を使用したとき
    __repr__ = __str__

    ## 四則演算
    def __add__(self, other):
        return ModInt(self.x + ModInt(other).x)
    
    def __sub__(self, other):
        return ModInt(self.x - ModInt(other).x)

    def __mul__(self, other):
        return ModInt(self.x * ModInt(other).x)
    
    # /
    def __truediv__(self, other):
        # a * a^(p - 2) ≡ 1 (mod p) 逆元から求める
        return ModInt(self.x * pow(ModInt(other).x, MOD - 2, MOD))

    # //
    def __floordiv__(self, other):
        return self.x // ModInt(other).x

    # 累乗
    def __pow__(self, other):
        return ModInt(pow(self.x, ModInt(other).x, MOD))

    ## 四則演算の順序
    __radd__ = __add__

    def __rsub__(self, other):
        return ModInt(other - self.x)
    
    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return ModInt(other * pow(self.x, MOD - 2, MOD))

    def __rfloordiv__(self, other):
        return ModInt(other // self.x)
    
    # 累乗の順序
    def __rpow__(self, other):
        return ModInt(pow(other, self.x, MOD))
    
    ## 不等号
    def __lt__(self, other):
        return self.x < ModInt(other).x
    
    def __gt__(self, other):
        return self.x > ModInt(other).x

    def __le__(self, other):
        return self.x <= ModInt(other).x
    
    def __ge__(self, other):
        return self.x >= ModInt(other).x
    
    def __eq__(self, other):
        return self.x == ModInt(other).x
    
    def __ne__(self, other):
        return self.x != ModInt(other).x
    
    ## in-place 演算子(+=, -=, *=, /=)
    def __iadd__(self, other):
        self.x += ModInt(other).x
        if self.x >= MOD:
            self.x -= MOD
        return self.x
    
    def __isub__(self, other):
        self.x -= ModInt(other).x
        if self.x < 0:
            self.x += MOD
        return self.x
    
    def __imul__(self, other):
        self.x = ModInt(self.x * ModInt(other).x)
        return self.x

    def __itruediv__(self, other):
        self.x = ModInt(self.x * pow(ModInt(other).x, MOD - 2, MOD))
        return self.x
    
    def __ifloordiv__(self, other):
        self.x = self.x // ModInt(other).x

def comb(n, r):
    res = ModInt(1)
    for i in range(n-r+1, n+1):
        res *= i
    for i in range(2, r+1):
        res /= i
    return res

n, a, b = map(ModInt, map(int, input().split()))

ans = 2 ** n

ans = ans - comb(n, a)
ans = ans - comb(n, b)
ans = ans - 1

print(ans)
