str="khokho"
half=int(len(str)/2)
if len(str)%2==0:
    first_str=str[:half]
    second_str=str[half:]
else:
    first_str=str[:half]
    second_str=str[half+1:]
if first_str==second_str:
    print(str,"symmetrical")
else:
    print(str,"not symmetrical")
#plindrome
if first_str== second_str[-1::-1]:
    print("palimdrome")
else:
    print("not palindrome")