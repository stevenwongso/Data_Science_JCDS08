'''
Kaggle
buat dapet dataset, terdapat proyek dan competition juga

command
kaggle datasets download -d  user/link -- unzip
'''

'''
Git

Teknologi version controlling

setelah install

git config user.name
git config user.email

cara nge set
git config --global user.name {nama}
git config --global user.email {email}

git config --global user.name stevenwongso
git config --global user.email stevenwongso97@gmail.com

cara membuat chekpoint atau commit
    - git init

Pastikan di repo (folder) project kita sudah git enabled
P.s : pastikan di folder yang diinginkan, karena ketika contoh di C diaktifkan maka semua folder di C akan aktif
p.s : U sebaga simbol git telah enabled

add files to staging area
    - git add{nama file atau .}
    - git commit -m "{message yang diinginkan}"
        contoh : git commit -m "Version 1.0" 
p.s : A sebagai simbol telah berada di staging area

remove file dari suatu area :
    - git rm --cached {nama}

cara ngecek udha berapa kali  kommit
    - git log
    - git log -- oneline

p.s = simbol M mengindikasikan modified

cara kembali
- CHECKOUT commit => sifatnya read_only
    - git checkout {id commit}
- REVERT commit => bisa modifikasi beberapa kommit
- RESET commit => 
    - git reset {id commit} : balik cuma perubahan yang terakhir kali dilakukan masih dapat diselamatkan
    - git reset {id commit} --hard : balik ke state yang diinginkan perubahan yang dilakukan setelahnya akan hilang

cara membuat branch
    - git branch {namabranch}
    - git checkout -b {namabranch}

cara melihat branch 
    - git branch -a

p.s: (*) mengindikasikan posisi kita

cara ke branch yang diingikan 
    - git checkout {namabranch}

cara mendelete branch (pastikan tidak berada di branch tersebut)
    -git branch -D {namabranch}

ketika branchnya udah bagus di join lagi ke master
    - git merge {namabranch}


cara mengupload ke GitHub

- bikin repository
- git remote add {Nama Alias} https://github.com/stevenwongso/TestingGIT.git
- git push -u{kalau user udah sama ga usah} {Nama Alias} master 

apabila yang di github lebih update dibanding lokal bisa menggunakan
    - git pull {Nama Alias} master

apabila mau menarik projek yang berbeda
    - git clone {link}

cara mengikuti project:
    - forking di website github

apabila terdapat file yang tidak ingin di commit 
tambahkan file .gitignore
lalu tulis nama file di .gitignore

P.S : hal ini dapat dilakukan juga untuk library yang langsung terinstall pada projek

README

cek di testing git

ada preview di readme : klik kanan pada file => open preview (belum tentu 100% sama)
'''
