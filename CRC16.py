data = [0x01, 0x03, 0x00, 0x00, 0x00, 0x13]


'''''''''''
Function: getCRC()
input: int[] (like: [0x01, 0x03, 0x00, 0x00, 0x00, 0x02])
output: 2 integers (196, 11, 0 <= int < 256)
purpose: calculate the CRC-16 ModBus value of input 
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
    
    output = ""                # this would feed back the CRC code in string 
    output += outputRaw[2]
    output += outputRaw[3]
    output += outputRaw[0]
    output += outputRaw[1]
    print(output)

    return int(output1,16),int(output2,16)


'''''''''''
Function: hexToString()
input: int[] (like: [0x01, 0x03, 0x00, 0x00, 0x00, 0x02])
output: chr[] (like: ['\x01', '\x03', '\x00', '\x00', '\x00', '\x02', 'Ä', '\x0b'])
purpose: calculate the string conversion of hex input, as the serial API provided by Python can only 
    send/receive string type
'''''''''''
def hexToString(data):
    
    chrList = []
    temp = 0
    for i in range(len(data)):
        temp = data[i]
        chrList.append(chr(temp))
    del temp
    return chrList


'''''''''''
Function: stringToHex()
input: chr[] (like: ['\x01', '\x03', '\x00', '\x00', '\x00', '\x02', 'Ä', '\x0b'])
output: int[] (like: [0x01, 0x03, 0x00, 0x00, 0x00, 0x02])
purpose: calculate the hex conversion of string feedback, as the serial API provided by Python can only 
    send/receive string type
'''''''''''
def stringToHex(chrList):
    
    data = []
    temp = 0
    for i in range(len(chrList)):
        temp = ord(chrList[i])
        data.append(temp)
    del temp
    return data

data += getCRC(data)
print(data)

chrList = hexToString(data)
print(chrList)

'''
stringSend = ""
for i in chrList:
    stringSend += i
print(stringSend)
'''

data = stringToHex(chrList)
print(data)

