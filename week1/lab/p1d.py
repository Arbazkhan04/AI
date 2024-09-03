def count_patteren(str1,str2):
    i = 0
    k = len(str1)
    ans = 0
    while(i+k <= len(str2)):

        if(str2[i:i+k] == str1):
            ans+=1
        
        i+=1
    return ans

print(count_patteren("ab","abab"))