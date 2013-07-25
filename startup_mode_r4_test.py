# Get Script Variables: timestamp: 48190171
# generated script variable --> self.fan1_fault = True: timestamp: 48190186
# generated script variable --> self.fan2_fault = True: timestamp: 48190206
# generated script variable --> self.TEST_RUN = "r4": timestamp: 48190226
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 48190246
# Test Setup --> r4 Debug Level: 3: timestamp: 48190252
# Start Test --> : timestamp: 48190641
# Powerup Test Script: timestamp: 48190642
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 48190642
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 48190642
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 48190642
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 48190642
# Validation Timestamp: 48190702: timestamp: 48190702
# No Fans Available EICAS message: timestamp: 48190702

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0 and 0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# Validation Timestamp: 48191642: timestamp: 48191642
# fan 2 should not power on: timestamp: 48191642

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Validation Timestamp: 48191642: timestamp: 48191642
# fan 1 should not power on: timestamp: 48191642

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1 and 1: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 48191642
