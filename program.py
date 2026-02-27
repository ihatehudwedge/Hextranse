import struct
import base64

def read(path):
    with open(str(path), "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
        return content

def write(path, string):
    with open(str(path), "w", encoding="utf-8") as f:
        f.write(f"{string}")

def hex_2_string(hex_string):
    clean_hex = hex_string.replace(" ", "").replace("\n", "")
    data = bytes.fromhex(clean_hex)
    return data
    
def to_string(hex_string):
    data = hex_2_string(hex_string)
    print("--- [ String Interpretation ] ---")
    ascii_output = ""
    for b in data:
        if 32 <= b <= 126: # 출력 가능한 ASCII 범위
            ascii_output += chr(b)
        else:
            ascii_output += "."
    
    print(f"[ASCII View]:\n{ascii_output}\n")
    result = f"[ASCII View]\n{ascii_output}\n\n"

    try:
        korean_output = data.decode('cp949', errors='ignore')
        print(f"[CP949(Korean) Decoded]:\n{korean_output}\n")
        result = result + f"===================\n[CP949(Korean) Decoded]\n{korean_output}\n\n"
    except Exception as e:
        print(f"CP949(Korean) Error")

    try:
        korean_output = data.decode('utf-8', errors='ignore')
        print(f"[UTF-8 Decoded]:\n{korean_output}")
        result = result + f"===================\n[UTF-8 Decoded]\n{korean_output}\n\n"
    except Exception as e:
        print(f"UTF-8 Error")

    try:
        utf16_output = data.decode('utf-16', errors='ignore')
        print(f"[UTF-16 Decoded]:\n{utf16_output}")
        result = result + f"===================\n[UTF-16 Decoded]\n{utf16_output}\n\n"
    except Exception as e:
        print(f"UTF-16 Error")

    try:
        base64_decoded = base64.b64decode(data).decode('utf-8', errors='ignore')
        print(f"[Base64 Decoded]:\n{base64_decoded}")
        result = result + f"===================\n[Base64 Decoded]\n{base64_decoded}\n\n"
    except Exception as e:
        print(f"Base64 Error")

    try:
        latin_output = data.decode('latin-1', errors='ignore')
        print(f"[Latin-1 (Western European) Decoded]:\n{latin_output}")
        result = result + f"===================\n[Latin-1 (Western European) Decoded]\n{latin_output}\n\n"
    except Exception as e:
        print(f"Latin-1 Error")

    try:
        sjis_output = data.decode('shift_jis', errors='ignore')
        print(f"[Shift-JIS Decoded]:\n{sjis_output}")
        result = result + f"===================\n[Shift-JIS Decoded]\n{sjis_output}\n\n"
    except Exception as e:
        print(f"Shift-JIS Error")

    try:
        eucjp_output = data.decode('euc-jp', errors='ignore')
        print(f"[EUC-JP (Japanese Web) Decoded]:\n{eucjp_output}")
        result = result + f"===================\n[EUC-JP (Japanese Web) Decoded]\n{eucjp_output}\n\n"
    except Exception as e:
        print(f"EUC-JP Error")

    try:
        russian_output = data.decode('windows-1251', errors='ignore')
        print(f"[Windows-1251 (Russian) Decoded]:\n{russian_output}")
        result = result + f"===================\n[Windows-1251 (Russian) Decoded]\n{russian_output}\n\n"
    except Exception as e:
        print(f"Windows-1251 Error")

    try:
        chinese_output = data.decode('gbk', errors='ignore')
        print(f"[GBK (Chinese) Decoded]:\n{chinese_output}")
        result = result + f"===================\n[GBK (Chinese) Decoded]\n{chinese_output}\n\n"
    except Exception as e:
        print(f"GBK Error")

    try:
        big5_output = data.decode('big5', errors='ignore')
        print(f"[Big5 (Traditional Chinese) Decoded]:\n{big5_output}")
        result = result + f"===================\n[Big5 (Traditional Chinese) Decoded]\n{big5_output}\n\n"
    except Exception as e:
        print(f"Big5 Error")

    write("result.txt", result)

def analyze_hex(hex_string):
    data = hex_2_string(hex_string)
    
    print(f"--- [ 총 길이: {len(data)} bytes ] ---\n")

    print("--- [ DWORD View (Big Endian) ] ---")
    print("Offset   | Hex (DWORD) | Integer")
    print("-" * 35)
    
    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        
        if len(chunk) < 4:
            chunk = chunk.ljust(4, b'\x00')
            
        dword_val = struct.unpack('>I', chunk)[0]
        
        print(f"0x{i:04X}   | {dword_val:08X}    | {dword_val}")

    print("\n")


if __name__ == "__main__":
    hex_value = read("origin.txt")

    analyze_hex(hex_value)
    to_string(hex_value)