# Get Script Variables: timestamp: 49436867
# generated script variable --> self.fan1_fault = False: timestamp: 49436882
# generated script variable --> self.fan2_fault = True: timestamp: 49436902
# generated script variable --> self.TEST_RUN = "r3": timestamp: 49436922
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 49436942
# Test Setup --> r3 Debug Level: 3: timestamp: 49436948
# Start Test --> : timestamp: 49437196
# Powerup Test Script: timestamp: 49437197
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 49437197
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 49437197
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 49437197
# ----------------
# Validation Timestamp: 49437229: timestamp: 49437229
# fan 1 should power on: timestamp: 49437229

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# ----------------
# Validation Timestamp: 49438197: timestamp: 49438197
# fan 2 should not power on: timestamp: 49438197

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# ----------------
# Validation Timestamp: 49438197: timestamp: 49438197
# Both fans are Available EICAS message: timestamp: 49438197

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r3: timestamp: 49438197
