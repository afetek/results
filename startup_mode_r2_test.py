# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r2
# Test Run Description: Fan1 faulted at startup
# #######################################################
# : timestamp: 11588293
# Start Test: : timestamp: 11588524
# Assigned value 1.0 to variable self.model.fan1FaultRead: timestamp: 11588525
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 11588525
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 11588525
# 
# Validation Timestamp: 11588561: timestamp: 11588561
# fan 2 should power on: timestamp: 11588561

def r2_tc1_test():
    """
    r2_tc1: Confirm self.model.fan2_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 11589525: timestamp: 11589525
# fan 1 should not power on: timestamp: 11589525

def r2_tc2_test():
    """
    r2_tc2: Confirm self.model.fan1_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan2_airflow_sensor_fb: timestamp: 11589525
# Assigned value 1.0 to variable self.model.fan2_power_status: timestamp: 11589525
# 
# Validation Timestamp: 11589540: timestamp: 11589540
# only fan 2 is available: timestamp: 11589540

def r2_tc3_test():
    """
    r2_tc3: Confirm self.model.eicas is within 2.0 and 2.0: actual value is 2.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 11589540: timestamp: 11589540
# low fan speed: timestamp: 11589540

def r2_tc4_test():
    """
    r2_tc4: Confirm self.model.fan2_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r2: timestamp: 11589540
