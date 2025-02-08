import re
import math
import getpass  

class RexzeaAdvancedPasswordStrengthChecker:
    def __init__(self):
        # kriteria kekuatan password
        self.min_length = 8
        self.max_length = 64
        
        # daftar password umum yang lemah
        self.common_passwords = [
            'password', '123456', 'qwerty', 'admin', 
            'welcome', 'letmein', 'login', 'abc123'
        ]
    
    def check_length(self, password):
        return len(password), len(password) >= self.min_length
    
    def check_complexity(self, password):
        complexity_checks = {
            'has_uppercase': bool(re.search(r'[A-Z]', password)),
            'has_lowercase': bool(re.search(r'[a-z]', password)),
            'has_digit': bool(re.search(r'\d', password)),
            'has_special_char': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
            'is_common_password': password.lower() in self.common_passwords
        }
        
        return complexity_checks
    
    def calculate_entropy(self, password):
        # menentukan character
        character_sets = {
            'lowercase': len(set(c for c in password if c.islower())),
            'uppercase': len(set(c for c in password if c.isupper())),
            'digits': len(set(c for c in password if c.isdigit())),
            'special': len(set(c for c in password if not c.isalnum()))
        }
        
        # hitung totsl set
        char_set_size = (
            26 if character_sets['lowercase'] > 0 else 0 +
            26 if character_sets['uppercase'] > 0 else 0 +
            10 if character_sets['digits'] > 0 else 0 +
            32 if character_sets['special'] > 0 else 0
        )
        
        # rumus entropi
        entropy = len(password) * math.log2(char_set_size) if char_set_size > 0 else 0
        return round(entropy, 2)
    
    def generate_detailed_feedback(self, password):
        # periksa panjang
        password_length, is_length_valid = self.check_length(password)
        
        # periksa kompleksitqs
        complexity = self.check_complexity(password)
        
        # mnghitung entropi
        entropy = self.calculate_entropy(password)
        
        # evaluasi kekuatan
        strength_score = sum([
            complexity['has_uppercase'],
            complexity['has_lowercase'], 
            complexity['has_digit'], 
            complexity['has_special_char']
        ])
        
        # tingkat kekuatan
        if not is_length_valid:
            strength = 'Sangat amat Lemah'
            recommendation = f'Password kamu terlalu pendek. Minimal {self.min_length} karakter.'
        elif complexity['is_common_password']:
            strength = 'Sangat Lemah'
            recommendation = 'Ini adalah password yang sangat umum. Hindari password yang mudah ditebak!'
        elif strength_score <= 1:
            strength = 'Sangat Lemah'
            recommendation = 'Gunakan kombinasi huruf besar, kecil, angka, dan simbol!.'
        elif strength_score == 2:
            strength = 'Lemah'
            recommendation = 'Password masih kurang kuat. coba kamu tambahkan variasi karakter agar lebih baik lagi.'
        elif strength_score == 3:
            strength = 'Cukup Kuat'
            recommendation = 'Password cukup baik, tetapi masih bisa ditingkatkan.'
        else:
            strength = 'Sangat Kuat'
            recommendation = 'Password kamu sangat kuat dan aman!'
        
        return {
            'password_length': password_length,
            'is_length_valid': is_length_valid,
            'complexity': complexity,
            'entropy': entropy,
            'strength': strength,
            'strength_score': strength_score,
            'recommendation': recommendation
        }
    
    def display_password_analysis(self, analysis):
        print("\n--- Analisis Keamanan Password ---")
        print(f"Panjang Password: {analysis['password_length']} karakter")
        print(f"Tingkat Kekuatan: {analysis['strength']}")
        print(f"Skor Kompleksitas: {analysis['strength_score']}/4")
        print(f"Entropi Password: {analysis['entropy']} bit")
        
        print("\n--- Pemeriksaan Kompleksitas ---")
        kompleksitas = analysis['complexity']
        print(f"Huruf Besar  : {'✓' if kompleksitas['has_uppercase'] else '✗'}")
        print(f"Huruf Kecil  : {'✓' if kompleksitas['has_lowercase'] else '✗'}")
        print(f"Angka        : {'✓' if kompleksitas['has_digit'] else '✗'}")
        print(f"Simbol Khusus: {'✓' if kompleksitas['has_special_char'] else '✗'}")
        print(f"Password Umum: {'✗' if not kompleksitas['is_common_password'] else '✓'}")
        
        print(f"\nRekomendasi  : {analysis['recommendation']}")

def main():
    checker = RexzeaAdvancedPasswordStrengthChecker()
    
    while True:
        print("\n--- Password Strength Checker ---")
        print("1. Periksa Kekuatan Password")
        print("2. Keluar")
        
        pilihan = input("Masukkan pilihan (1/2): ")
        
        if pilihan == '1':
            # input password yg tersembunyi
            password = getpass.getpass("Masukkan password kamu (akan disembunyikan): ")
            
            # menganalisis password
            result = checker.generate_detailed_feedback(password)
            checker.display_password_analysis(result)
        
        elif pilihan == '2':
            print("Terima kasih. Sampai jumpa lagi yaa :)")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi!.")

if __name__ == "__main__":
    main()
