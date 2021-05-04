import sqlite3
import time

class Arac():
    def __init__(self,brand,model,color,speed):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = speed
    def __str__(self):
        return "brand: {}\nModel: {}\ncolor: {}\nspeed: {}\n*****************".format(self.brand,self.model,self.color,self.speed)

class Garaj():
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.con = sqlite3.connect("araclarkiralama.db")
        self.cursor = self.con.cursor()
        query_db = "create table if not exists araclar (brand TEXT,model TEXT,color TEXT,speed INT)"
        self.cursor.execute(query_db)
        self.con.commit()

    def baglanti_kes(self):
        self.con.close()

    def araclari_listele(self):
        query_db ="select * from araclar"
        self.cursor.execute(query_db)
        araclar = self.cursor.fetchall()
        if len(araclar) == 0:
            print("Sorry! There is no auto availabe at the moment.")
        else:
            for i in araclar:
                arac = Arac(i[0],i[1],i[2],i[3])
                print(arac)

    def auto_query_db(self,auto_feature,your_choice):  #input ile alacagiz
        query_db = "select * from araclar where {} = ?".format(auto_feature) ##  speed icin >= olabilir
        self.cursor.execute(query_db,(your_choice,))
        araclar = self.cursor.fetchall()
        if len(araclar)==0:
            print("There is no auto available with these features!")
        else:
            for i in araclar:
                arac = Arac(i[0],i[1],i[2],i[3])
                print(arac)

    def auto_add_db(self,arac):
        query_db = "insert into araclar Values(?,?,?,?)"
        self.cursor.execute(query_db,(arac.brand,arac.model,arac.color,arac.speed))
        self.con.commit()

    def remove_from_stock(self,brand):
        query_db = "delete from araclar where brand = ?"
        self.cursor.execute(query_db,(brand,))
        self.con.commit()
print("""**************************
What do you want to do ?
1. List the Vehicles
2. Request a vehicle
3. Add a vehicle
4. Delete a vehicle
**************************
""")
garaj = Garaj()

while True:
    islem = input('Which process do you want to do ? : ')
    if islem == 'q':
        print('Exit the program...')
        break

    elif islem == '3':
        brand = input("brand: ")
        model = input("Model: ")
        color = input("color: ")
        speed = int(input("speed: "))
        yeni_arac = Arac(brand, model, color, speed)
        garaj.auto_add_db(yeni_arac)
    elif islem == '1':
        garaj.araclari_listele()

    elif islem =='2':
        auto_feature = input('Choose your criteria:  (brand/model/color/speed): ')
        if auto_feature in ['brand','model','color','speed']:
            your_choice = input('{} your selection ? : '.format(auto_feature) )
            garaj.auto_query_db(auto_feature,your_choice)
        else:
            print("""Only brand,model,color or speed...""")
            auto_feature = input('Your choice? brand/model/color/speed: ')
            your_choice = input('{} your selection ? : '.format(auto_feature))
            garaj.auto_query_db(auto_feature, your_choice)

    elif islem == '4':
        auto_del = input('Auto brand to delete from the stock: ')
        garaj.remove_from_stock(auto_del)
    else:
        print('Invalid Selection..')

































