import urllib.request as url
print("          ASN lookup \n"+"Created By :"+"Abisheik M \n"+" \n ▁ ▂ ▄ ▅ ▆ ▇ █ 𝟘𝕩𝟞𝟙𝟞𝕓𝟞𝕕 █ ▇ ▆ ▅ ▄ ▂ ▁"+" \n \n follow me on instagram :"+"https://www.instagram.com/__its_just._.akm/")
Asn = input("Enter the Asn to Get the Ip Range : ") #Iknow the code suck but i can give you output
web = url.urlopen("https://api.hackertarget.com/aslookup/?q=" + Asn)
data = list(str(web.read()).split("n"))
for i in data:print(str(i)[:-1])
