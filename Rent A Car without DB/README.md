This is a rent a car project written as object oriented programming.
Contains two python files:
RentaCar.py contains all the classes and methods while RentaCar_Main.py contains the menu.

Below is the planning before starting to code.
#parent class #########
- class vehicleRent
- we are going to use the below methods in the parent
- display stock, rent hourly, rent daily, return vehicle

#  Child class ###############
- CarRent and BikeRent are child classes inherits from Parent Class vehicleRent
- we will have discount method in the parent class

#  customer class ###########
- request vehicle
- return vehicle

# main.py and rent.py we will have two py script.
- class lar rent.py icerisinde
- methodlar ve classlarin objeleri main.py


# We first start writing with the layout with pass:

# parent class
class VehicleRent:
    def __init__(self, stock):
        pass

    def displayStock(self):
        """
            display stock
        """

        pass


    def rentHourly(self, n):
        """
            reny hourly
        """
        pass

    def rentDaily(self, n):
        """
            rent daily
        """

        pass

    def returnVehicle(self,request,brand):
        """
        return a bill
        :param request:
        :param brand:
        :return:
        """
        pass

# child class 1
class CarRent(VehicleRent):   # inherits from vehicleRent
    def __init__():
        pass
    
    def discount():
        pass

# child class 2
class BikeRent(VehicleRent):
    def __init__():
        pass

# customer class
class Customer:
    def __init__():
        pass
    
    def requestVehicle():
        """
        request vehicle
        :return:
        """
        pass
    
    def returnVehicle():
        """
        return vehicle
        :return:
        """
        pass  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
