import re
import requests
from urllib.parse import urlparse
from typing import Dict, List, Tuple
import json
from datetime import datetime, timedelta

class PhishingDetector:
    
    def __init__(self):
        self.suspicious_words = [
            'verifikasi', 'konfirmasi', 'akun diblokir', 'segera', 'darurat',
            'kata sandi', 'password', 'credit card', 'kartu kredit', 'login',
            'bank', 'verify', 'urgent', 'suspended', 'blocked'
        ]
        
        self.phishing_db = set()
        self.last_db_update = None
        
        self.url_length_threshold = 75
        self.update_phishing_database()

    def update_phishing_database(self) -> None:
        if (self.last_db_update is None or 
            datetime.now() - self.last_db_update > timedelta(days=1)):
            try:
                # Note: Dalam implementasi nyata, Anda perlu mendaftar untuk API key
                # dan menggunakan endpoint yang sesuai
                response = requests.get(
                    "https://openphish.com/feed.txt", 
                    timeout=5
                )
                if response.status_code == 200:
                    self.phishing_db = set(response.text.split('\n'))
                    self.last_db_update = datetime.now()
            except Exception as e:
                print(f"Gagal mengupdate database: {str(e)}")

    def analyze_url(self, url: str) -> Dict[str, any]:
        results = {
            'suspicious_patterns': [],
            'risk_factors': [],
            'score': 0
        }
        
        if len(url) > self.url_length_threshold:
            results['risk_factors'].append('URL terlalu panjang')
            results['score'] += 1
        
        if not url.startswith('https://'):
            results['risk_factors'].append('Tidak menggunakan HTTPS')
            results['score'] += 2
        
        suspicious_chars = re.findall(r'[@%]', url)
        if suspicious_chars:
            results['risk_factors'].append(
                f'Mengandung karakter mencurigakan: {suspicious_chars}'
            )
            results['score'] += len(suspicious_chars)
        
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        
        if domain.count('.') > 2:
            results['risk_factors'].append('Terlalu banyak subdomain')
            results['score'] += 1
        
        if url in self.phishing_db:
            results['risk_factors'].append('URL terdaftar dalam database phishing')
            results['score'] += 5
        
        return results

    def analyze_content(self, text: str) -> Dict[str, any]:

        results = {
            'suspicious_words': [],
            'risk_factors': [],
            'score': 0
        }
        
        for word in self.suspicious_words:
            if re.search(word, text.lower()):
                results['suspicious_words'].append(word)
                results['score'] += 1
        
        if re.search(r'\b\d{16}\b', text): 
            results['risk_factors'].append('Meminta nomor kartu kredit')
            results['score'] += 2
            
        if re.search(r'\bpassword\b|\bkata\s+sandi\b', text.lower()):
            results['risk_factors'].append('Meminta kata sandi')
            results['score'] += 2
            
        urgency_words = ['segera', 'urgent', 'darurat', 'immediately']
        if any(word in text.lower() for word in urgency_words):
            results['risk_factors'].append('Mengandung kata-kata urgensi')
            results['score'] += 1
        
        return results

    def get_risk_level(self, score: int) -> str:
 
        if score <= 2:
            return "Rendah"
        elif score <= 5:
            return "Sedang"
        else:
            return "Tinggi"

    def analyze(self, url: str = None, content: str = None) -> Dict[str, any]:

        results = {
            'timestamp': datetime.now().isoformat(),
            'total_score': 0,
            'risk_level': 'Rendah',
            'url_analysis': None,
            'content_analysis': None
        }
        
        if url:
            results['url_analysis'] = self.analyze_url(url)
            results['total_score'] += results['url_analysis']['score']
            
        if content:
            results['content_analysis'] = self.analyze_content(content)
            results['total_score'] += results['content_analysis']['score']
            
        results['risk_level'] = self.get_risk_level(results['total_score'])
        
        return results

if __name__ == "__main__":
    detector = PhishingDetector()
    
    test_url = "http://127.0.0.1:5504/flappybird/index.html"
    url_result = detector.analyze(url=test_url)
    print("\nAnalisis URL:")
    print(json.dumps(url_result, indent=2, ensure_ascii=False))
    
    # Contoh analisis konten email
    test_content = """
    PENTING! Akun anda akan diblokir!
    Silakan verifikasi akun anda segera dengan mengklik link berikut
    dan masukkan nomor kartu kredit anda untuk verifikasi:
    http://suspicious-bank.com/verify
    """
    content_result = detector.analyze(content=test_content)
    print("\nAnalisis Konten Email:")
    print(json.dumps(content_result, indent=2, ensure_ascii=False))