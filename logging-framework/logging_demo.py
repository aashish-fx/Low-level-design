from logger import Logger
from log_config import LogConfig
from log_levels import DEBUG
from output_destinations import File

class LoggingDemo:
    
    @staticmethod
    def run():
        logger = Logger()
        logger.info("Get message")
        logger.debug("this issue has accured")
        logger.warning("Warring sign")
        
        config = LogConfig(DEBUG, File)
        logger.set_config(config)
        
        logger.debug("This is a debug message")
        
        
if __name__ == "__main__":
    LoggingDemo.run()