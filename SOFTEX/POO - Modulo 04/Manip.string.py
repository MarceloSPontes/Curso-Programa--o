ling = '                                 PYTHON    '
x = ling.strip()
texto1 = 'Python,C,C++,Java,JavaScript'
linguagens = texto1.split(',')
texto2 = ling.replace('                                 PYTHON    ','PYTHON')
print('A linguagem predileta dos programadores é',x)
print('Em ordem, as mais queridas são:')
for i in linguagens:
    print(i)
print('Definitivamente, prefiro progamar em:',texto2)