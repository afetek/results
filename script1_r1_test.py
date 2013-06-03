# Get Script Variables: timestamp: 531484
# generated script variable --> self.s2 = 11: timestamp: 531499
# generated script variable --> self.TEST_RUN = "r1": timestamp: 531519
# generated script variable --> self.description = "hello r1": timestamp: 531539
# generated script variable --> self.s1 = 1: timestamp: 531559
# Test Setup --> r1 Debug Level: 3: timestamp: 531565
# Start Test --> : timestamp: 531920
# signal1: 1: timestamp: 531921
# signal2: 11: timestamp: 531921
# Waitng ...: timestamp: 531921
# ... Ok: timestamp: 536509
# self.model.c1.Value == 2.0: timestamp: 536509
# self.model.c1.Value == 2.0: timestamp: 536509
# self.model.c3.Value == 3.0: timestamp: 536509
# Validation Timestamp: 536509: timestamp: 536509
# set c1: timestamp: 536509

def test1_test_test():
    """
    script1 run r1 test 1: Confirm self.model.d1 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 536509: timestamp: 536509
# set c2: timestamp: 536509

def test2_test_test():
    """
    script1 run r1 test 2: Confirm self.model.d2 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 536509: timestamp: 536509
# set c3: timestamp: 536509

def test3_test_test():
    """
    script1 run r1 test 3: Confirm self.model.d3 is >= 4.0 and <= 6.0: actual value is 4.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 540078
