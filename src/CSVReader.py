def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader(object):
    pass
