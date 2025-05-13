import time
import random
import folium

def get_gps_coordinates():
    # Simulasi pembacaan data GPS dari perangkat target
    latitude = -6.178306  # Gambar lokasi di daerah Jakarta
    longitude = 106.631889  # Gambar lokasi di daerah Jakarta
    
    # Menambahkan peluru untuk mendapatkan data GPS secara acak
    # Jika data GPS tidak tersedia, maka akan menghasilkan data acak
    latitude += random.uniform(-0.001, 0.001)
    longitude += random.uniform(-0.001, 0.001)
    
    return latitude, longitude

def track_location(phone_number):
    # Simulasi pelacakan lokasi dengan data GPS
    print(f"Melacak lokasi untuk nomor telepon: {phone_number}...")
    try:
            while True:
                latitude, longitude = get_gps_coordinates()
                print(f"Lokasi terdeteksi: Latitude = {latitude}, Longitude = {longitude}")
                
                # Membuat peta dengan lokasi terdeteksi
                m = folium.Map(location=[latitude, longitude], zoom_start=15)
                folium.Marker([latitude, longitude], popup="Lokasi Terdeteksi").add_to(m)
                
                # Menyimpan peta ke file HTML
                m.save("location_map.html")
                print("Peta lokasi telah disimpan sebagai 'location_map.html'. Buka file ini di browser untuk melihat lokasi.")
                time.sleep(10)  # Tunggu 10 detik
    except KeyboardInterrupt:
            print("Pelacakan dihentikan oleh pengguna.")

if __name__ == "__main__":
    phone_number = "+6289652969323"  # Nomor telepon yang akan di pelacakan
    track_location(phone_number)