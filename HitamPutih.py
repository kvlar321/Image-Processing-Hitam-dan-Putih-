#mengambil fungsi library pillow
from PIL import Image

#mengambil gambar harus satu folder dengan program
citra = Image.open("gambar.jpg")
 
#merubah gambar ke mode L, yaitu hitam dan putih 
gray = citra.convert('L') 

#menampilkan gambar yang sudah di ubah menjadi hitam dan putih 
gray.show() 
