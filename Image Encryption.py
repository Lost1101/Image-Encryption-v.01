# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import tkinter as tk
from tkinter.filedialog import askopenfile

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

import os

#Membuat instance untuk frame tkinter
win = Tk()

#Menentukan Geometri untuk jendela aplikasi
win.geometry("800x600")
win.title("Image Encryption")

#global variable
path = ''
path_enc = ''
path_txt = ''

#FUNCTION
#Frame Enkripsi
def frame1():
    dekripsi_frame.forget()
    enkripsi_frame.pack(pady=5)

#Frame Dekripsi
def frame2():
    enkripsi_frame.forget()
    dekripsi_frame.pack(pady=5)

#Untuk mencari file image yang akan dienkripsi
def open_file_img():
    global path
    file = filedialog.askopenfile(mode='r', filetypes=[('Image Files', '*.png'),
                                                       ('Image Files', '*.jpg'),
                                                       ('Image Files', '*.jpeg')])
    if file:
        filepath = os.path.abspath(file.name)
        Label(enkripsi_frame, text="Filenya berlokasi di : " + str(filepath), font=('Aerial 11')).pack()
        path = (str(filepath))

#Untuk mencari file .enc yang akan didekripsi
def open_file_enc():
    global path_enc
    file = filedialog.askopenfile(mode='r', filetypes=[('Encryption file', '*.enc')])
    if file:
        filepath = os.path.abspath(file.name)
        Label(dekripsi_frame, text="Filenya berlokasi di : " + str(filepath), font=('Aerial 11')).pack()
        path_enc = (str(filepath))

#Code untuk mengenkripsi
def enc(alamat, nama, key):
    if nama.get() == '':
        messagebox.showwarning("Warning", "Nama untuk file .enc belum diisi!")
    else:
        #membaca file input yang akan di enkrip
        input_file = alamat
        with open(input_file, "rb") as f:
            data = f.read()

        # fungsi yang digunakan untuk mengenkrip data menggunakan AES-CBC
        def encrypt_data(msg: bytes, key: bytes):
            key = SHA256.new(key).digest()
            iv = os.urandom(AES.block_size)
            aes = AES.new(key, AES.MODE_CBC, iv)
            enc = aes.encrypt(pad(msg, AES.block_size))
            return iv + enc

        # fungsi untuk mengenkripsi data 2 stack dengan menggunakan key yang berbeda dan secara acak
        def double_encrypt(msg: bytes):
            keys = [os.urandom(32) for _ in range(2)]
            for key in keys:
                msg = encrypt_data(msg, key)
            return keys, msg

        # menuliskan hasil keluaran enkripsi pada nama file yang diinginkan dan lokasi yang diinginkan
        output = (nama.get() + '.enc')
        output_file = ('D:\Image Encryption\Hasil Enkripsi\{}'.format(output))
        keys, encrypted_data = double_encrypt(data)
        with open(output_file, "wb") as f:
            f.write(encrypted_data)

        # menyimpan kunci enkripsi di folder Key dan usahakan di sembunyikan (Admin only) setelah mengenkripsi
        nama_key = key.get() + '.txt'
        output_key_file = ('D:\Image Encryption\Key\{}'.format(nama_key))
        with open(output_key_file, "w") as f:
            f.write("{}\n".format(keys))
            messagebox.showinfo("Yeay!", "File berhasil dienkrip!")

#Code untuk mendekripsi
def dec(path, output):
    from key import keys
    if output.get() == '':
        messagebox.showwarning("Warning", "Nama untuk file output belum diisi!")
    else:
        # fungsi yang akan digunakan untuk mendekrip data menggunakan AES-CBC
        def decrypt_data(enc: bytes, key: bytes, iv: bytes):
            key = SHA256.new(key).digest()
            aes = AES.new(key, AES.MODE_CBC, iv)
            msg = aes.decrypt(enc)
            return unpad(msg, AES.block_size)

        # fungsi untuk melakukan dekrip berlapis sebanyak 2 stack dengan implementasi key berbeda
        def double_decrypt(enc: bytes, keys: list):
            keys = keys[::-1]
            for key in keys:
                iv, enc = enc[:AES.block_size], enc[AES.block_size:]
                key = key
                enc = decrypt_data(enc, key, iv)
            return enc

        # membaca isi file yang akan di dekrip valuenya
        input_file = (path)
        with open(input_file, "rb") as f:
            data = f.read()

        # mendeskripsikan hasil keluaran berupa nama file dan menampilkan hasil dekrip file
        output_file = output.get()  # usahakan samakan ekstensi dengan file awalnya
        decrypted_data = double_decrypt(data, keys)
        with open('D:\Image Encryption\Hasil Dekripsi\{}'.format(output_file), "wb") as f:
            f.write(decrypted_data)
        messagebox.showinfo("Ingfo", "File berhasil didekrip")


#INTERFACE
#Main Interface
parent =Frame(win)

main_label =Label(win, text="꒰⑅´˘`⑅꒱♡✩‧₊˚IMAGE ENCRYPTION˚₊‧✩♡꒰⑅´˘`⑅꒱", font=('Georgia 24')).pack(pady=5)
secondary_label =Label(win, text="Pilih yang ingin anda lakukan :").pack(pady=5)
var = IntVar()
parent.pack(pady=(0,10))

#Radiobutton untuk memilih apa yang ingin dilakukan
R1 = Radiobutton(parent, text="Enkripsi", variable=var, value=1, command=frame1).pack(side='left')
R2 = Radiobutton(parent, text="Dekripsi", variable=var, value=2, command=frame2).pack(side='left')

enkripsi_frame = Frame(win)
dekripsi_frame = Frame(win)

#INTERFACE ENKRIPSI
#Label judul
Label(enkripsi_frame, text="ENKRIPSI", font=('Georgia 16')).pack(pady=5)

#Widget
nama_enkripsi = StringVar()
nama_key = StringVar()
Label(enkripsi_frame, text="Klik tombol untuk mencari gambar yang ingin dienkripsi", font=('Georgia 13')).pack(pady=10)
Button(enkripsi_frame, text="Cari gambar", command=open_file_img).pack(pady=10)
Label(enkripsi_frame,text="Nama file enkripsi (.enc)").pack(pady=5)
Entry(enkripsi_frame, textvariable=nama_enkripsi).pack(pady=5)
Label(enkripsi_frame,text="Nama file key (.txt)").pack(pady=5)
Entry(enkripsi_frame, textvariable=nama_key).pack(pady=5)
Button(enkripsi_frame, text="Enkripsi!", command=lambda: enc(path, nama_enkripsi, nama_key)).pack(pady=10)

#INTERFACE DEKRIPSI
#Label judul
Label(dekripsi_frame, text="DEKRIPSI", font=('Georgia 16')).pack(pady=5)

#Widget
nama_dekripsi = StringVar()
Label(dekripsi_frame, text="Klik tombol untuk mencari file.enc yang akan didekripsi", font=('Georgia 13')).pack(pady=10)
Button(dekripsi_frame, text="Cari .enc", command=open_file_enc).pack(pady=10)
Label(dekripsi_frame,text="Nama file output/bentuk awal (.jpg,.png,.jpeg. Contoh: example.png)").pack(pady=5)
Entry(dekripsi_frame, textvariable=nama_dekripsi).pack(pady=5)
Label(dekripsi_frame, text="Key nya tolong masukkan di file bernama key.py", font=('Georgia 13')).pack(pady=10)
Button(dekripsi_frame, text="Dekripsi!", command=lambda: dec(path_enc, nama_dekripsi)).pack(pady=10)

win.mainloop()
