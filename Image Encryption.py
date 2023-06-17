#IMPORTANT!!!!!!!
#If you want the result file is organized, better place them in separated folder
#you can set up the folder location below (marked with ☆☆☆)


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

#Create instance for the tkinter frame
win = Tk()

#Geometry spec for the application window
win.geometry("800x600")
win.title("Image Encryption")

#global variable
path = ''
path_enc = ''
path_txt = ''

#FUNCTION
#Encryption Frame 
def frame1():
    decrypt_frame.forget()
    encrypt_frame.pack(pady=5)

#Decryption Frame 
def frame2():
    encrypt_frame.forget()
    decrypt_frame.pack(pady=5)

#To find the image file to be encrypted
def open_file_img():
    global path
    file = filedialog.askopenfile(mode='r', filetypes=[('Image Files', '*.png'),
                                                       ('Image Files', '*.jpg'),
                                                       ('Image Files', '*.jpeg')])
    if file:
        filepath = os.path.abspath(file.name)
        Label(encrypt_frame, text="The file is located at : " + str(filepath), font=('Aerial 11')).pack()
        path = (str(filepath))

#To find the .enc file to decrypt
def open_file_enc():
    global path_enc
    file = filedialog.askopenfile(mode='r', filetypes=[('Encryption file', '*.enc')])
    if file:
        filepath = os.path.abspath(file.name)
        Label(decrypt_frame, text="The file is located at : " + str(filepath), font=('Aerial 11')).pack()
        path_enc = (str(filepath))

#Code to encrypt
def enc(alamat, nama, key):
    if nama.get() == '':
        messagebox.showwarning("Warning", "The name for the .enc file is missing!")
    else:
        #reads the input file to be encrypted
        input_file = alamat
        with open(input_file, "rb") as f:
            data = f.read()

        # function used to encrypt data using AES-CBC
        def encrypt_data(msg: bytes, key: bytes):
            key = SHA256.new(key).digest()
            iv = os.urandom(AES.block_size)
            aes = AES.new(key, AES.MODE_CBC, iv)
            enc = aes.encrypt(pad(msg, AES.block_size))
            return iv + enc

        # function to encrypt 2 stacks of data using different and random keys
        def double_encrypt(msg: bytes):
            keys = [os.urandom(32) for _ in range(2)]
            for key in keys:
                msg = encrypt_data(msg, key)
            return keys, msg

        # write the output of the encryption in the desired file name and desired location
        output = (nama.get() + '.enc')
        output_file = ('YOUR PATH STORAGE\image_encryption\Encryption Result\{}'.format(output)) #☆☆☆
        keys, encrypted_data = double_encrypt(data)
        with open(output_file, "wb") as f:
            f.write(encrypted_data)

        # save the encryption key in the Key folder and try to hide it (Admin only) after encrypting
        key_name = key.get() + '.txt'
        output_key_file = ('YOUR PATH STORAGE\image_encryption\Key\{}'.format(key_name)) #☆☆☆
        with open(output_key_file, "w") as f:
            f.write("{}\n".format(keys))
            messagebox.showinfo("Yeay!", "File encrypted successfully!")

#Code to decrypt
def dec(path, output):
    from key import keys
    if output.get() == '':
        messagebox.showwarning("Warning", "The name for the output file is missing!")
    else:
        # function that will be used to decrypt data using AES-CBC
        def decrypt_data(enc: bytes, key: bytes, iv: bytes):
            key = SHA256.new(key).digest()
            aes = AES.new(key, AES.MODE_CBC, iv)
            msg = aes.decrypt(enc)
            return unpad(msg, AES.block_size)

        # function to perform layered decryption of 2 stacks with different key implementations
        def double_decrypt(enc: bytes, keys: list):
            keys = keys[::-1]
            for key in keys:
                iv, enc = enc[:AES.block_size], enc[AES.block_size:]
                key = key
                enc = decrypt_data(enc, key, iv)
            return enc

        # read the contents of the file that will decrypt the value
        input_file = (path)
        with open(input_file, "rb") as f:
            data = f.read()

        # describes the output in the form of a file name and displays the results of the file decryption
        output_file = output.get()  # try to match the extension with the initial file
        decrypted_data = double_decrypt(data, keys)
        with open('YOUR PATH STORAGE\image_encryption\Encryption Result\{}'.format(output_file), "wb") as f: #☆☆☆
            f.write(decrypted_data)
        messagebox.showinfo("Yeay!", "File successfully decrypted!")


#INTERFACE
#Main Interface
parent =Frame(win)

main_label =Label(win, text="꒰⑅´˘`⑅꒱♡✩‧₊˚IMAGE ENCRYPTION˚₊‧✩♡꒰⑅´˘`⑅꒱", font=('Georgia 24')).pack(pady=5)
secondary_label =Label(win, text="Choose what you want to do :").pack(pady=5)
var = IntVar()
parent.pack(pady=(0,10))

#Radiobutton to choose what to do
R1 = Radiobutton(parent, text="Encryption", variable=var, value=1, command=frame1).pack(side='left')
R2 = Radiobutton(parent, text="Decryption", variable=var, value=2, command=frame2).pack(side='left')

encrypt_frame = Frame(win)
decrypt_frame = Frame(win)

#ENCRYPTION INTERFACE 
#Title tag
Label(encrypt_frame, text="ENCRYPTION", font=('Georgia 16')).pack(pady=5)

#Widget
encrypt_name = StringVar()
key_name = StringVar()
Label(encrypt_frame, text="Click the button to find the image you want to encrypt", font=('Georgia 13')).pack(pady=10)
Button(encrypt_frame, text="Search images", command=open_file_img).pack(pady=10)
Label(encrypt_frame,text="Encryption file name (.enc)").pack(pady=5)
Entry(encrypt_frame, textvariable=encrypt_name).pack(pady=5)
Label(encrypt_frame,text="Key file name (.txt)").pack(pady=5)
Entry(encrypt_frame, textvariable=key_name).pack(pady=5)
Button(encrypt_frame, text="Encrypt!", command=lambda: enc(path, encrypt_name, key_name)).pack(pady=10)

#DECRYPTION INTERFACE 
#Title tag
Label(decrypt_frame, text="DECRYPTION", font=('Georgia 16')).pack(pady=5)

#Widget
decrypt_name = StringVar()
Label(decrypt_frame, text="Click the button to locate the.enc file to decrypt", font=('Georgia 13')).pack(pady=10)
Button(decrypt_frame, text="Search for .enc", command=open_file_enc).pack(pady=10)
Label(decrypt_frame,text="Output file name/original form (.jpg,.png,.jpeg. Example: example.png)").pack(pady=5)
Entry(decrypt_frame, textvariable=decrypt_name).pack(pady=5)
Label(decrypt_frame, text="Please enter the key in a file called key.py", font=('Georgia 13')).pack(pady=10)
Button(decrypt_frame, text="Decrypt!", command=lambda: dec(path_enc, decrypt_name)).pack(pady=10)

win.mainloop()
