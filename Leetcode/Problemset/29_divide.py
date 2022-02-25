class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = True
        if dividend < 0:
            dividend = - dividend
            sign = not sign 
        if divisor < 0:
            divisor = - divisor
            sign = not sign 
        
        if divisor == 1:
            ret = dividend
        
        else:
            ret = ['0']
            offset = 0  # cur_dividend is [offset, pivot]
            divisor_str = str(divisor)
            divisor_len = divisor_str.__len__()
            dividend_str = str(dividend)
            dividend_len = dividend_str.__len__()
            for pivot in range(1, dividend_len + 1):
                while dividend_str[offset] == '0':
                    offset += 1
                cur_dividend = dividend_str[offset: pivot]
                val_dividend = int(cur_dividend)
                # print(val_dividend, divisor, offset, pivot)
                if val_dividend < divisor:
                    if ret:  # no leading-zeros
                        ret.append('0')
                    continue
                ans = 0
                while val_dividend >= divisor:
                    ans += 1
                    val_dividend -= divisor
                ret.append('{}'.format(ans))
                dividend_str = '{}{}{}{}'.format(
                    dividend_str[:offset], 
                    '0' * (pivot - offset - str(val_dividend).__len__()),
                    str(val_dividend), 
                    dividend_str[pivot:])
            if not ret:
                ret = ['0']
            ret = int(''.join(ret))

        ret = ret if sign else -ret
        if ret < - 2 ** 31 or ret > 2 ** 31 - 1:
            # 如果除法结果溢出，则返回 2**31 − 1
            return 2 ** 31 - 1
        return ret
        