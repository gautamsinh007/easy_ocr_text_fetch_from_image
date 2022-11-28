import easyocr 
from pprint import pprint
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

reader = easyocr.Reader(['en'])

ii = ['per.png', 'sal.png' ,'sal2.png', 'pur2.png', 's.png']


datas = ''


salse = []
extra = []
perchecs  = []
    
for j in ii:
    xx = str(j)
    print(xx,"------------------")
    result  =  reader.readtext(j)


    text = ''
    for i  in result:
        # print(i,"========================")
        text += i[1] + ' '
        # break
    op = text.lower()    
    
    if "purchase"   in op:
        perchecs.append(xx)
   
    else:
       salse.append(xx)    
              
              
    print(op)
  
        
      
    

print(salse,"sal")  
print(perchecs,"pur")

print(extra,"extra====")



    
    