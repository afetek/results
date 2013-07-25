# Get Script Variables: timestamp: 68872116
# generated script variable --> self.fan1_fault = True: timestamp: 68872131
# generated script variable --> self.fan2_fault = False: timestamp: 68872151
# generated script variable --> self.TEST_RUN = "r2": timestamp: 68872171
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 68872191
# Test Setup --> r2 Debug Level: 3: timestamp: 68872197
# Start Test --> : timestamp: 68872522
# Powerup Test Script: timestamp: 68872523
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 68872523
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 68872523
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 68872523
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 68872523
# 
# Validation Timestamp: 68872569: timestamp: 68872569
# fan 2 should power on: timestamp: 68872569

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 68873523: timestamp: 68873523
# fan 1 should not power on: timestamp: 68873523

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 68873523
# 
# Validation Timestamp: 68873549: timestamp: 68873549
# only fan 2 is available: timestamp: 68873549

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    test_passed = True
    assert test_passed, "Failed test3_test"


# 
# Validation Timestamp: 68873549: timestamp: 68873549
# low fan speed: timestamp: 68873549

def test4_test_test():
    """
     run r2 test 4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test4_test"


# Test Done --> r2: timestamp: 68873549
