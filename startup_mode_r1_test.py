# Get Script Variables: timestamp: 49430803
# generated script variable --> self.fan1_fault = False: timestamp: 49430818
# generated script variable --> self.fan2_fault = False: timestamp: 49430838
# generated script variable --> self.TEST_RUN = "r1": timestamp: 49430858
# generated script variable --> self.description = "Fan1 ok, Fan2 ok at startup mode test": timestamp: 49430878
# Test Setup --> r1 Debug Level: 3: timestamp: 49430884
# Start Test --> : timestamp: 49431115
# Powerup Test Script: timestamp: 49431116
# Testing Requirements: Statrup Mode - 5 through 8: timestamp: 49431116
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 49431116
# ----------------
# Validation Timestamp: 49431149: timestamp: 49431149
# fan 1 should power on: timestamp: 49431149

def test1_test_test():
    """
     run r1 test 1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    test_passed = True
    assert test_passed, "Failed test1_test"


# ----------------
# Validation Timestamp: 49432116: timestamp: 49432116
# fan 2 should not power on: timestamp: 49432116

def test2_test_test():
    """
     run r1 test 2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    test_passed = True
    assert test_passed, "Failed test2_test"


# ----------------
# Validation Timestamp: 49432116: timestamp: 49432116
# Both fans are Available EICAS message: timestamp: 49432116

def test3_test_test():
    """
     run r1 test 3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 4.0
    """

    test_passed = False
    assert test_passed, "Failed test3_test"


# Test Done --> r1: timestamp: 49432116
