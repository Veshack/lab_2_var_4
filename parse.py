def make_dictionary(s1, s2, file):
    l1 = []
    l2 = []
    for i in file:
        if s1 in i:
            l1.append(i)
        if s2 in i:
            l2.append(i)
    for j in range(len(l1)):
        l1[j] = l1[j].replace('    ', '').replace(f'<{s1}>', '').replace(f'</{s1}>\n', '')
        l2[j] = l2[j].replace('    ', '').replace(f'<{s2}>', '').replace(f'</{s2}>\n', '')
    return dict(zip(l2, l1))


file = open('currency.xml').readlines()
print(make_dictionary('NumCode', 'CharCode', file))
