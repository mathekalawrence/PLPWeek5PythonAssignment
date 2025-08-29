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
        