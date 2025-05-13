import requests

# Ganti dengan API key dan endpoint dari layanan pihak ketiga
API_URL = "https://api.thirdpartyservice.com/track"
API_KEY = "YOUR_THIRD_PARTY_API_KEY"

def track_phone_number(phone_number):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "phone_number": phone_number
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        if response.status_code == 200:
            location = response.json()
            print(f"Lokasi: {location}")
        else:
            print(f"Gagal melacak. Kode status: {response.status_code}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    phone_number = "Your phone number"  # Nomor telepon yang akan di pelacakan
    track_phone_number(phone_number)