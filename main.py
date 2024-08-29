HellDivers = {'Heavy': 991234, 'Light': 988823}
print('Список подразделений: ' , HellDivers)
#
print('Heavy: ', HellDivers['Heavy'])
#
HellDivers['AntiArmor'] = 450098
print('AntiArmor: ', HellDivers['AntiArmor'])
#
HellDivers.update({'AntiAir': 785525 ,
                   'Support': 987774})
#
print('Новый список подразделений: ', HellDivers)
#
HellDivers.pop('Heavy')
print('Обновленный список подразделений ', HellDivers)
print(HellDivers.get('Heavy', "В данный момент подразделение 'Heavy' упразднено"))
# разделение
print('----------------------------')
#
Whispers = {1,2,3,1,1, 'Gds lve us', 11 ,2,3,4,'wtHn0p4in'}
print(Whispers)
Whispers.update([22 , 'nm', 9.0])
Whispers.discard(1)
print(Whispers)