def print_upper_word(words):
    
    for word in words:
        print(word.upper())
print_upper_word(["Python", "is", "really" , "cool"])

def print_upper_word2(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())
print_upper_word2(["eating","hungry","ELLA","BEAUTIFUL"])

def print_upper_word3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_word3(["eating","hungry","ELLA","BEAUTIFUL"], must_start_with=['E','B'])