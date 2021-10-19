class Rain:

    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Rain.__instance is None:
            Rain()
        return Rain.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Rain.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Rain.__instance = self

if __name__ == '__main__':
    rain = Rain()
    print(rain)

    rain = Rain.get_instance()
    print(rain)

    rain = Rain.get_instance()
    print(rain)

    print("this supposed not to happen")