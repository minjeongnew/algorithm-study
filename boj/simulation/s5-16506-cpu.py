import sys

opcode = {"ADD": 0, "ADDC": 1,
          "SUB": 2, "SUBC": 3,
          "MOV": 4, "MOVC": 5,
          "AND": 6, "ANDC": 7,
          "OR": 8, "ORC": 9,
          "NOT":10,
          "MULT": 12, "MULTC": 13,
          "LSFTL": 14, "LSFTLC": 15,
          "LSFTR": 16, "LSFTRC": 17,
          "ASFTR": 18, "ASFTRC": 19,
          "RL": 20, "RLC": 21,
          "RR": 22, "RRC": 23}
tmp = bin(10)[2:]
# print(tmp.zfill(6))


def solve(op, rd, ra, rb):
    answer = ""
    deci_op = opcode[op]
    bin_op = bin(deci_op)[2:].zfill(5)
    answer += bin_op
    if bin_op[4] == "1":
        rb = bin(int(rb))[2:].zfill(4)
    elif bin_op[4] == "0":
        rb = bin(int(rb))[2:].zfill(3) + "0"
    answer += "0"
    rd = bin(int(rd))[2:].zfill(3)
    answer += rd
    if op == "MOV" or op == "MOVC" or op == "NOT":
        ra = "000"
    else:
        ra = bin(int(ra))[2:].zfill(3)
    answer += ra
    answer += rb
    print(answer)


n = int(sys.stdin.readline())
for _ in range(n):
    op, rd, ra, rb = map(str, sys.stdin.readline().split())
    solve(op, rd, ra, rb)