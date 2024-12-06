from telethon.sync import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest

# Masukkan API ID dan API HASH Anda
API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'

# Login ke akun Telegram
with TelegramClient('session_name', API_ID, API_HASH) as client:
    print("Login berhasil! Memulai pencarian grup lama...")

    # Ambil semua dialog (chat, grup, channel)
    dialogs = client.get_dialogs()

    old_groups = []  # Untuk menyimpan grup lama

    # Filter hanya grup
    for dialog in dialogs:
        if dialog.is_group:
            created_time = dialog.date  # Waktu pertama kali bergabung/aktivitas grup
            old_groups.append((dialog.name, created_time, dialog.entity))

    # Sortir grup berdasarkan waktu bergabung (yang paling lama di atas)
    old_groups.sort(key=lambda x: x[1])

    # Tampilkan grup lama
    print("\nGrup yang ditemukan:")
    for i, group in enumerate(old_groups, start=1):
        print(f"{i}. Nama: {group[0]} | Tanggal: {group[1]}")

    # Konfirmasi untuk meninggalkan grup lama
    leave_groups = input("\nApakah Anda ingin meninggalkan semua grup lama ini? (y/n): ")
    if leave_groups.lower() == 'y':
        for group in old_groups:
            try:
                client(LeaveChannelRequest(group[2]))  # Keluar dari grup
                print(f"Berhasil keluar dari grup: {group[0]}")
            except Exception as e:
                print(f"Gagal keluar dari grup {group[0]}: {e}")
    else:
        print("Tidak ada grup yang dihapus.")