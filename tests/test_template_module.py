import unittest

from src.codegenlib.templateModule import TemplateModule

testModule = TemplateModule(
    name="test-module",
    templates_files=[]
    )

class TestSimple(unittest.TestCase):
    

    def test_module_path(self):
        path = testModule.getModulePath()
        print(path)
        self.assertEqual(testModule.name, "test-module")


if __name__ == '__main__':
    unittest.main()