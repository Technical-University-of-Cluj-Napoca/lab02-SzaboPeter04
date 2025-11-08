from collections import defaultdict

def group_anagrams(strs:list[str])->list[list[str]]:
    anagrams=defaultdict(list)
    for word in strs:
        char_count=26*[0]
        for char in word:
            index=ord(char)-ord('a')
            char_count[index]+=1
        key="#".join(map(str,char_count))
        #anagrams[tuple(char_count)].append(word)
        anagrams[key].append(word)
    return list(anagrams.values()) 

if __name__=="__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    print(group_anagrams([""]))
    print(group_anagrams(["r"]))