from _enum import SignalsEnum
from signals import Green, Red, Signals, Yellow
from threading import Lock

class TrafficLight:
    def __init__(self):
        self.curr_signal = Red()
        self.green_signal = Green()
        self.red_signal = Red()
        self.yellow_signal = Yellow()
        self._lock = Lock()
        
    def get_signal(self, signal: SignalsEnum) -> Signals:
        if signal == SignalsEnum.GREEN:
            return self.green_signal
        if signal == SignalsEnum.YELLOW:
            return self.yellow_signal
        if signal == SignalsEnum.RED:
            return self.red_signal
    
    def set_signal_duration(self, signal: SignalsEnum, duration: int):
        signal_ = self.get_signal(signal)
        signal_.set_duration = duration
            
    def change_signal(self, signal: SignalsEnum) -> Signals:
        signal_ = self.get_signal(signal)
        with self._lock:
            self.curr_signal = signal_
        return self
    
    def get_curr_signal(self) -> Signals:
        return self.curr_signal
            
        