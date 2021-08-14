def largest_divisible_power(integer, base):
    current_start = 0
    current_mod = 0
    while (int(integer/(base**(current_start+1))) != 0):
        next_power = current_start + 2**current_mod
        if int(integer/(base**next_power)) != 0:
            current_mod += 1
        else:
            current_start += 2**(current_mod - 1)
            current_mod = 0
    return current_start

def represent_integer(integer, base):
    return_toggle = (integer < 0)
    if return_toggle:
        integer = -integer
    largest_power = largest_divisible_power(integer, base)
    rep_list = max(largest_power + 1, 1)*[0]
    for power in range(0, len(rep_list))[::-1]:
        rep_list[power] = int(integer/(base**power))
        integer -= rep_list[power]*(base**power)
    return [return_toggle] + rep_list


def perform_carry(word_list, base):
    for xit in range(0, len(word_list)-1):
            if word_list[xit] < 0:
                multiplier = -int((word_list[xit] - base)/base)
                word_list[xit] += multiplier*base
                word_list[xit + 1] -= multiplier
            if word_list[xit] >= base:
                multiplier = int(word_list[xit]/base)
                word_list[xit] -= multiplier*base
                word_list[xit + 1] += multiplier


def add_words(word_1, word_2, subtraction=False):
    max_size = max(word_1.word_length, word_2.word_length)
    extend_1 = word_1.word + [0 for xit in range(0, max_size - word_1.word_length)]
    extend_2 = word_2.word + [0 for xit in range(0, max_size - word_2.word_length)]
    max_test = [extend_1[xit] + extend_2[xit] for xit in range(0, max_size)]
    max_test = [result for result in max_test if result != 0]
    if len(max_test) == 0:
        return_word = [0 for xit in range(0, max_size)]
        return_toggle = False
        return_base = word_1.base
    else:
        if max_test[-1] > 0:
            large_word = word_1
            small_word = word_2
            large_extend = extend_1
            small_extend = extend_2
            large_toggle = word_1.toggle
            small_toggle = word_2.toggle
            if subtraction:
                small_toggle = (not small_toggle)
        else:
            large_word = word_2
            small_word = word_1
            large_extend = extend_2
            small_extend = extend_1
            large_toggle = word_2.toggle
            small_toggle = word_1.toggle
            if subtraction:
                large_toggle = (not small_toggle)
        return_toggle = large_toggle
        subtract = (large_toggle != small_toggle)
        temp_result = [large_extend[xit] + ((-1)**int(subtract))*small_extend[xit] for xit in range(0, max_size)] + [0]
        perform_carry(temp_result, large_word.base)
        return_word = temp_result
        if return_word[-1] == 0:
            return_word = return_word[0:-1]
        return_base = large_word.base
    return return_word, return_toggle, return_base 

def multiply_words(word_1, word_2):
    return_toggle = (word_1.toggle != word_2.toggle)
    return_word = [0 for i in range(0, len(word_1) + len(word_2)+1)]
    return_base = word_1.base
    for xit_1 in range(0, len(word_1)):
        for xit_2 in range(0, len(word_2)):
            return_word[xit_1 + xit_2] += word_1.word[xit_1]*word_2.word[xit_2]
    perform_carry(return_word, return_base)
    return return_word, return_toggle, return_base

def divide_words(word_1, word_2):
    return_toggle = (word_1.toggle != word_2.toggle)
    return_word = [0 for i in range(0, 2*len(word_1))]
    return_base = word_1.base
    significant_power_1 = ([-1] + [i for i in range(0, len(word_1)) if word_1.word[i] !=0])[-1]
    significant_power_2 = ([-1] + [i for i in range(0, len(word_2)) if word_2.word[i] !=0])[-1]
    if significant_power_1 == -1 or significant_power_2 == -1:
        return return_word, return_toggle, return_base
    tmp_word_1 = [xit for xit in word_1.word]
    tmp_word_2 = [xit for xit in word_2.word[0:significant_power_2 + 1]]
    max_iter = 0
    while significant_power_1 >= 0 and max_iter < 15:
        max_iter += 1
        current_offset = significant_power_1 - significant_power_2
        mult_factor = 1
        if tmp_word_1[significant_power_1] < tmp_word_2[significant_power_2]:
            current_offset -= 1
            mult_factor = return_base
        if current_offset < 0:
            return_word[len(word_1):] = tmp_word_1
            perform_carry(return_word, return_base)
            return return_word, return_toggle, return_base
        for trial_mult in range(1, int(float(mult_factor*tmp_word_1[significant_power_1])/float(tmp_word_2[significant_power_2]))+ 1)[::-1]:
            temp_mult = [0 for i in range(0, len(word_1))]
            temp_mult[current_offset:significant_power_2 + 1] = [trial_mult*xit for xit in tmp_word_2]
            temp_mult = [tmp_word_1[i] - temp_mult[i] for i in range(0, len(word_1))]
            perform_carry(temp_mult, return_base)
            mult_sig = ([-1] + [i for i in range(0, len(word_1)) if temp_mult[i] !=0])[-1]
            if temp_mult[mult_sig] > 0:
                return_word[current_offset] += trial_mult
                tmp_word_1 = temp_mult
                break
        significant_power_1 = ([-1] + [i for i in range(0, len(word_1)) if tmp_word_1[i] !=0])[-1]

    return return_word, return_toggle, return_base