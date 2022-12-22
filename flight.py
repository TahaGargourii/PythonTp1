class Flight:   
     def __init__(self, src_code, dst_code, duration):   
             self.src_code = src_code       
             self.dst_code = dst_code       
             self.duration = duration    
             def __new__(cls, src_code, dst_code, duration):       
              flight = super().__new__(cls) 
                # initialize attributes      
              flight.src_code = src_code     
              flight.dst_code = dst_code      
              flight.duration = duration     
                 # inject new attribute       
              flight.full_info = f'{src_code} {dst_code} {duration}'  
              return flight


