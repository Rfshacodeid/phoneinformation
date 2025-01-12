import phonenumbers
from phonenumbers import geocoder, timezone, carrier, number_type
import requests

def tipe_nomor(telepon):
    jenis = number_type(telepon)
    if jenis == phonenumbers.PhoneNumberType.MOBILE:
        return "Ponsel"
    elif jenis == phonenumbers.PhoneNumberType.FIXED_LINE:
        return "Telepon Rumah"
    elif jenis == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
        return "Telepon Rumah atau Ponsel"
    elif jenis == phonenumbers.PhoneNumberType.TOLL_FREE:
        return "Bebas Pulsa"
    elif jenis == phonenumbers.PhoneNumberType.PREMIUM_RATE:
        return "Premium Rate"
    elif jenis == phonenumbers.PhoneNumberType.VOIP:
        return "VOIP"
    elif jenis == phonenumbers.PhoneNumberType.PAGER:
        return "Pager"
    else:
        return "Tidak Diketahui"

def main():
    print("""
██╗  ██╗███████╗██╗   ██╗██╗      ██████╗ ███████╗███████╗██████╗ 
██║ ██╔╝██╔════╝██║   ██║██║     ██╔═══██╗██╔════╝██╔════╝██╔══██╗
█████╔╝ ███████╗██║   ██║██║     ██║   ██║███████╗█████╗  ██████╔╝
██╔═██╗ ╚════██║██║   ██║██║     ██║   ██║╚════██║██╔══╝  ██╔══██╗
██║  ██╗███████║╚██████╔╝███████╗╚██████╔╝███████║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
                                                                  
███████╗██╗  ██╗ █████╗ ██╗   ██╗███████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║  ██║██╔══██╗██║   ██║██╔════╝██║  ██║██╔════╝██╔══██╗
███████╗███████║███████║██║   ██║█████╗  ███████║█████╗  ██████╔╝
╚════██║██╔══██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██║██╔══╝  ██╔══██╗
███████║██║  ██║██║  ██║ ╚████╔╝ ███████╗██║  ██║███████╗██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
         BY Rafasha                    
    Selamat Datang di Alat Informasi Nomor Telepon!
    """)

    print("Silakan masukkan nomor telepon dengan kode negara (contoh: +628123456789).\n")
    try:
        # Meminta input dari pengguna
        nomor = input("Masukkan nomor telepon: ").strip()

        # Mem-parsing nomor telepon
        nomor_terparsing = phonenumbers.parse(nomor)

        # Memvalidasi nomor telepon
        if not phonenumbers.is_valid_number(nomor_terparsing):
            print("\nError: Nomor telepon yang dimasukkan tidak valid. Periksa kembali nomor tersebut dan coba lagi.")
            return

        # Menampilkan informasi
        print("\n-------------------------------------")
        print("          Nomor Telepon:", nomor)
        print("                Negara:", geocoder.description_for_number(nomor_terparsing, "id"))
        print("        Penyedia Layanan:", carrier.name_for_number(nomor_terparsing, "id"))
        print("           Zona Waktu:", ", ".join(timezone.time_zones_for_number(nomor_terparsing)))
        print("    Tipe Nomor Telepon:", tipe_nomor(nomor_terparsing))
        print(" Nomor Telepon Terparsing:", nomor_terparsing)
        print("       Apakah Valid:", phonenumbers.is_valid_number(nomor_terparsing))
        print("    Apakah Mungkin:", phonenumbers.is_possible_number(nomor_terparsing))
        print("-------------------------------------")

    except phonenumbers.NumberParseException as e:
        print(f"\nError: {e}\nPastikan nomor telepon menyertakan kode negara (contoh: +628123456789).")

if __name__ == "__main__":
    main()
