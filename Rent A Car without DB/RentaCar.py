import datetime
# parent class
class VehicleRent:
    def __init__(self, stock):
        self.stock = stock    # self.stock parameter now can be used in the methods of VehicleRent
        self.now = 0          # we use to calculate the bill

    def displayStock(self):
        """
            display stock
        """
        print("{} vehicle is available to rent".format(self.stock))
        return self.stock


    def rentHourly(self, n):
        """
            reny hourly, n number of vehicle
        """
        if n <= 0:
            print("number should be more then zero")
            return None
        elif n > self.stock:
            print(" Sorry {} vehicle are available to rent".format(self.stock))

        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours".format(n, self.now.hour))
            self.stock -= n
            return self.now

    def rentDaily(self, n):
        """
            rent daily
        """

        if n <=0:
            print("Number of vehicle should be more than zero")
            return None

        elif n > self.stock:
            print(" Sorry {} numbers of vehicle is available".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} number of vehicle on {} hours".format(n,self.now.hour))
            self.stock -= n
            return self.now

    def returnVehicle(self,request,brand):
        """
        return a bill, we need to calculate the cost
        :param request:
        :param brand:
        :return:
        """
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24

        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0
        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()  # time of return
                rentalPeriod = now - rentalTime  # difference of when it is rented and return
                if rentalBasis == 1: # hourly
                    bill = rentalPeriod.seconds/3600*car_h_price*numOfVehicle
                elif rentalBasis == 2: # daily
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numOfVehicle
                if (2<= numOfVehicle):
                    print("You have a %20 discount")
                    bill = bill*0.8
                print("Thanks returning the car")
                print("Price: $ {}".format(bill))
                return bill

        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()  # time of return
                rentalPeriod = now - rentalTime
                if rentalBasis == 1:  # hourly
                    bill = rentalPeriod.seconds /3600*bike_h_price*numOfVehicle
                elif rentalBasis == 2:  # daily
                    bill = rentalPeriod.seconds /(3600*24)*bike_d_price*numOfVehicle
                if (4 <= numOfVehicle):
                    print("You have a %20 discount")
                    bill = bill * 0.8
                print("Thanks returning the bike")
                print("Price: $ {}".format(bill))
                return bill
        else:
            print("You couldn't rent any vehicle")
            return None

# child class 1
class CarRent(VehicleRent):   # inheritance
    global discount_rate
    discount_rate = 15
    def __init__(self,stock):
        super().__init__(stock) # when we user this, CarRent class inherits from VehicleRent and use stock variable from VehicleRent.
                                     # above command inherit the initializer of Parent Class

    def discount(self,b):
        bill = b - (b*discount_rate)/100
        return bill






# child class 2
class BikeRent(VehicleRent):
    def __init__(self,stock):
        super().__init__(stock)





# customer
class Customer:
    def __init__(self):
        self.bikes = 0
        self.cars = 0
        self.rentalBasis_b = 0
        self.rentalBasis_c = 0
        self.RentalTime_b =0
        self.RentalTime_c = 0

    def requestVehicle(self, brand):
        """
        request vehicle by customer
        :return:
        """
        if brand == "bike":
            bikes = input("How many bikes do you want to rent:")

            try:
                bikes = int(bikes)
            except ValueError:
                print("Please enter a number")
                return -1

            if bikes < 1:
                print("Number of bikes can not be <1")
                return -1

            else:
                self.bikes  = bikes

                return bikes

        elif brand == "car":
            cars = input("How many cars do you want to rent:")

            try:
                cars = int(cars)
            except ValueError:
                print("Please enter a number")
                return -1

            if cars < 1:
                print("Number of cars can not be <1")
                return -1

            else:
                self.cars = cars
                return cars

        else:
            print("request vehicle error")



    def returnVehicle(self,brand):
        """
        return vehicle
        :return:
        """
        if brand == 'bike':
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return 0,0,0

        elif brand == "cars":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars

            else:
                return 0, 0, 0



        else:
            print("Return vehicle error")

