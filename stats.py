



def GetWordCount(_string):
    _list = _string.split()
    return len(_list)


def CountCharacters(_string):
    new_dict = dict()
    for char in _string:
        c = char.lower()
        if c not in new_dict:
            new_dict[c] = 1
        else:
            new_dict[c] += 1

    return new_dict

def SortedReport(_dict):
    _list = list(_dict.items())
    _list.sort(reverse = True, key = lambda x: x[1])
    return _list
