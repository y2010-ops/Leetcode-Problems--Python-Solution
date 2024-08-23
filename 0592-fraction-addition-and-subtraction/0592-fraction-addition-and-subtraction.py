class Solution:
    def fractionAddition(self, exp: str) -> str:
        num = []
        denom = []
        sign = 1
        for i in range(len(exp)):
            if exp[i] == "-":
                sign = -1
            if exp[i] in ["/"]:
                if exp[i-2:i].isdigit():
                        num.append(int(exp[i-2:i]) * sign)
                else:
                    num.append(int(exp[i - 1:i]) * sign)
                if exp[i+1:i+3].isdigit():
                    denom.append(int(exp[i + 1: i+3]))
                else:
                    denom.append(int(exp[i + 1]))
                sign = 1

        numerator = 0
        denominator = math.prod(denom)
        for i in range(0, len(num)):
            k = i
            numerator += math.prod(denom[:k]) * math.prod(denom[k+1:]) * num[i]

        common_divisor = math.gcd(abs(numerator), denominator)
        return f"{numerator // common_divisor}/{denominator // common_divisor}"


