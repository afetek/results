# Get Script Variables: timestamp: 49544054
# generated script variable --> self.fan1_fault = True: timestamp: 49544069
# generated script variable --> self.fan2_fault = True: timestamp: 49544089
# generated script variable --> self.TEST_RUN = "r4": timestamp: 49544109
# generated script variable --> self.description = "Fan1 faulted Fan2 faulted at startup mode": timestamp: 49544129
# Test Setup --> r4 Debug Level: 3: timestamp: 49544135
# Start Test --> : timestamp: 49544445
# Powerup Test Script: timestamp: 49544446
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 49544446
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 49544446
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 49544446
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 49544446
# 
# Validation Timestamp: 49544504: timestamp: 49544504
# No Fans Available EICAS message: timestamp: 49544504

def test1_test_test():
    """
     run r4 test 1: Confirm self.model.eicas is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 49545446: timestamp: 49545446
# fan 2 should not power on: timestamp: 49545446

def test2_test_test():
    """
     run r4 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 49545446: timestamp: 49545446
# fan 1 should not power on: timestamp: 49545446

def test3_test_test():
    """
     run r4 test 3: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# Test Done --> r4: timestamp: 49545446
