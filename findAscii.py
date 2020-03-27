with open("utils/load_data.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print("%d: %s" % (i, repr(line)))
