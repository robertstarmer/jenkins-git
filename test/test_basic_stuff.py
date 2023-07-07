

# import _pytest.config
# import conftest

import test_case


class TestBasicStuff(test_case.TestCase):

    @classmethod
    def setup_class(cls, name: str = None):
        super_name = cls.__name__ if name is None else name
        super().setup_class(super_name)


    def setup(self, name: str= None):
        super_name = self.__class__.__name__ if name is None else name
        super().setup(super_name)

    def teardown(self):
        super().teardown()


    @classmethod
    def teardown_class(cls):
        super().teardown_class()

    def test_one(self):
        print("I am test one lets pass")
        dict_to_save = {
            "zone": 94.32,
            "area": "somewhere",
            "integer": 'false'
        }
        with open("my_file.txt", "w") as f:
            for k, v in dict_to_save.items():
                f.write(f"{k}={v}\n")
        assert True