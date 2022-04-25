def load_code_file(file_path):
    with open(file_path) as f:
        lines = f.read()
    char_list = []

    for i in lines:
        char_list.append(i)
    
    return char_list

def write_to_file(token):
    f = open('output2.vctok', 'w')
    token_set = set(token)
    print(token_set)
    for i in token_set:
        f.write(i+'\n')
    f.close()
