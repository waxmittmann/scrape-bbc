class StringUtil:

    def __init__(self):
        pass

    @staticmethod
    def get_first(in_list, if_empty):
        if len(in_list) > 0:
            return in_list[0]
        else:
            return if_empty
