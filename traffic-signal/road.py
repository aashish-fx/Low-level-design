from traffic_lights import TrafficLight

class Road:
    def __init__(self, name: str):
        self.name = name
        self.traffic_light = None
        
    def get_road_name(self) -> str:
        return self.name
    
    def get_traffic_light(self) -> TrafficLight:
        return self.traffic_light
    
    def set_traffic_light(self, traffic_light: TrafficLight):
        self.traffic_light = traffic_light
        
    
            