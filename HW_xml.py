import xml.etree.ElementTree as ET


def read_xml(file_path, word_max_len=6, top_words_amt=10):
    s = ''
    parser = ET.XMLParser(encoding='UTF-8')
    tree = ET.parse(file_path,parser)
    root = tree.getroot()
    new_list = root.findall('channel/item/description')
    for row in new_list:
        s+= (row.text)

    
    d = {}
    final_list = []


    my_list = s.replace(',',"").split()
    my_set = list(set(my_list))
    new_list = [i for i in my_set if len(i)> word_max_len]
    for i in new_list:
        d[i] = my_list.count(i)
    sorted_d = sorted(d.items(), key=lambda item : item[1], reverse=True)
    for i in range(top_words_amt):
        final_list.append(sorted_d[i][0])
    
    return final_list

print(read_xml('newsafr.xml'))