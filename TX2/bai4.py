file = open('doc_ghi_file.txt', 'r', encoding='utf-8')
read_content = file.readlines()
print(read_content)
file.close()