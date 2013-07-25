# Get Script Variables: timestamp: 45926743
# Convert value for fan1_fault (enum) to a (enum): timestamp: 45926753
# generated script variable --> self.fan1_fault = True: timestamp: 45926758
# Convert value for fan2_fault to a (none): timestamp: 45926773
# generated script variable --> self.fan2_fault = "True": timestamp: 45926778
# Convert value for TEST_RUN to a (none): timestamp: 45926793
# generated script variable --> self.TEST_RUN = "r4": timestamp: 45926798
# Convert value for description to a (none): timestamp: 45926813
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 45926818
# Test Setup --> r4 Debug Level: 3: timestamp: 45926824
# Start Test --> : timestamp: 45927243
# Powerup Test Script: timestamp: 45927244
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 45927244
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 45927244
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 45927244
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 45927244
# Validation Timestamp: 45927320: timestamp: 45927320
# No Fans Available EICAS message: timestamp: 45927320

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0 and 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 45928244: timestamp: 45928244
# fan 2 should not power on: timestamp: 45928244

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 45928244: timestamp: 45928244
# fan 1 should not power on: timestamp: 45928244

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 45928244
