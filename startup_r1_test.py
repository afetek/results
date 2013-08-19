# #######################################################
# Test Name: STARTUP
# Requirements Under Test: 1,5,6,7,8
# Test Run: r1
# Description: Fans OK at startup
# #######################################################
# : timestamp: 5773170
# Start Test: : timestamp: 5773462
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 5773463
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 5773463
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 5773463
# 
# Validation Timestamp: 5773504: timestamp: 5773504
# fan 1 should power on: timestamp: 5773504

def r1_tc1_test():
    """
    STARTUP r1 tc1: Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 5774463: timestamp: 5774463
# fan 2 should not power on: timestamp: 5774463

def r1_tc2_test():
    """
    STARTUP r1 tc2: Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 5774463
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 5774463
# 
# Validation Timestamp: 5774505: timestamp: 5774505
# both fans are available: timestamp: 5774505

def r1_tc3_test():
    """
    STARTUP r1 tc3: Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 5774505: timestamp: 5774505
# low fan speed: timestamp: 5774505

def r1_tc4_test():
    """
    STARTUP r1 tc4: Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r1: timestamp: 5774505