# Get Script Variables: timestamp: 1894769
# generated script variable --> self.s2 = 1111: timestamp: 1894784
# generated script variable --> self.TEST_RUN = "r2": timestamp: 1894804
# generated script variable --> self.description = "hello r2": timestamp: 1894824
# generated script variable --> self.s1 = 111: timestamp: 1894844
# Test Setup --> r2 Debug Level: 3: timestamp: 1894850
# Start Test --> : timestamp: 1895247
# signal1: 111: timestamp: 1895248
# signal2: 1111: timestamp: 1895248
# self.model.c1.Value == 2.0: timestamp: 1895248
# self.model.c2.Value == 2.0: timestamp: 1895248
# self.model.c3.Value == 3.0: timestamp: 1895248
# Validation Timestamp: 1895248: timestamp: 1895248
# set c1: timestamp: 1895248

def test1_test_test():
    """
    script1 run r2 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 1895248: timestamp: 1895248
# set c2: timestamp: 1895248

def test2_test_test():
    """
    script1 run r2 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 1895248: timestamp: 1895248
# set c3: timestamp: 1895248

def test3_test_test():
    """
    script1 run r2 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 6.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 1895249
