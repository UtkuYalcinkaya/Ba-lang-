urunler=[] 
adet = int(input('Kaç Adet Ürün Girmek İstersiniz? '))

i=0

while(i<adet):
    name = input('Ürün İsmi: ')
    price = input('Ürün Fiyatı: ')
    urunler.append({
    'name': name,
    'price': price 
    })

    i+=1

for urun in urunler:
    print(f' Ürün adı: {urun["name"]} Ürün Fiyatı {urun["price"]}')
