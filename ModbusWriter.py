from pymodbus.client.tcp import ModbusTcpClient

print("This file is part of ModbusReaderWriter.")
print("ModbusReaderWriter  Copyright (C) 2024  Dawid")
print("This program comes with ABSOLUTELY NO WARRANTY")
print("This is free software, and you are welcome")
print("to redistribute it under certain conditions.")
print("")

# Ustawienia
IP = input("IP adress: ")
register = int(input("Register to write: "))
newValue = int(input("Int to write: "))

# Konfiguracja połączenia
client = ModbusTcpClient(IP, port=502)
client.connect()

# Zapis wartości do rejestru
result = client.write_register(register, newValue)

if result.isError():
    print("Error when writing to register")
else:
    print(f"Succesfuly writed {newValue} to register {register}")

# Zamknięcie połączenia
client.close()
input("Press ENTER to exit.")