def solution(s):
    s = s.lower().split(" ")
    for i in range(len(s)):
        if s[i].isalpha():
            s[i]=s[i][0].upper()+s[i][1:]

    return " ".join(s)