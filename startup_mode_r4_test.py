# Get Script Variables: timestamp: 44492153
# Conversion for fan1_fault (enum) is (enum): timestamp: 44492163
# generated script variable --> self.fan1_fault = True: timestamp: 44492168
# Conversion for fan2_fault is (none): timestamp: 44492183
# generated script variable --> self.fan2_fault = "True": timestamp: 44492188
# Conversion for TEST_RUN is (none): timestamp: 44492203
# generated script variable --> self.TEST_RUN = "r4": timestamp: 44492208
# Conversion for description is (none): timestamp: 44492223
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 44492228
# Test Setup --> r4 Debug Level: 3: timestamp: 44492234
# Start Test --> : timestamp: 44492574
# Powerup Test Script: timestamp: 44492575
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 44492575
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 44492575
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 44492575
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 44492575
# Validation Timestamp: 44492622: timestamp: 44492622
# No Fans Available EICAS message: timestamp: 44492622

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0 and 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 44493575: timestamp: 44493575
# fan 2 should not power on: timestamp: 44493575

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 44493575: timestamp: 44493575
# fan 1 should not power on: timestamp: 44493575

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 44493575
