"""
有一段二进制数据码流 n，请将数据切分成 3 段，每一段得到相同的值
例如：输入为 1010010，可以切分为 10 / 10 / 010 三段
如果无法做到输出 -1，如果输入码全为 0，输出 -1

时间要求: 10ms/20ms
3 <= n.length() <= 50000
"""


def code_split(a=None):
    s = []
    if a is None:
        a = input().split()
    cnt, j = 0, 0
    for i, c in enumerate(a):
        if c == '1':
            cnt += 1
        s.append(c)
        j += 1

    if cnt % 3 != 0 or cnt == 0:
        print("-1 -1")
        return

    ans1, ans2, ans3 = 0, 0, 0
    for i, c in enumerate(s):
        if c == '1':
            ans1 += 1
            if ans1 == 1:
                ans1 = i
                break
    for i, c in enumerate(s):
        if c == '1':
            ans2 += 1
            if ans2 == cnt // 3 + 1:
                ans2 = i
                break
    for i, c in enumerate(s):
        if c == '1':
            ans3 += 1
            if ans3 == cnt // 3 * 2 + 1:
                ans3 = i
                break
    
    while ans3 < j and s[ans1] == s[ans2] == s[ans3]:
        ans1 += 1
        ans2 += 1
        ans3 += 1
    # print(ans1, ans2, ans3)

    if ans3 == j:
        print("{} {} {}".format(
            ''.join(s[:ans1]), 
            ''.join(s[ans1:ans2]), 
            ''.join(s[ans2:])))
    else:
        print("-1 -1")
    

"""
糖果天王:
首先统计这个字符串1的个数，因为把这个字符串分为3段，
要求这三段所表示的二进制是相同的，就是要求这三段里面的数字1的位置必须是相同的，
也就是说有3个相同的二进制数，因此这三段的二进制数就是3个一样的数。

然后枚举截断位置，三个for循环依次用三个不同的变量依次记录第一出现1的下标ans1，
cnt/3+1出现1的位置ans2，cnt/3*2+1的位置ans3；

然后再用 a[ans1]==a[ans2]&&a[ans2]==a[ans3]&&ans<j 判断，
ans1++,ans2++,ans3++; 相同就往后移，一旦不相同或到了最后就截断
"""

if __name__ == "__main__":
    code_split("1010000101001010")
    pass