# Get Script Variables: timestamp: 51603325
# generated script variable --> self.fan1_fault = True: timestamp: 51603340
# generated script variable --> self.fan2_fault = False: timestamp: 51603360
# generated script variable --> self.TEST_RUN = "r2": timestamp: 51603380
# generated script variable --> self.description = "Fan1 Fault Fan2 ok at startup mode": timestamp: 51603400
# Test Setup --> r2 Debug Level: 3: timestamp: 51603406
# Start Test --> : timestamp: 51603739
# Powerup Test Script: timestamp: 51603740
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 51603740
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 51603740
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 51603740
# 
# Validation Timestamp: 51603784: timestamp: 51603784
# fan 2 should power on: timestamp: 51603784

def test1_test_test():
    """
     run r2 test 1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# 
# Validation Timestamp: 51604740: timestamp: 51604740
# fan 1 should not power on: timestamp: 51604740

def test2_test_test():
    """
     run r2 test 2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# 
# Validation Timestamp: 51604740: timestamp: 51604740
# Fan 2 is available EICAS message: timestamp: 51604740

def test3_test_test():
    """
     run r2 test 3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r2: timestamp: 51604740
