text_w = open(
    'The Zen of Python.txt', 'w'
)

text_w.write('''

The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!

''')

text_w.close()

text_r = open('The Zen of Python.txt', 'r')
text_read_str = text_r.read()
print(text_read_str)
word_s = []

def check_text(text):
    new_text = text.replace('.', '\n').split()
    new_text = list(new_text)
    print(new_text)
    for i in new_text:
        if i.startswith('c') or i.startswith('C'):
            word_s.append(i)

check_text(text_read_str)

print(f'This words title on "c" and "C" {word_s}')

text_r.close()
