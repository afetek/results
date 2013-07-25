# Get Script Variables: timestamp: 68875151
# generated script variable --> self.fan1_fault = False: timestamp: 68875166
# generated script variable --> self.fan2_fault = True: timestamp: 68875186
# generated script variable --> self.TEST_RUN = "r3": timestamp: 68875206
# generated script variable --> self.description = "Fan1 ok Fan2 faulted at startup mode": timestamp: 68875226
# Test Setup --> r3 Debug Level: 3: timestamp: 68875232
# Start Test --> : timestamp: 68875480
# Powerup Test Script: timestamp: 68875481
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 68875481
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 68875481
# Assigned value 1.0 to variable self.model.fan2FaultRead: timestamp: 68875481
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 68875481
# 
# Validation Timestamp: 68875529: timestamp: 68875529
# fan 1 should power on: timestamp: 68875529

def test1_test_test():
    """
     run r3 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 68876481: timestamp: 68876481
# fan 2 should not power on: timestamp: 68876481

def test2_test_test():
    """
     run r3 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 68876481
# 
# Validation Timestamp: 68876509: timestamp: 68876509
# only fan 1 is available: timestamp: 68876509

def test3_test_test():
    """
     run r3 test 3: Confirm self.model.eicas is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 68876509: timestamp: 68876509
# low fan speed: timestamp: 68876509

def test4_test_test():
    """
     run r3 test 4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r3: timestamp: 68876509
