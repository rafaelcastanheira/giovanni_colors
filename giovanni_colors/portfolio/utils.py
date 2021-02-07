

def split_by_columns(art_list):
    first, second, third = [], [], []
    counter = 1

    for x in art_list:
        if counter == 1:
            first.append(x)
            counter += 1
        elif counter == 2:
            second.append(x)
            counter += 1
        else:
            third.append(x)
            counter = 1

    return {
        "first": first,
        "second": second,
        "third": third
    }
