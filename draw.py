# Create By: Hesham White
# heshamwhite@gmail.com
# 15 Nov 2017

from random import randint

pot1 = ['RUSSIA','GERMANY','BRAZIL','PORTUGAL','ARGENTINA','BELGIUM','POLAND','FRANCE']
pot2 = ['SPAIN','PERU','SWITZERLAND','ENGLAND','COLOMBIA','MEXICO','URUGUAY','CROATIA']
pot3 = ['DENMARK','ICELAND','COSTA RICA','SWEDEN','TUNISIA','EGYPT','SENEGAL','IRAN']
pot4 = ['SERBIA','NIGERIA','AUSTRALIA','JAPAN','MOROCCO','PANAMA','KOREA REP.','SAUDI ARABIA']

continent_dict = {'TUNISIA':'CAF','EGYPT':'CAF','SENEGAL':'CAF','NIGERIA':'CAF','MOROCCO':'CAF',
'IRAN':'AAF','KOREA REP.':'AAF','SAUDI ARABIA':'AAF','JAPAN':'AAF',
'BRAZIL':'SAFA','ARGENTINA':'SAFA','PERU':'SAFA','COLOMBIA':'SAFA','URUGUAY':'SAFA',
'MEXICO':'NAFA','COSTA RICA':'NAFA','PANAMA':'NAFA',
'RUSSIA':'UEFA','GERMANY':'UEFA','BELGIUM':'UEFA','POLAND':'UEFA','FRANCE':'UEFA','SPAIN':'UEFA','CROATIA':'UEFA','SWITZERLAND':'UEFA','ENGLAND':'UEFA',
'DENMARK':'UEFA','ICELAND':'UEFA','SWEDEN':'UEFA','SERBIA':'UEFA','AUSTRALIA':'OFC','PORTUGAL':'UEFA'
}


for i in range(0,8):
  print('group ',i+1,':')
  first_choice = pot1[i]
  x = randint(0, len(pot2)-1)
  current_choice = pot2[x]
  while continent_dict[current_choice] != 'UEFA' and continent_dict[current_choice] == continent_dict[first_choice]:
      x = randint(0, len(pot2)-1)
      current_choice = pot2[x]
  second_choice = current_choice
  pot2.remove(second_choice)

  x = randint(0, len(pot3)-1)
  current_choice = pot3[x]
  while continent_dict[current_choice] != 'UEFA' and (continent_dict[current_choice] == continent_dict[first_choice] or continent_dict[current_choice] == continent_dict[second_choice] ):
      x = randint(0, len(pot3)-1)
      current_choice = pot3[x]
  third_choice = current_choice
  pot3.remove(third_choice)

  x = randint(0,len(pot4)-1)
  current_choice = pot4[x]
  while continent_dict[current_choice] != 'UEFA' and (continent_dict[current_choice] == continent_dict[first_choice] or continent_dict[current_choice] == continent_dict[second_choice] or continent_dict[current_choice] == continent_dict[third_choice] ):
      x = randint(0, len(pot4)-1)
      current_choice = pot4[x]
  fourth_choice = current_choice
  pot4.remove(fourth_choice)

  print(first_choice)
  print(second_choice)
  print(third_choice)
  print(fourth_choice)
