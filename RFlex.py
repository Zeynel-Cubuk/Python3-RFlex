import ftplib
import time

class FTPChecker(object):

    def __init__(self,host="",port=21):
        self.host = host
        self.port = port
        self.C = '\033[36m'
        self.P = '\033[35m'
        self.G = '\033[1;32m'
        self.R = '\033[31m'

    def banner(self):
        W = '\033[0m'  # beyaz
        R = '\033[31m'  # kirmizi
        G = '\033[1;32m'  # koyu yesil
        O = '\033[33m'  # turuncu
        B = '\033[34m'  # mavi
        P = '\033[35m'  # mor
        C = '\033[36m'  # sari
        GR = '\033[37m'  # gri
        RED = "\033[1;31m"
        BLUE = "\033[1;34m"
        CYAN = "\033[1;36m"
        GREEN = "\033[0;32m"

        print(R+"  ______     ______     __   __   __     ______     ______  ")
        print(R+" /\  ___\   /\  __ \   /\ \ / /  /\ \   /\  ___\   /\__  _\ ")
        print(R+r" \ \___  \  \ \ \/\ \  \ \ \'/   \ \ \  \ \  __\   \/_/\ \/ ")
        print(R+"   \/\_____\  \ \_____\  \ \__|    \ \_\  \ \_____\    \ \_\ ")
        print(R+"    \/_____/   \/_____/   \/_/      \/_/   \/_____/     \/_/ ☭")
        print(CYAN+"# Author      :"+ "KIZILYILDIZ✮")
        print(CYAN+"# Instagram   :"+ "https://www.instagram.com/kiziilyildiz")
        print(CYAN+"# GitHub      :"+ "https://github.com/Zeynel-Cubuk")
        print(CYAN+"# Title       :"+ "RFlex.py")
        print(CYAN+"# Date        :"+ "13/1/2021")
        print(CYAN+"# Version     :"+ "1.2")

        print(self.R + "#===========================")
        print("[*] IP/Host:", self.host)
        print(self.R + "#===========================")

    def ftp_connect(self):
        # FTP BAĞLANTISINI GERÇEKLEŞTİRİR
        self.ftp = ftplib.FTP(host)
        try:
            self.ftp.login("anonymous","anonymous")
            return self.ftp
        except:
            return "İşlem Başarısız!"
    def file_list(self):
        # FTP SUNUCUDA BULUNAN DOSYALARI LİSTELER
        ftp = self.ftp_connect()
        files = ftp.nlst()
        for file in files:
            time.sleep(1)
            print(self.G+"[Found]:",file)

    def upload_files(self,file=""):
        # FTP SUNUCUSUNA DOSYA YÜKLER
        ftp = self.ftp_connect()
        f = open(file, 'rb+')

        try:
            ftp.storbinary('STOR '+str(f.name), f)
            f.close()
            return "Dosya Başarıyla Yüklendi.."

        except:
            return "İşlem Başarısız!"



    def down_file(self,saveFile=str(),downFile=str()):
        # FTP SUNUCUDAN DOSYA İNDİRİR
        ftp = self.ftp_connect()

        for file in ftp.nlst():
            print("[Found]: ",file)


        self.downFile = input("Dosya Adı:")
        self.saveFile = input("Kayıt Adı: ")
        # KULLANICI TARAFINDA YAZILACAK VERİ DOSYA İŞLEMLERİ
        f = open(self.saveFile,"wb+")
        # SUNUCU ÜZERİNDE VERİ DOSYASI ALIMI
        try:
            ftp.retrbinary(r'RETR '+str(self.downFile) ,f.write)
            time.sleep(0.5)
            f.close()
        except:
           return "İşlem Başarısız!"

        return "Dosya Başarıyla İndirildi.."

    def del_file(self,file=""):
        ftp = self.ftp_connect()

        try:
            ftp.delete(file)

        except:
            print("İşlem Başarısız!")

    def dir_process(self):
        ftp = self.ftp_connect()

        try:

            cmd = input("Komut: ")
            com = ftp.sendcmd(cmd)
            print(com)
        except:
            print("İşlem Başarısız!")

        try:
            # testWrite666.txt
            newFile = input("Dosya Oluştur: ")
            ftp.mkd(newFile)
        except:
            print("İşlem Başarısız!")

        try:
            fromFile = input("Değiştirilecek Dosya: ")
            toFile = input("Yeni Dosya Adı: ")
            ftp.rename(fromFile, toFile)

        except :
            print("İşlem Başarısız!")

        print("Bulunulan Dizin: ",ftp.pwd())
        print("Dizin Klasör/Dosyalar: ")
        ftp.dir()


if __name__ == "__main__":
    # 114.55.39.153
    # 45.144.179.154
    # 142.103.6.49
    # 128.223.4.25
    host = "114.55.39.153"

    ftpchecker = FTPChecker(host=host,port=21)
    ftpchecker.banner()
    #ftpchecker.file_list()

    #print(ftpchecker.down_file()) #[Found]:  \home\ftpadmin\sbt\policy\9df52e00-71a7-46ce-8110-f0cc94b698a7.10.10???.xls
    #ftpchecker.dir_process()
    #print(ftpchecker.upload_files("v.jpg"))
    #ftpchecker.file_list()
