def kongruen_multiplikatif(seed, a, m, n):
    random_numbers = []
    current_seed = seed

    for _ in range(n):
        current_seed = (a * current_seed) % m
        random_number = current_seed / m  # Normalisasi ke rentang (0,1)
        random_numbers.append(random_number)

    return random_numbers

def main():
    # Parameter metode kongruen multiplikatif
    seed = int(input("Masukkan NPM sebagai seed (Z0): "))  # Gunakan NPM sebagai seed
    a = 16807
    m = 2147483647
    n = 100

    # Membangkitkan bilangan acak
    random_numbers = kongruen_multiplikatif(seed, a, m, n)

    # Menampilkan hasil dalam bentuk tabel
    print("Bilangan Acak (4 angka dibelakang koma):")
    print("------------------------------------")
    print("| No. | Bilangan Acak             |")
    print("------------------------------------")
    for i, num in enumerate(random_numbers, start=1):
        print(f"| {i:3d} | {num:.4f} |")
    print("------------------------------------")

if __name__ == "__main__":
    main()
