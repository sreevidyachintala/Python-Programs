
# 1kilobyte == 1024bytes
# 8192bits == 1024bytes
# 1bit == 1024/8192

# unit converters
u1=input('Which unit would you like to convert from("bits,bytes,kilobytes"): ')
u2=input('Which unit would you like to convert to("bits,bytes,kilobytes"): ')
value=int(input('enter your value:'))

if u1=='bits' and u2=='bytes':
   print("%s bytes" %(value/8))

elif u1=='bytes' and u2=='bits':
   print("%s bits" %(value*8))

elif u1=='bits' and u2=='kilobytes':
   print("%s kilobytes" %(value/8192))

elif u1=='bytes' and u2=='kilobytes':
   print("%s kilobytes" %(value/1024))

elif u1=='kilobytes' and u2=='bits':
   print("%s bits" %(value*8192))

elif u1=='kilobytes' and u2=='bytes':
   print("%s bytes" %(value*1024))

else:
   print('invalid u1 and u2')






