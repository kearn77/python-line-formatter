# Get key attributes of a line of text.
# Think about possible alternatives to '_'.
def get_attrs(ln: str) -> list[tuple]:
    words = " $&#".join(ln.split(" ")).split("$&#")
    return list(zip(words, [len(word) for word in words]))

# Find the index that corresponds to a line 
# split at an arbitrary length.  Splits at 
# the beginning of a string.
def split_at(ln: list[tuple], length: int) -> int:
    lnLength = 0
    for index, value in  enumerate(ln):
        _, y = value
        lnLength += y
        if lnLength > length:
            return index
        elif index+1 == len(ln):
            return index 
    
# Returns a string split at an arbitrary length.
# Defaults to eighty, the line length recommended
# for code in PEP8.

def keep_line(ln: str, length: int = 80) -> str:
    if len(ln) <= length and ln != '\n':
        return ln.rstrip()
    elif len(ln) <= length and ln == '\n':
        return ln
    
    word_tuples = get_attrs(ln)
    current_line = [a for a, _ in word_tuples]
    keep = current_line[:split_at(word_tuples,length)]
    return ''.join(keep).rstrip()

# Returns the leftover portion of a string split
# at an arbitrary line length.
def send_line(ln: str, length: int = 80) -> str:
    if len(ln) <= length:
        return ''
    
    word_tuples = get_attrs(ln)
    current_line = [a for a, _ in word_tuples]
    send = current_line[split_at(word_tuples, length):]
    send_str = ''.join(send).lstrip()

    return send_str.rstrip() + ' '