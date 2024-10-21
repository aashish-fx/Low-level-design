
import typing as tp
import threading
import time

from constants import TRAFFIC_DURATION
from traffic_condition import TrafficCondition
from road import Road
from _enum import SignalsEnum
from traffic_lights import TrafficLight

class TrafficController:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.roads = {}
        return cls._instance
        
    def add_road(self, road: Road):
        self.roads[road.name] = road
    
    def remove_road(self, road_name):
        self.roads.pop(road_name, None)
        
    def control(self):
        total_green_signal_time = 0
        for road in self.roads.values():
            self._set_duration_of_green_signal(road)
            traffic_light = road.get_traffic_light()
            total_green_signal_time += traffic_light.green_light.duration()
        for road in self.roads.values():
            self._set_duration_of_red_signal(road, total_green_signal_time)
            traffic_light = road.get_traffic_light()
            threading.Thread(target=self._start_signal, args=traffic_light, daemon=True).start()
                
    def _set_duration_of_green_signal(self, road: Road):
        condition = TrafficCondition(road).get_condition()
        duration = TRAFFIC_DURATION[condition.value]
        road.get_traffic_light().set_signal_duration(SignalsEnum.GREEN, duration)
    
    def _set_duration_of_red_signal(self, road: Road, total_duration_of_green_light: int):
        red_light_duration = total_duration_of_green_light - road.get_traffic_light().green_signal.duration
        road.get_traffic_light().set_signal_duration(SignalsEnum.RED, red_light_duration)
    
        
    def _start_signal(self, traffic_light: TrafficLight):
        while True:
            green_duration = traffic_light.green_light.duration()
            time.sleep(green_duration)
            traffic_light.change_signal(SignalsEnum.YELLOW)
            yellow_duration = traffic_light.get_curr_light().duration()
            time.sleep(yellow_duration)
            traffic_light.change_signal(SignalsEnum.RED)
            red_duration = traffic_light.get_curr_light().duration()
            time.sleep(red_duration)
            
    def handle_emergency(self, road_name: str):
        road: Road = self.roads[road_name]
        road.get_traffic_light().change_signal(SignalsEnum.GREEN)
        time.sleep(20)
        
            
            
            
        
            
            
            