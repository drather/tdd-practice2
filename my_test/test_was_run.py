
from codes.was_run import WasRun


class TestWasRun:
    test = WasRun("testMethod")
    print(test.wasRun)
    test.run()
    print(test.wasRun)

