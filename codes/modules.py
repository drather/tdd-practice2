class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        print("setUp method done")

    def run(self):
        print("TestCase.run method start")
        self.setUp()
        method = getattr(self, self.name)
        method()

    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.log = "setUp " + "testMethod "

    def testMethod(self):
        self.wasRun = 1

