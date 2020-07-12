#!/usr/bin/python
import serial
import time
ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)  # check if there exists the file to confirm if connection is maintained

'''''''''''
Function: paraQuerySingle()
output: a list which has 12 variables, containing all the results
        result[0]: humidity 0.1%RH
        result[1]: temparature 0.1°C
        result[2]: soil humidity 0.1%RH
        result[3]: soil temparature 0.1°C
        result[4]: PM2.5 lug/m3
        result[5]: CO2 1ppm
        result[6]: gas 1ppm ???(written on the document)
        result[7]: brightness highest 1Lux
        result[8]: brightness lowest 1Lux
        result[9]: PM10 1ug/m3
        result[10]: atmospheric pressure highest 0.01kpa
        result[11]: atmospheric pressure lowest 0.01kpa
        result[12]: noise 0.1dba
purpose: check all the variables
attention:  according to obervation until now, the 3 4 6 7 8 variable always shows zero(fail to get data),
    may due to not connecting with detector probe (which is impossible to implement up to now)
'''''''''''
def paraQueryAll():
    send = [0x01, 0x03, 0x00, 0x00, 0x00, 0x0c]   # the structure of sending list
    
    send += getCRC(send)
    print('send signal to serial port: ',send)
    
    receive = list()
    flag = 0
    while(1==1):
        receive = [-1]
        while (receive == [-1]):
            signalSend(send,ser)
            
            receive = signalReceive(ser)     # receive a list of single bytes, receive = -1 means receives no signal
            print('receive signal from serial port: ',receive)
        
        for j in range(24):              # when all the feedback variables are zero, it is almost impossible that the result is right
            if (receive[3+j] != 0):
                flag = 1
                break
        if (flag == 1):
            break
    
    temp = [0]
    result = list()
    for i in range(12):
        temp[0] = receive[2*i+3]*16 + receive[2*i+4]
        result = result + temp
    return result

'''''''''''
Function: paraQuerySingle()
input: a number ranging from 0x00 to 0x0c
output: single integer
purpose: check the variables individially
    for the fourth variable in the list:
        0x00: humidity 0.1%RH
        0x01: temparature 0.1°C
        0x02: soil humidity 0.1%RH
        0x03: soil temparature 0.1°C
        0x04: PM2.5 lug/m3
        0x05: CO2 1ppm
        0x06: gas 1ppm ???(written on the document)
        0x07: brightness highest 1Lux
        0x08: brightness lowest 1Lux
        0x09: PM10 1ug/m3
        0x0a: atmospheric pressure highest 0.01kpa
        0x0a: atmospheric pressure lowest 0.01kpa
        0x0a: noise 0.1dba
'''''''''''
def paraQuerySingle(para):
    send = [0x01, 0x03, 0x00, 0x00, 0x00, 0x01]   # the structure of sending list 
    send[3] = para
    
    send += getCRC(send)
    print('send signal to serial port: ',send)
    
    receive = list()
    result = 0
    for i in range(20):
        receive = [-1]
        while (receive == [-1]):
            signalSend(send,ser)
            
            receive = signalReceive(ser)    # receive = -1 means receives no signal
            print('receive signal from serial port: ',receive)
        
        result = 16*receive[3] + receive[4]
        if (result != 0):          # reporting zero is very likely to be wrong, need to check
            break
    return result

'''''''''''
Function: getCRC()
input: int[] (like: [0x01, 0x03, 0x00, 0x00, 0x00, 0x02])
output: 2 integers (196, 11, 0 <= int < 256)
purpose: calculate the CRC-16 ModBus value of input list
'''''''''''
def getCRC(data):
    crc = 0xFFFF
    poly = 0xA001

    for j in data:   # I DO NOT KNOW WHY THE BULLSHIT FUNCTION, IT JUST WORKS
                     # code simulated from C++ code from internet 
        crc = crc^j
        for i in range(8):
            temp = crc//2
            if (crc == 2*temp):
                crc = temp
            else:
                crc = temp
                crc = crc^poly

    crcs = hex(crc)
    outputRaw = ""
    output1 = ""
    output2 = ""

    del crc, poly

    for i in range(6 - len(crcs)):
        outputRaw += "0"
    for i in range(2,len(crcs)):
        outputRaw += crcs[i]

    output1 += outputRaw[2]
    output1 += outputRaw[3]
    output2 += outputRaw[0]
    output2 += outputRaw[1]
    
    '''
    output = ""                # this would feed back the CRC code in string 
    output1 += outputRaw[2]
    output1 += outputRaw[3]
    output2 += outputRaw[0]
    output2 += outputRaw[1]
    print(output)
    '''

    return int(output1,16),int(output2,16)


'''''''''''
Function: signalSend()
input: int[] (like: [0x01, 0x03, 0x00, 0x00, 0x00, 0x02]), serial port
purpose: calculate the string conversion of hex input, as the serial API provided by Python can only 
    send/receive string type
'''''''''''
def signalSend(data,ser):
    
    packet = bytearray()
    for i in data:
        packet.append(i)
    ser.write(packet)


'''''''''''
Function: signalReceive()
input: serial port
output: int[] (like: [0x01, 0x03, 0x00, 0x00, 0x00, 0x02])
purpose: calculate the hex conversion of string feedback, as the serial API provided by Python can only 
    send/receive string type
attention: return [-1] if the serial port fail to receive signal
'''''''''''
def signalReceive(ser):
    
    time.sleep(1)
    byteList = ser.read(30)
    #print('receive signal from serial port: ',byteList)
    if (len(byteList) == 0): #check if serial port fail to return signal
        return [-1]
    length = byteList[2]
    feedback = list()
    for i in range(length + 5):
        feedback.append(byteList[i])
    check = feedback[:-2]       # CRC-16 check
    check += getCRC(check)
    if (check == feedback):
        return feedback
    else:
        return [-1]

#ddd = paraQuerySingle(0x00)
#ddd = paraQueryAll()
#print('ddd is: ',ddd)