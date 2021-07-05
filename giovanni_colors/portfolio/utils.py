
def split_by_rows(art_list):

    return {
        "first": art_list[0:3] if len(art_list) >= 2 else [],
        "second": art_list[3:6] if len(art_list) >= 4 else [],
        "third": art_list[6:9] if len(art_list) >= 6 else [],
        "forth": art_list[9:12] if len(art_list) >= 8 else [],
        "fifth": art_list[12:15] if len(art_list) >= 10 else [],
        "sixth": art_list[15:18] if len(art_list) >= 12 else [],
        "seventh": art_list[18:21] if len(art_list) >= 14 else [],
        "eighth": art_list[21:24] if len(art_list) >= 16 else [],
        "ninth": art_list[24:27] if len(art_list) >= 18 else [],
        "tenth": art_list[27:30] if len(art_list) >= 20 else [],
    }


print(split_by_rows(
    [1,2,3,4]
))