# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r2
# Test Run Description: Fan1 Fault Fan2 ok at startup mode
# #######################################################
# : timestamp: 7978566
# Test Setup --> r2 Debug Level: 3: timestamp: 7978567
# Start Test --> : timestamp: 7978871
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 7978872
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 7978872
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 7978872
# 
# Validation Timestamp: 7978895: timestamp: 7978895
# fan 2 should power on: timestamp: 7978895

def r2_tc1_test():
    """
    Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7979872: timestamp: 7979872
# fan 1 should not power on: timestamp: 7979872

def r2_tc2_test():
    """
    Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 7979872
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 7979872
# 
# Validation Timestamp: 7979895: timestamp: 7979895
# only fan 2 is available: timestamp: 7979895

def r2_tc3_test():
    """
    Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 7979895: timestamp: 7979895
# low fan speed: timestamp: 7979895

def r2_tc4_test():
    """
    Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 7979895
