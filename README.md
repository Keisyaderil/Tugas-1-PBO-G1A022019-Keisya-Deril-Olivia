# 1. Buatlah perbedaan functional programming dan object oriented programming dalam bahasa pemrograman pyhon, serta berikan contoh masing-masing code nya
  # Functional Programming
  Functional programming adalah komputasi pada program dengan menggunakan ekspresi dan evaluasi-sering kali dienkapsulasi dalam definisi fungsi. fuctional programming memodelkan masalah komputasi sebagai suatu fungsi matematika,yang mempunyai input (domain) dan hasil atau output (range). pemrograman ini tidak menekankan atau menghindari kerumitan perubahan status dan objek yang dapat terjadi melainkan senderung membuat program lebih ringkas dan ekspresif.
  # OOP
  Pemrograman berorientasi objek atau object-oriented programming merupakan suatu pendekatan pemrograman yang menggunakan object dan class.OOP (Object Oriented Programming) adalah teknik membuat suatu program berdasarkan objek dan apa yang bisa dilakukan objek tersebut. OOP terdiri dari objek-objek yang berinteraksi satu sama lain untuk menyelesaikan sebuah tugas. Kode-kode di-breakdown agar lebih mudah di-manage. Breakdown berdasarkanobjek-objek yang ada pada program tersebut. Dianjurkan  diimplementasikan untuk program dengan berbagai ukuran karena lebih mudah untuk men-debug. 
  > Karakteristik dari OOP mencakup:
  > 1) Program-program dibuat dari pendefinisian objek-objek, fungsi-fungsi, dan kebanyakan perhitungan komputasi diekspresikan ke dalam operasi pada objek.
  > 2) Masing-masing pendefinisian objek merujuk ke beberapa objek atau konsep yang sebenarnya pada dunia nyata, dan fungsi-fungsi pada objek dianalogikan sebagai interaksi pada objek. 
  > 3) Pada suatu objek terdapat metode-metode yang dapat digunakan, seperti keys dan values.
 
# 2. Berikan apa saja contoh pengimplementasian dari oop
# Pengimplementasian dari OOP:
  1) Encapsulation. Penggabungan antara data (attribut) dengan prosedure (method) yang mengolahnya.Enkapsulasi telah diterapkan jika setiap objek tetap menjaga state/variabel-variabel yang ada dalam dirinya tetap Private. Sehingga, ketika objek lain berinteraksi dengannya, objek tersebut tidak memiliki akses langsung ke state ini. Sebagai gantinya, mereka hanya dapat menngakses berbagai fungsi/method public yang disediakan oleh suatu objek.
  2) Inheritance. Penurunan sifat (attribut dan method) dari Class Parent (SuperClass) ke Class Child (SubClass). Ini menandakan bahwa OOP mendukung konsep code reuse dimana data-data yang ada di class parent bisa di kenal di kelas child.
  3) Polymorphism. Sebuah kemampuan dari sebuah objek untuk bekerja dalam berbagai bentuk. Penggunaan umum polymorphism biasanya digunakan ketika sebuah reference dari class parent digunakan untuk mengacu ke class child.
  4) Abstraction. Abstraction atau abstraksi merupakan prinsip OOP lainnya yang memungkinkan pengembang memerintahkan suatu fungsi tanpa perlu mengetahui kinerja dari fungsi tersebut. Dengan kata lain, abstraksi bisa disebut sebagai penyembunyian latar belakang secara rinci dan hanya menampilkan informasi yang diperlukan saja. Analogi sederhananya yaitu ketika menggunakan smartphone, pengguna cukup memberikan sebuah perintah tanpa harus mengetahui proses kerjanya.
  5) Class. Class adalah cetak biru/prototipe/pendefinisian dari suatu benda. Didalam class-lah attribut dan method suatu object didefinisikan. Contoh : Manusia, Window
  6) Object. Object adalah bentuk instance/nyata/real/hidup dari sebuah class. 
     Contoh :
     - Shelly:Manusia (Object Shelly mempunyai Class Manusia)
     - Form1:Window (Object Form1 mempunyai class Window)
     Setiap object pasti memiliki class (sebagai templatenya). Setiap object harus diinstansiasi/dihidupkan terlebih dahulu sebelum digunakan. Instansiasi sebuah objek dapat dilakukan dengan keyword new. 
     Contoh:
     - NamaClass NamaObject;
     - NamaObject=new NamaClass(parameter_konstruktornya);

     
