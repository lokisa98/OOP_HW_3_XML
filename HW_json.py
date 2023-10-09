import json

def read_json(file_path, word_max_len=6, top_words_amt=10):
    s = ""
    d = {}
    final_list = []
    with open (file_path,encoding='utf-8') as file:
        new_json = json.load(file)
    a = new_json['rss']['channel']['items']
    for row in a:
        s += row['description']
    my_list = s.replace(',',"").split()
    my_set = list(set(my_list))
    new_list = [i for i in my_set if len(i)> word_max_len]
    for i in new_list:
        d[i] = my_list.count(i)
    sorted_d = sorted(d.items(), key=lambda item : item[1], reverse=True)
    for i in range(top_words_amt):
        final_list.append(sorted_d[i][0])
    
    return final_list
    
print(read_json('newsafr.json')) 