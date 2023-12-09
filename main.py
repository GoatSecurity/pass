from itertools import permutations
print('''
 ___                                  _   ___                             _            
| . \ ___  ___ ___ _ _ _  ___  _ _  _| | /  _>  ___ ._ _  ___  _ _  ___ _| |_ ___  _ _ 
|  _/<_> |<_-<<_-<| | | |/ . \| '_>/ . | | <_/\/ ._>| ' |/ ._>| '_><_> | | | / . \| '_>
|_|  <___|/__//__/|__/_/ \___/|_|  \___| `____/\___.|_|_|\___.|_|  <___| |_| \___/|_|  
                                                                                        
                             A Tool By : github.com/GoatSecurity


''')
def get_inputs():
    inputs = []
    while True:
        inp = input("\nType a word (leave blank to finish): ")
        if inp == "":
            break
        inputs.append(inp)
    return inputs

def generate_passwords(inputs):
    passwords = []
    for r in range(1, len(inputs) + 1):
        for permutation in permutations(inputs, r):
            password = "".join(permutation)
            passwords.append(password)
    return passwords

def write_passwords_to_file(passwords, filename):
    with open(filename, 'w') as f:
        for password in passwords:
            f.write(password + '\n')

inputs = get_inputs()
passwords = generate_passwords(inputs)
write_passwords_to_file(passwords, 'passwords.txt')

print("\n\n\n\n              Total passwords generated:", len(passwords))

print("                Thanks For Using This Tool                  ")
