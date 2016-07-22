def num_to_word(s):
    S = str(s)
    words = []
    directives = {
    '0':'zero', '1':'one', '2':'two', '3':'three', '4':'four',
    '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'
    }
    for in S:
        if each in directives:
            words.append(directives[each])
        else:
            words.append(each)
    return " ".join(words)
