def solve():
    alphabet = "qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM"
    target = "d9xJaU5YpMiK9t71WlG"
    
    decrypted_key = ""
    
    for i, char in enumerate(target):
        if char in alphabet:
            new_idx = alphabet.index(char)
            # 암호화: (old + i + 3) % 62 -> 복호화: (new - i - 3) % 62
            old_idx = (new_idx - i - 3) % 62
            decrypted_key += alphabet[old_idx]
        else:
            decrypted_key += char
            
    print(f"주황색 정답 키: {decrypted_key}")

solve()
