from amtrak.objects.stop import Stop

class Route:
    def __init__(self, stops: list[Stop]):
        self.stops = stops
        
    def __len__(self):
        return len(self.stops)
    
    def __getitem__(self, index):
        return self.stops[index]
    
    def __iter__(self):
        return iter(self.stops)
    
    def __repr__(self):
        return f"<Route stops={len(self)}>"
    
    def __str__(self):
        return f"Route with {len(self)} stops"