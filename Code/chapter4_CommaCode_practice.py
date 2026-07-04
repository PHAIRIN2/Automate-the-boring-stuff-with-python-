def comma_code(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return str(items[0])
    else:
        result = " , ".join(str(item) for item in items[:-1])
        result += " and " + str(items[-1])
        return result


spam = ["apples", "bananas", "tofu", "cats"]
print(comma_code(spam))
