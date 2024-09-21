#Check if vowel is present or not

#vowels - a,e,i,0,u

def Is_vowel_present(str):
    if 'a' in str or 'e' in str or 'i' in str or 'o' in str or 'u' in str:
        return 1
    else:
        return 0

def Is_vowel_present1(str):
    var = 0
    for s in str:
        if s in "aeiou":
            return 1
        else:
            return 0

def List_vowel_index(str):
     Dict = {}
     index = 0
     print(enumerate(str))
     for i in str:
         if i=='a' or i =='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U':
             Dict[i] = index
     index+=1
     print("\nthe vowels in the str")
     print(dict)


def main():
    str = input("Enter a string here :: ")
    if Is_vowel_present(str) == 1:
        print("\nIn the given string vowel is present")
#        List_vowel_index(str)
    else:
        print("\nIn the givien string vowel is not present")

if __name__=="__main__":
    main()
