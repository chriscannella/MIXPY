import re
from operator import itemgetter

def parse_F(F):
    L = F / 8
    R = F % 8
    return F, (L,R)

def parse_string_rep(string_rep):
    match_string = "^(?P<OPNAME>\w*)(\s(?P<ADDRESS>\-?\d*)?(\,(?P<I>\d*))?(\((?P<FSTART>\d*)(\:(?P<FEND>\d*))?\))?)?$"
    m = re.match(match_string, string_rep)
    if m:
        return m.groupdict()
    return None

def valid_F(parsed_rep, instruction_info):
    if parsed_rep["FSTART"]:
        if not parsed_rep["FEND"]:
            F_val, F_range = parse_F(int(parsed_rep["FSTART"]))
            if "RANGE" in instruction_info["F"] and F_range[1] <= int(instruction_info["F"][-1]) and F_range[0] <=F_range[1]:
                return True, F_val
            elif "VAL" in instruction_info["F"] and F_val == int(instruction_info["F"][-1]):
                return True, F_val
            elif instruction_info["F"] == "ANY":
                return True, F_val
            else:
                return False, F_val
        else:
            F_range = (int(parsed_rep["FSTART"]), int(parsed_rep["FEND"]))
            F_val = 8*F_range[0] + F_range[1]
            if "RANGE" in instruction_info["F"] and F_range[1] <= min(int(instruction_info["F"][-1]), 7) and F_range[0] <= F_range[1] :
                return True, F_val
            elif instruction_info["F"] == "ANY":
                return True, F_val
            else:
                return False, F_val

    return True, instruction_info["normF"]
        
    