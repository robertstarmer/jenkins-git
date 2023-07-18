
import conftest
import sys
import _pytest.config


class TestCase():

    @classmethod
    def setup_class(cls, name: str = None):
        super_name = cls.__name__ if name is None else name
        print(f"setup_class from {super_name}")
        pytest_cfg = _pytest.config.get_config() # updated for pytest 4.x
        parser = pytest_cfg._parser
        conftest.pytest_addoption(parser)
        cmdline_options = parser.parse_known_args(sys.argv)
        print(f"cmdline_options.number: {cmdline_options.number}")


    def setup(self, name: str= None):
        super_name = self.__class__.__name__ if name is None else name
        print(f"setup from {super_name}")



    def teardown(self):
        print(f"teardown from: {self.__class__.__name__}")


    @classmethod
    def teardown_class(cls):
        print(f"teardown_class from: {cls.__name__}")
