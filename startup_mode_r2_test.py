# Get Script Variables: timestamp: 49537988
# generated script variable --> self.fan1_fault = True: timestamp: 49538003
# generated script variable --> self.fan2_fault = False: timestamp: 49538023
# generated script variable --> self.TEST_RUN = "r2": timestamp: 49538043
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 49538063
# Test Setup --> r2 Debug Level: 3: timestamp: 49538069
# Start Test --> : timestamp: 49538378
# Powerup Test Script: timestamp: 49538379
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 49538379
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 49538379
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 49538379
# 
# Validation Timestamp: 49538405: timestamp: 49538405
# fan 2 should power on: timestamp: 49538405

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 49539379: timestamp: 49539379
# fan 1 should not power on: timestamp: 49539379

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 49539379: timestamp: 49539379
# Fan 2 is available EICAS message: timestamp: 49539379

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 49539379
