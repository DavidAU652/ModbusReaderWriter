from pymodbus.client.tcp import ModbusTcpClient  # Importowanie klienta Modbus TCP

print("This file is part of ModbusReaderWriter.")
print("ModbusReaderWriter  Copyright (C) 2024  Dawid")
print("This program comes with ABSOLUTELY NO WARRANTY")
print("This is free software, and you are welcome")
print("to redistribute it under certain conditions.")
print("")

# Ustawienia
IP_ADDRESS = input("IP adress: ")  # Adres IP ESP32
PORT = 502                     # Standardowy port Modbus TCP
REGISTER_START = int(input("Register Start: "))           # Adres początkowy rejestru
REGISTER_COUNT = int(input("Register Count: "))             # Liczba rejestrów do odczytania

# Tworzenie klienta Modbus
client = ModbusTcpClient(IP_ADDRESS, port=PORT)

# Połączenie z serwerem
connection = client.connect()

if connection:
    print("Connected to server")
    
    # Ustawienie jednostki
    client.unit_id = 1

    # Odczyt rejestrów
    try:
        result = client.read_holding_registers(REGISTER_START, REGISTER_COUNT)
        
        if result.isError():  # Sprawdzanie, czy wystąpił błąd podczas odczytu
            print(f"Error when reading: {result}")
        else:
            # Wyświetlanie wartości rejestrów
            for i, value in enumerate(result.registers):
                print(f"Register {REGISTER_START + i}: {value} (Hex: {hex(value)})")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Error connecting to server")

# Zamknięcie połączenia
client.close()
input("Press ENTER to exit.")
