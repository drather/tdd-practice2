from codes.modules import WasRun, TestCase


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self):
        self.test.run()
        assert self.test.wasSetUp


class TestWasRun:
    test = WasRun("testMethod")
    test.run()


if __name__ == '__main__':
    TestCaseTest("testRunning").run()
