from xitwords import XitWord

test_word = XitWord()

print("Word Creation and Assignment Tests")
print(str(test_word))
print(int(test_word))
test_word.copy([1,2,3,4,5])
print(str(test_word))
print(int(test_word))
test_word.read([0,1,2,3,4,5])
print(str(test_word))
print(int(test_word))
test_word.read([1,2,3,4])
print(str(test_word))
print(int(test_word))
test_word.read([True, 1,2,3,4,5])
print(str(test_word))
print(int(test_word))

print(str(-test_word))

print("Word Addition and Subtraction Tests")
word_1 = XitWord([0,0,0,0, 1], word_length=5, base=10)
word_2 = XitWord([True, 1,0,0,0,0], word_length=5, base=10)
print(int(word_1 + word_2))
word_1.copy([True, 9,9,9,9, 9])
word_2.copy([True, 1,0,0,0,0])
print(int(word_1 + word_2))
print(str(word_1 - word_2))
word_1 += word_2

print(str(word_1))
test = [7,0,0,0,0]
word_1.copy(test)
word_2.copy([3,0,0,0,0])
print(str(word_1*word_2))
word_1 *= word_2
print(str(word_1))

word_1 = XitWord(word_length=2, base=64)
word_2 = XitWord(word_length=2, base=64)
word_1.copy([True, 1, 7])
word_2.copy([True, 7, 2])
print(int(word_1), int(word_2))

factor, remainder = divmod(word_1, word_2)
print(int(factor), int(remainder))
word_1 /= word_2
print(int(word_1))

word_1.copy(31)
word_2.copy(100)

print(str(word_1), str(word_2))
word_2.copy(word_1)
print(str(word_1), str(word_2))
test = 31
print(31 != word_1)
print(str(word_1 - word_2))
word_2 += word_1
print(str(word_1), str(word_2))

word_1 = XitWord(7, base=2)
word_2 = XitWord(3, base=3)

print(int(word_1*word_2))
print(str(word_1))
print(2 <<1 )
print(str(word_1 >> 2))
print(str(word_2))

x = XitWord(54321)
y = XitWord(67)
print(x)
print(y)
print(x/y)
