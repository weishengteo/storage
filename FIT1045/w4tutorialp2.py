list = ['mom','daddy','racecar','mooooom','tttttttt']

def palindrome(list):
    my_list = []
    for word in range(len(list)):
        if list[word] == list[word][::-1]:
             my_list.append(list[word])
    return my_list

def vowel(list):
    my_list = palindrome(list)
    final_list = []
    vowel = ['aeiou']
    for word in range(len(list)):
        vowelcount = 0
        for letter in range(len(list(word))):
            if letter in vowel:
                vowelcount += 1
        wordcount = list(word).count()
        if vowelcount > wordcount - vowelcount:
            final_list.append(list(word))
            
print(palindrome(list))
print(vowel(list))
