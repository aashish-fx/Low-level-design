from log_levels import Level, DEBUG, INFO, ERROR, WARNING
from logging_message import LoggingMessage
from log_config import LogConfig


class Logger:
    _instance = None
    
    def __call__(cls):
        if not cls._instance:
            cls._instance = super().__call__(cls, Logger)
            cls.config = LogConfig()
        return cls._instance
    
    
    def _log(self, level: Level, message: str):
        if level.weight() >= self.config.log_level().weight():
            log_message = LoggingMessage(level, message)
            self.config.destination.add(log_message)
        
    def set_config(self, config: LogConfig):
        self.config = config
    
    def debug(self, message: str):
        self._log(DEBUG, message)
        
    def info(self, message):
        self._log(INFO, message)
        
    def error(self, message):
        self._log(ERROR, message)
    
    def warning(self, message):
        self._log(WARNING, message)
    
    
    