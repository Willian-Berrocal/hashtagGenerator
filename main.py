# Este programa devuelve una frase en forma de hastag, tal que solo la inicial de cada palabra es mayuscula
# tiempo de ejecucion es O(n), siendo n el len de el input

s = 'hello there thanks for trying my Kata'
# s = '    Hello     World   '
# s = 'CoDeWaRs is niCe'

last = ''
out = '#'

for c in s:
    if c.isalpha():
        if last == ' ' or last == '':
            out += c.capitalize()
        elif 'A' <= c <= 'Z':
            out += c.lower()
        else:
            out += c
    last = c

print(out)
