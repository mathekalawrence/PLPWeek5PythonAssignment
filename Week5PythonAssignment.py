#Designing a class
class House:
    """Base class representing a house"""
    
    def __init__(self, address, size_square_feet, num_bedrooms, num_bathrooms, color, price):
        """A constructor to initialize the house class attributes"""
        self.address = address
        self.size_square_feet = size_square_feet
        self.num_bedrooms = num_bedrooms
        self.num_bashrooms = num_bathrooms
        self.price = price
        self.color = color
        self.is_sold = False
        
    def calculate_price_per_sqft(self):
        """Calculating the price per square foot"""
        return self.price / self.size_square_feet
    
    def mark_as_sold(self):
        """Mark the house as sold"""
        self.is_sold = True
        print(f"House at {self.address} has been sold!")
        
    def renovate(self, renovation_cost):
        """Add renovation cost to the price"""
        self.price += renovation_cost
        print(f"Renovation completed. Redefined price is ${self.price:,.2f}")
        
    def get_house_info(self):
        """Return full information"""
        status = "Sold" if self.is_sold else "Available"
        return f"""
        Address: {self.address}
        Size: {self.size_square_feet} sqft
        Color: {self.color}
        Bedrooms: {self.num_bedrooms}
        Bathrooms: {self.num_bashrooms}
        Price: ${self.price:,.2f}
        Status: {status}
        Price per sqft: ${self.calculate_price_per_sqft():.2f}   
    """
    def__str__(self):
    """String representation of the house"""
       return f"House at {self.address} = ${self.price:,.2f}"
   
   #Inheritance/ specailized house types
class Apartment(House):
    def __init__(self, address, size_square_feet, num_bedrooms, num_bathrooms, price, floor_number, has_doorman):
        """    Constructor for apartment with additional attributes
        
        _summary_

        Args:
            address (_type_): _description_
            size_square_feet (_type_): _description_
            num_bedrooms (_type_): _description_
            num_bathrooms (_type_): _description_
            price (_type_): _description_
            floor_number (_type_): _description_
            has_doorman (bool): _description_
        """
        
        super().__init__(address, size_square_feet, num_bedrooms, num_bathrooms, price)
        self.floor_number = floor_number
        self.has_doorman = has_doorman
        self.monthly_maintenance = 300 #Encapsulated attribute
    
    #Encapsulation using getters and setters
    def get_maintenance_fee(self):
        return self.monthly_maintenance
    
    def get_house_info(self): #Method overriding/polymorphism
        base_info = super().get_house_info()
        doorman = "Yes" if self.has_doorman else "No"
        return base_info + f"""
        Floor: {self.floor_number}
        Doorman: {doorman}
        Monthly Maintenance: ${self.monthly_maintenance}
        Estimated Monthly cost: ${self.calculate_monthly_costs():.2f}
        """
#Demonstration of the classes
def main():
    print("===HOUSE CLASS DEMOSTRATION===\n")
    
    #create basic
   
        
        
        