#Lab 7

#Finds the edit distance between two strings
def edit_distance(s1,s2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    if s1[0] == s2[0]:
        return edit_distance(s1[1:],s2[1:])
    s1
    return 1 + min(edit_distance(s1,s2[1:]), edit_distance(s1[1:],s2[1:]), edit_distance(s1[1:],s2))
                                    
                                    
def main():
    print(edit_distance("yeet","yoot"))
main()