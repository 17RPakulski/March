import serial
serialPort = serial.Serial(port = "COM3", baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

serialString = ""

while(1):
    fro = open('TempLight.txt', 'a+')
    if(serialPort.in_waiting > 0):
        serialString = serialPort.readline()
        print(serialString.decode('Ascii'))
        fro.write(serialString.decode('Ascii'))
        
    fro.close()