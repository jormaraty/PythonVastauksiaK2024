# Laskutoimituksia

'''
Laskujärjestys, voimakkain ensin:
   ensin sulut ()
   kerto- ja jakolaskut vasemmalta oikealle (*, /)
   yhteen- ja vähennyslaskut vasemmalta oikealle (+, -)
'''


print(2+3)                  # 5
print(2 + 8 / 2)            # 6, jakolasku 8/2 ensin

# laskutoimituksen tulos otetaan talteen muuttujaan 'tulos'
tulos = 2 * 3 + 2 * 5       # 16, sama kuin (2*3) + (2*5)
print(tulos)

tulos = 3 + 6 + 6 / 2           # 12, sama kuin 3 + 6 + (6/2)
# str(tulos) muuttaa numeron merkkijonoksi tulostusta varten
print("tulos on " + str(tulos) )
