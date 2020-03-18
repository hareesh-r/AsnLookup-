import urllib as url
print("          ASN lookup \n"+" \n ▁ ▂ ▄ ▅ ▆ ▇ █ 𝟘𝕩𝟞𝟙𝟞𝕓𝟞𝕕 █ ▇ ▆ ▅ ▄ ▂ ▁"+" \n \n follow me on instagram :"+"https://www.instagram.com/__its_just._.akm/")
Asn = input("Enter the Asn to Get the Ip Range : ") #Iknow the code suck but i can give you output
web = url.request.urlopen("https://api.hackertarget.com/aslookup/?q=" + Asn)
data = web.read()
print(data)
