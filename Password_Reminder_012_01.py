# Görev : 
# Diyelim ki; Geçmişte ihtiyacınız olan bir şifreyi yazdıran bir mesaj bıraktınız. 
# Yazmış olduğunuz şifreyi görebilmek için adınızı girmeniz ve programın sizi tanıması gerekmektedir. öyle bir program yazın . 
# Kullanıcıdan ilk adı alır ve sizinkiyle karşılaştırır,
# Ardından, kullanıcının girdiği ad sizinkiyle aynıysa, "Merhaba Yusuf ! Şifre: W@12" gibi bir çıktı alın,
# Kullanıcının girdiği ad sizinkiyle aynı değilse, "Merhaba, Amina ! Sonra görüşürüz" gibi bir çıktı alın.
user_input = input("Enter your name: ")
user = {"osman" : "Ankara@06"}
if user_input in user.keys() :
    print("Hello Osman! Password : ", user[user_input])
else:
    print("Hello guest ! See you later.")
