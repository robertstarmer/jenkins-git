
class TestCase():

    @classmethod
    def setup_class(cls, name: str = None):
        super_name = cls.__name__ if name is None else name
        print(f"setup_class from {super_name}")


    def setup(self, name: str= None):
        super_name = self.__class__.__name__ if name is None else name
        print(f"setup from {super_name}")



    def teardown(self):
        print(f"teardown from: {self.__class__.__name__}")


    @classmethod
    def teardown_class(cls):
        print(f"teardown_class from: {cls.__name__}")
