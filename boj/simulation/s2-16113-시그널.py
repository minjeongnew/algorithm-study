from pprint import pprint


nums = [[0, ["###",
            "#.#",
            "#.#",
            "#.#",
            "###"]],
        [1, ["#",
            "#",
            "#",
            "#",
            "#"]],
        [2, ["###",
            "..#",
            "###",
            "#..",
            "###"]],
        [3, ["###",
            "..#",
            "###",
            "..#",
            "###"]],
        [4, ["#.#",
            "#.#",
            "###",
            "..#",
            "..#"]],
        [5, ["###",
            "#.",
            "###",
            "..#",
            "###"]],
        [6, ["###",
            "#.",
            "###",
            "#.#",
            "###"]],
        [7, ["###",
            "..#",
            "..#",
            "..#",
            "..#"]],
        [8, ["###",
            "#.#",
            "###",
            "#.#",
            "###"]],
        [9, ["###",
            "#.#",
            "###",
            "..#",
            "###"]]]
n = int(input())
s = input()
cut = n // 5
sig = [s[i:i+cut] for i in range(0, n, cut)]
pprint(sig)
s_k = list(x[1] for x in nums)
pprint(s_k)
i = 0
print(sig[:][i:i+3])
answer = ""
while True:
    if i == cut:
        break
    if sig[i:i+3] in s_k:
        print(sig[i:i+3])
        i += 3
    elif sig[i:i+1] in s_k:
        print(sig[i:i+1])
        i += 1
    else:
        i += 1
