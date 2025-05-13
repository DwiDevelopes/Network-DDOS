import requests
import time

# Ganti dengan API key Anda dari Google Cloud Console
API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'

def get_location(phone_number):
    # Ini hanya contoh, Google Maps API tidak mendukung pelacakan langsung via nomor telepon.
    # Anda perlu menggunakan layanan lain atau mengintegrasikan dengan perangkat yang terhubung ke akun Google.
    print("Google Maps API tidak mendukung pelacakan langsung via nomor telepon.")
    print("Anda dapat menggunakan layanan lain atau mengintegrasikan dengan perangkat yang terhubung ke akun Google.")

def track_device(device_id):
    # Endpoint untuk melacak perangkat yang terhubung ke akun Google
    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}"
    
    # Data yang dikirim ke API (contoh: WiFi access points atau cell towers)
    data = {
        "considerIp": "true",  # Gunakan alamat IP untuk estimasi lokasi
        "wifiAccessPoints": [],  # Anda bisa menambahkan info WiFi access points jika ada
        "cellTowers": []  # Anda bisa menambahkan info cell towers jika ada
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            location = response.json()
            latitude = location['location']['lat']
            longitude = location['location']['lng']
            accuracy = location['accuracy']
            print(f"Lokasi perangkat: Latitude = {latitude}, Longitude = {longitude}")
            print(f"Akurasi: {accuracy} meter")
        else:
            print(f"Gagal melacak perangkat. Kode status: {response.status_code}")
            print(response.json())
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    # Contoh penggunaan
    phone_number = "Your phone number"  # Nomor telepon yang akan di pelacakan
    
    # Menggunakan nomor telepon sebagai ID perangkat
    device_id = phone_number
    
    # Menggunakan ID perangkat yang dihasilkan oleh aplikasi
    device_id = "Your device ID"
    
    print("Melacak lokasi perangkat...")
    track_device(device_id)
    time.sleep(5)  # Tunggu 5 detik
    print("Menghentikan lokasi perangkat...")