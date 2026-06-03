# 1. 드림이의 32글자 커스텀 키 (A=0, B=1, ... f=31)
custom_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef"

def dream_decode(cipher_text):
    # [1단계] 뒤에 붙은 패딩(=)을 제거합니다. (비트 연산에는 방해가 되므로)
    cipher_text = cipher_text.replace("=", "")
    
    # [2단계] 암호문 문자들을 5비트 이진수로 풀어서 길게 이어붙입니다.
    binary_stream = ""
    for char in cipher_text:
        # 문자가 드림이 표에서 몇 번째 인덱스인지 찾습니다. (예: 'I' -> 8)
        index = custom_table.index(char)
        # 그 인덱스(숫자)를 '5자리짜리 이진수' 문자열로 바꿉니다. (예: 8 -> '01000')
        five_bits = f"{index:05b}"
        binary_stream += five_bits

    # [3단계] 이어붙인 이진수 스트림을 이번엔 '8비트(1바이트)'씩 뚝뚝 끊어줍니다.
    decoded_bytes = bytearray()
    for i in range(0, len(binary_stream), 8):
        eight_bits = binary_stream[i:i+8]
        
        # 만약 마지막 덩어리가 8비트가 안 채워지면 (인코딩 때 버림처리/패딩된 부분) 버립니다.
        if len(eight_bits) < 8:
            break
            
        # 8비트 이진수를 10진수 숫자로 바꿉니다. (예: '01000100' -> 68)
        byte_value = int(eight_bits, 2)
        # 바이트 배열에 차곡차곡 추가합니다.
        decoded_bytes.append(byte_value)
        
    # [4단계] 바이트 배열을 우리가 읽을 수 있는 글자(UTF-8)로 변환합니다.
    return decoded_bytes.decode('utf-8')

# 실제 문제의 암호문 입력
cipher = "IREHWYJZMEcGCODGMMbTENDDGcbGEMJZGEbGEZTFGYaGKNRTMIcGIMBSGRQTSNDDGAaWGYZRHEbGCNRQMUaDOMbEMRTGEYJYGUaWGOJQMYZHa==="

# 실행 및 출력
flag = dream_decode(cipher)
print("찾아낸 진짜 플래그:", flag)
