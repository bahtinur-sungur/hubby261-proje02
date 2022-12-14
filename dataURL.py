import os
class DataURL:
  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
    kontrolHTTP = siteURL[:7]
    kontrolHTTPS = siteURL[:8]
    http = "http://"
    https = "https://"
    if kontrolHTTP == http or kontrolHTTPS == https:
      dataOpen.write(siteURL+"\n")
      dataOpen.close()
      print("URL başarıyla kaydedildi")
    else:
      print("URL girişi hatalı")
      time.sleep(1)
      print("Lütfen site adresini ön eki ile birlikte giriniz")
      time.sleep(2)

  def dataRead(self):
    dataOpen = open(self.dataFile, 'r')
    if os.stat(self.dataFile).st_size != 0:
     for dataShow in dataOpen:
      print(dataShow)
    else:
      print("Kaydedilmiş adres yok")
    dataOpen.close()