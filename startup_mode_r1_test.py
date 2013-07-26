# #######################################################
# Test Name: Startup Mode
# Requirements Under Test: 1,5,6,7,8
# Test Run: r1
# Description: Fans OK at startup
# #######################################################
# : timestamp: 8639037
# Start Test: : timestamp: 8639168
# Assigned value 0.0 to variable self.model.fan1FaultRead: timestamp: 8639169
# Assigned value 0.0 to variable self.model.fan2FaultRead: timestamp: 8639169
# Assigned value 1.0 to variable self.model.powerECU: timestamp: 8639169
# 
# Validation Timestamp: 8639216: timestamp: 8639216
# fan 1 should power on: timestamp: 8639216

def r1_tc1_test():
    """
    Confirm self.model.fan1_power_enable is within 1.0 and 1.0: actual value is 1.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8640169: timestamp: 8640169
# fan 2 should not power on: timestamp: 8640169

def r1_tc2_test():
    """
    Confirm self.model.fan2_power_enable is NOT within 1.0 and 1.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Assigned value 3.0 to variable self.model.fan1_airflow_sensor_fb: timestamp: 8640169
# Assigned value 1.0 to variable self.model.fan1_power_status: timestamp: 8640169
# 
# Validation Timestamp: 8640206: timestamp: 8640206
# both fans are available: timestamp: 8640206

def r1_tc3_test():
    """
    Confirm self.model.eicas is within 3.0 and 3.0: actual value is 3.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# 
# Validation Timestamp: 8640206: timestamp: 8640206
# low fan speed: timestamp: 8640206

def r1_tc4_test():
    """
    Confirm self.model.fan1_high_low is within 0.0 and 0.0: actual value is 0.0
    """

    ##########################
    TEST_STATUS = '''PASSED'''
    ##########################

    assert TEST_STATUS == "PASSED", "*** TEST FAILED ***"


# Test Done --> r1: timestamp: 8640206
