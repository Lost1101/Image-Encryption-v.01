<h1 align="center">꒰⑅´˘`⑅꒱♡✩‧₊˚IMAGE ENCRYPTION˚₊‧✩♡꒰⑅´˘`⑅꒱"</h1>
<p align="center">
  <img src="https://github.com/Lost1101/Image-Encryption-v.01/assets/114213500/b272deb7-b908-4f89-9161-0ac7c8db8a33" />
</p>

Using python language to encrypt data. The algorithm that we implemented in this project is AES (Advance Encryption Standard) using CBC Mode. We Do Double Encryption of which data will be encrypted on the data so that we get a more secure type of data. We are very happy that someone will make some improvements or use the main logic of our code >.&lt;

# 📝 NOTES:

1. File formats supported are only .png, .jpg and .jpeg image extensions.
2. Encryption, decryption and key results are saved in the specified default folder.
3. The key must be well hidden so that others cannot decipher it
4. The program can only process one image/file.enc at a time. So if you want to encode different images you have to change the source image periodically

# 🔌 SETUP
1. Of course, you should clone this repo
```
git clone https://github.com/Lost1101/Image-Encryption-v.01.git
```
2. Open editor that can open python file
3. You should change the location in 'Image Encryption.py' file, depend of where you want to put the result
4. Recommend to make separated folder for each result
5. Before you running it, make sure the library (pycrypto & tkinter) installed
```
pip install pycryptodome
pip install tkinter
```
7. Run the program with this command (the cli should inside the folder where 'Image Encryption.py' placed
```
python 'Image Encryption.py'
```
# 💡 STEP

Encryption step:

1. Press the button to search for images
2. Enter the name of the .enc file.
3. Enter the name of the key TXT file
4. If yes, click Encrypt. encrypt
5. The .enc file will be saved in the Encryption Result folder and the key will be saved in the Key folder.

Step description:

1. Find the desired .enc file and restore the original image
2. Enter a name for the decrypted result (e.g. = "hasil.jpg") and make sure the file extension is the same as the original file (e.g. if original = .jpg then decrypt The resulting extension must also be .jpg). . )
3. Enter the hidden key in key.py (Keys variable).
4. Press "Decryption!!" when done.
5. The image is saved in the "decryption result" folder

# ✨ REMARKS
The program is still in development, so all kinds of changes, optimizations and fixes are expected
If you have any suggestions or comments, please express them in a more modern code format.

thank you for using. Enjoy our program~

# MAKE WITH ✨ FROM Group 33

 # 🤓 Group 33 fellas :
  <a href = "https://github.com/Lost1101">
  <img src = "https://avatars.githubusercontent.com/u/114213500?v=4" width="100" height="auto" style="border-radius:50%"/>
</a>
 <a href = "https://github.com/RyZal25">
  <img src = "https://avatars.githubusercontent.com/u/118142575?v=4"  width="100" height="auto" style="border-radius:50%"/>
</a>
 <a href = "https://github.com/revlizn">
  <img src = "https://avatars.githubusercontent.com/u/114213552?v=4"  width="100" height="auto" style="border-radius:50%"/>
</a>
