class string_util():

    @staticmethod
    def get_first(list, ifEmpty):
        if len(list) > 0:
            return list[0]
        else:
            return ifEmpty