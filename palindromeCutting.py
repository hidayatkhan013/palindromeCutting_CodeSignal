# def palindromeCutting(s):
    
    
#     for _ in range(1,len(s)+1):
#         kk=[]
#         for i in range(1,len(s)+1):
#             kk.append(s[:i])
#             pel=[]
#             for k in kk:
#                 if k==k[::-1]:
#                     pel.append(k)
#         s=s.replace(pel[-1],"")
#         if s=="":
#             break
            
            
#     return s




# print(palindromeCutting("aaacodedoc"))


def palindromeCutting(s):
    for _ in range(1,len(s)+1):
        kk=[]
        pel=[]
        for i in range(1,len(s)+1):
            rev=s[:i]
            if rev==rev[::-1]:
                pel.append(rev)
        s=s.replace(pel[-1],"")
        if not s:
            break
    return s

print(palindromeCutting("aaacodedoc"))