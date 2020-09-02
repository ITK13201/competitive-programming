MOD = 10**9 + 7

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
    
    # 逆元
    def modinv(self):
        return ModInt(pow(self.value, MOD - 2, MOD))
    
N, K = map(ModInt, map(int, input().split()))

ans = ModInt(0)
for i in range(K, N + 2):
    res_min = ModInt( int(i * (i - 1) / 2) )
    res_max = ModInt( int(i * (N + (N - i + 1)) / 2) )
    
    ans += res_max - res_min + 1

print(ans)