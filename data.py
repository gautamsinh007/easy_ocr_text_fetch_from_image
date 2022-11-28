z = ['sales invoice apple invoice no: 1234 i7th may, 2022 invoice to: yudiz hello@reallygreatsite.com 123 anywhere st, any city, st 12345 description qty cost subtotal initial consultation 5 s300.00 s15.000 project draft 2 s500.00 s1.ooo implementation s12.000 s12.000 foundation labor 30 s60.00 s1.800 payment details: subtotal s29.800 bank code: tax s250.00 123-456-7890 bank name: total 530.050 fauget bank contact us thank youl +123-456-7890 wwwreallygreatsite.com 123 anywhere st, any city, st 12345 administrator frf' ,
    'simform invoice to yudiz purchase invoice 123 anywhere st., st 12345 hello@reallygreatsite.com invoice no #1234 +123-456-7890 invoice date february 05, 20223 name qty price total item name s50 s200 item name 3 s1oo s300 item name s40 s120 item name 3 s20 s60 item name 2 s80 s160 sub-total s840 tax s1o total s850 zalan thank you! administrator +123-456-7890 hello@reallygreatsite.com 123 anywhere st.> city any city , any']

# a = ["png bsjk  ifsjf fjs fjds jf sfjsf  goal","jpg","png","jpg","png","jpg"]



png = []
jpg = []

for i in z:
    
    
    
    x = i
    if 'sales' in x:
        print(True)
        png.append(i)
    break
    # print(i)


print(png)
print(jpg)














# import easyocr 
# from pprint import pprint
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# reader = easyocr.Reader(['en'])

# ii = ['per.png', 'sal.png']





# result  =  reader.readtext(ii)


# text = ''
# for i  in result:
#     text += i[1] + ' '
    
# op = text.lower()

# x = (op)

# print(x)


# salse = []
# perchecs  = []




# if "salse" or "sale" or "salses" in x:
#     print(True)
    
#     salse.append(ii)
    
# elif "purchase" or "purchases" in x:
#     perchecs.append(ii)
    
# else:
#     print(False)    
    

# print(salse,"sal")  
# print(perchecs,"pur")
    
    