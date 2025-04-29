import sys

# Unicode
# bytes Datatype

# default encoding scheme of system can get by
print(sys.stdin.encoding)

s = 'Hi'
print(type(s))
print(type('Hello'))

by = b'\xe0\xa4\x85'
print(type(by))
print(type(b'\xee\x84\x65'))

# string can be 'encode' back to bytes and bytes can be 'encode' back to string

eng = 'A B C D'
dev = 'अ इ उ ऋ'

print(type(eng))
print(type(dev))

print(eng.encode('utf-8'))
print(eng.encode('utf-16'))
print(dev.encode('utf-8'))
print(dev.encode('utf-16'))


print('\ndecode bytes to string')

print(b'A B C D'.decode('utf-8'))
print(b'\xff\xfeA\x00 \x00B\x00 \x00C\x00 \x00D\x00'.decode('utf-16'))
print(b'\xe0\xa4\x85 \xe0\xa4\x87 \xe0\xa4\x89 \xe0\xa4\x8b'.decode('utf-8'))
print(b'\xff\xfe\x05\t \x00\x07\t \x00\t\t \x00\x0b\t'.decode('utf-16'))






