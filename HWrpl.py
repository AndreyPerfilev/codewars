# Завершите метод/функцию, чтобы он преобразовывал слова, разделенные тире/подчеркиванием, в верблюжий регистр.
# Первое слово в выводе должно быть написано с заглавной буквы,
# только если исходное слово было написано с заглавной буквы
# (так называемый верхний верблюжий регистр, также часто называемый регистром Паскаля).
# Следующие слова всегда должны быть с заглавной буквы.
word= 'the_stealth_warrior'
word_camel=""
print(len(word))
for i in range(len(word)):
    if word[i-1] == '-' or word[i-1]=='_':
        word_camel += word[i].upper()
        print(i)
        print(word_camel)
    else:
        word_camel+= word[i]
word_camel=word_camel.replace('_','')
word_camel=word_camel.replace('-','')
print(word_camel)
# word = "the-stealth-warrior"
# word_list = []
# for i in word:
#     word_list.append(i)
#
# print(word_list)
# for i in range(len(word_list)):
#     print(i)
#     if i < len(word_list):
#         if (word_list[i] == ('-')) or (word_list[i] == ('_')):
#             word_list[i + 1] = word_list[i + 1].upper()
#             word_list[i] = ''
#         else:
#             word_list[i] = word_list[i]
#     else:
#         break
# print(*word_list.)
