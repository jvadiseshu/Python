#palindrom function

#Dry method
def palindrome(str):
    str_len = len(str)
    print(f"\nThe input string length is {str_len:.2f}")
    for i in range(int(str_len/2)):
        if str[i] != str[str_len-i-1]:
            print(f"\n the {i}th character && {str_len-1-i}th character are", str[i], str[str_len-i-1])
            print(f"The given string {str} is not a palinrome")
            return 0
        else:
            return 1

#palindrome check using string slicing method
def palindrome1(str):
    if(str == str[::-1]):
        return 1
    else:
        return 0

def main():
    str = input("enter a string")
    if(palindrome1(str) == 0):
        print("\n Not a palindrome")
    else:
        print("\n Palindrome")
    

if __name__=="__main__":
    main()
