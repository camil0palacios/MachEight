def find_pairs(a, sum):
    ans, m = [], {}
    for i in a:
        val = sum - i
        if val in m:
            ans.append([i, sum - i])
        m[i] = 1
    return ans

def main():
    f = open('input.txt', 'r')
    a, sum = f.read().split(' ')
    a = [int(i) for i in a.split(',')]
    for p in find_pairs(a, int(sum)):
        print(f"{p[0]},{p[1]}")

main()