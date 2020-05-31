# 02-Logic, IF, Else IF, Else

# Solve it! #1
# x = input("Masukkan Angka : ")
# if ( int(x) % 2 != 0) :
#     print ("Angka", x, "tergolong bilangan GANJIL!") ;
# else :
#     print ("Angka", x, "tergolong bilangan GENAP!") ;

# Solve it! #2
# import math
# massa = input(" Masukkan Massa (kg) : ")
# tinggi = input(" Masukkan Tinggi (cm) : ")
# print("Massa", massa, "kg", "& Tinggi", float(tinggi)/100,"m")
# IMT = int(massa)/math.pow((int(tinggi)/100), 2)
# if (IMT < 18.5):
#     print("IMT =", IMT, "Berat Badan Kurang" );
# elif (IMT >= 18.5 and IMT <= 24.9) :
#     print("IMT =", IMT, "Berat Badan ideal" );
# elif (IMT >= 25.0 and IMT <= 29.9) :
#     print("IMT =", IMT, "BB Berlebih" );
# elif (IMT >= 30.0 and IMT <= 39.9) :
#     print("IMT =", IMT, "BB Sangat Berlebih" );
# else :
#     print("IMT =", IMT, "Obesitas" );