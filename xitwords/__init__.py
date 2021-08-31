from xitwords.math import *

class XitWord ():
#===============================================================================
# Represents a word of xits in specified base.
# Toggle is included to represent negative numbers.
#===============================================================================

    def __init__ (self, value=[], word_length=0, base=10):
        self.base = base
        self.word = []
        self.word_length = word_length
        self.toggle = False
        self.overflow = False
        if value:
            if word_length:
                self.word = self.word_length*[0]
                self.read(value)
            else:
                self.copy(value)
        else:
            if word_length:
                self.word = self.word_length*[0]

    def read_word(self, other_word):
        self.read_int(int(other_word))
        self.toggle = other_word.toggle
        
    def read_list(self, other_word):
        temp_list = [xit for xit in other_word]
        if (len(other_word) > 0) and isinstance(other_word[0], bool):
            self.toggle = other_word[0]
            temp_list = temp_list[1:]
        perform_carry(temp_list, self.base)
        if len(temp_list) > 0:
            while len(temp_list) > 0 and temp_list[-1] == 0:
                temp_list = temp_list[0:-1]
        if (len(temp_list) > 0) and temp_list[-1] < 0:
            self.toggle = not self.toggle
            temp_list[-1] *= -1
        if (len(temp_list) > 0) and temp_list[-1] >= self.base:
            temp_list = temp_list[0:-1] + represent_integer(temp_list[-1], self.base)[1:]
        if len(temp_list) > self.word_length:
            self.word = [int(xit) for xit in temp_list[0:self.word_length]]
            self.overflow = True
        else:
            self.word = [0 for i in range(0, self.word_length)]
            self.word[0:len(temp_list)] = [int(xit) for xit in temp_list]
        
    def read_int(self, integer):
        self.read_list(represent_integer(integer, self.base))
    
    def read(self, other):
        if isinstance(other, int):
            self.read_int(other)
        elif isinstance(other, list):
            self.read_list(other)
        elif isinstance(other, XitWord):
            self.read_word(other)
        
    def copy_word(self, other_word):
        self.copy_int(int(other_word))
        
    def copy_list(self, other_word):
        temp_list = [xit for xit in other_word]
        if (len(other_word) > 0) and isinstance(other_word[0], bool):
            self.toggle = other_word[0]
            temp_list = temp_list[1:]
        perform_carry(temp_list, self.base)
        if (len(temp_list) > 0) and temp_list[-1] < 0:
            self.toggle = not self.toggle
            temp_list[-1] *= -1
        if (len(temp_list) > 0) and temp_list[-1] >= self.base:
            temp_list = temp_list[0:-1] + represent_integer(temp_list[-1], self.base)[1:]
        self.word = temp_list
        self.word_length = len(temp_list)
        self.overflow = False
        
    def copy_int(self, integer):
        self.copy_list(represent_integer(integer, self.base))
    
    def copy(self, other):
        if isinstance(other, int):
            self.copy_int(other)
        elif isinstance(other, list):
            self.copy_list(other)
        elif isinstance(other, XitWord):
            self.copy_word(other)
        
    def overflown(self):
        return self.overflow
        
    def __len__(self):
        return len(self.word)
    
    def __or__(self, new_base):
        return XitWord(int(self), base=new_base)
    
    def __xor__(self, new_base):
        return_val = int(self)
        self.base = new_base
        self.copy(return_val)
        return self
        
    def __add__(self, other):
        if other.base != self.base:
            temp_other = other | self.base
        else:
            temp_other = other
        return_list, return_toggle, return_base = add_words(self, temp_other)
        while (return_list[-1] == 0) and len(return_list)>1:
            return_list = return_list[0:-1]
        return XitWord([return_toggle] + return_list, base=return_base)
    
    def __sub__(self, other):
        if other.base != self.base:
            temp_other = other | self.base
        else:
            temp_other = other
        return_list, return_toggle, return_base = add_words(self, temp_other, subtraction=True)
        while (return_list[-1] == 0) and len(return_list)>1:
            return_list = return_list[0:-1]
        return XitWord([return_toggle] + return_list, base=return_base)
    
    def __mul__(self, other):
        if other.base != self.base:
            temp_other = other | self.base
        else:
            temp_other = other
        return_list, return_toggle, return_base = multiply_words(self, temp_other)
        while (return_list[-1] == 0) and len(return_list)>1:
            return_list = return_list[0:-1]
        return XitWord([return_toggle] + return_list, base=return_base)
    
    def __divmod__(self, other):
        if other.base != self.base:
            temp_other = other | self.base
        else:
            temp_other = other
        return_list, return_toggle, return_base = divide_words(self, temp_other)
        factor_list = return_list[0:len(self)]
        remainder_list = return_list[len(self):]
        while (factor_list[-1] == 0) and len(factor_list)>1:
            factor_list = factor_list[0:-1]
        while (remainder_list[-1] == 0) and len(remainder_list)>1:
            remainder_list = remainder_list[0:-1]
        return_word = XitWord([return_toggle] + factor_list, base=return_base)
        remainder_word = XitWord([return_toggle] + remainder_list, base = return_base)
        if len([xit for xit in other.word if xit != 0])==0:
            return_word.overflow = True
        return return_word, remainder_word
    
    def __truediv__(self, other):
        factor, remainder = divmod(self, other)
        return factor
    
    def __mod__(self, other):
        factor, remainder = divmod(self, other)
        return remainder
        
    
    def __iadd__(self, other):
        if other.base != self.base:
            temp_other = other | self.base
        else:
            temp_other = other
        return_list, return_toggle, return_base = add_words(self, temp_other)
        self.read([return_toggle] + return_list)
        return self
    
    def __isub__(self, other):
        if other.base != self.base:
            temp_other = other | self.base
        else:
            temp_other = other
        return_list, return_toggle, return_base = add_words(self, temp_other, subtraction=True)
        self.read([return_toggle] + return_list)
        return self
    
    def __imul__(self, other):
        if other.base != self.base:
            temp_other = other | self.base
        else:
            temp_other = other
        return_list, return_toggle, return_base = multiply_words(self, temp_other)
        self.read([return_toggle] + return_list)
        return self
    
    def __itruediv__(self, other):
        if other.base != self.base:
            temp_other = other | self.base
        else:
            temp_other = other
        return_list, return_toggle, return_base = divide_words(self, temp_other)
        prev_overflow = self.overflow
        self.read([return_toggle] + return_list)
        self.overflow = prev_overflow
        if len([xit for xit in other.word if xit != 0])==0:
            self.overflow = True
        return self
    
    def __neg__(self):
        if self != 0:
            return XitWord([not self.toggle] + self.word,word_length=self.word_length, base=self.base)
        else:
            return self
    
    def index_grabber(self, index):
        if index == 0:
            return self.toggle
        else:
            return self.word[len(self.word) - index]

    def index_setter(self, index, value):
        if index == 0:
            self.toggle = value
        else:
            self.word[len(self.word) - index] = value
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            indices = list(range(*key.indices(len(self.word) + 1)))
            return_toggle = False
            if 0 in indices:
                return_toggle = self.index_grabber(0)
                indices.remove(0)
            return_list = [self.index_grabber(i) for i in indices]
            return XitWord([return_toggle] + return_list[::-1], word_length=len(return_list), base=self.base)
        return self.index_grabber(key)
    
    def __setitem__(self, key, value):
        self.overflow = False
        if isinstance(key, slice):
            indices = list(range(*key.indices(len(self.word) + 1)))
            word_value = XitWord(value, word_length=(len(indices) - int(0 in indices)), base=self.base)
            if 0 in indices:
                self.index_setter(0, word_value[0])
                indices.remove(0)
            for set_key,i in enumerate(indices):
                self.index_setter(i, word_value[set_key + 1])
        else:
            self.index_setter(key, value)
    
    def __eq__(self, other):
        return int(self) == int(other)
    
    def __ne__(self, other):
        return int(self) != int(other)
    
    def __lt__(self, other):
        return int(self) < int(other)
    
    def __le__(self, other):
        return int(self) <= int(other)
    
    def __gt__(self, other):
        return int(self) > int(other)
    
    def __ge__(self, other):
        return int(self) >= int(other)
    
    def __lshift__(self, shift):
        if shift < 0:
            return self >> -shift
        return XitWord(([self.toggle] + shift*[0] + self.word), word_length = len(self) + shift, base = self.base)
    
    def __rshift__(self, shift):
        if shift < 0:
            return self << -shift
        return XitWord(([self.toggle] + self.word + shift*[0]), word_length = len(self) + shift, base = self.base)
            
    def __str__(self):
        toggle_string = "+"
        if self.toggle:
            toggle_string = "-"
        return_string = "|".join([toggle_string] + [str(xit) for xit in self.word[::-1]])
        return "|" + return_string + "|"
        
    def __int__(self):
        return int(((-1)**(self.toggle))*sum([self.word[xit]*(self.base)**xit for xit in range(0, self.word_length)]))
    
    def __obj__(self):
        return True