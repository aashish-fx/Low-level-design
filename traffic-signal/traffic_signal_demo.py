
from traffic_controller import TrafficController
from road import Road
from traffic_lights import TrafficLight

class TrafficLightDemo:
    @staticmethod
    def run():
        traffic_controller = TrafficController()
        
        mg_road = Road("MG ROAD")
        hsr_road = Road("HSR")
        
        traffic_controller.add_road(mg_road)
        traffic_controller.add_road(hsr_road)
        
        mg_road.set_traffic_light(TrafficLight())
        hsr_road.set_traffic_light(TrafficLight())
        
        traffic_controller.control()
        
    
    
if __name__ == "__main__":
    TrafficLightDemo.run()
    