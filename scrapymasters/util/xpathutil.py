class XpathUtil:

    def __init__(self):
        pass

    @staticmethod
    def xpath_for_class(classname):
        return "*[contains(concat(' ', @class, ' '), ' " + classname + " ')]"
