from config import config

class Comms_error(Exception):
    pass

class ConfigValidationsError(Comms_error):
    def __init__(self, *args):
        super().__init__(*args)
        self.needed_config_valuse=[ 
            "PLAYER NAME",
            "GOBLIN NAME",
            "ORC NAME",
            "PLAYER LIFE",
            "PLAYER STRENGH",
            "PLAYER AGILITY",
            "PLAYER LUCK",
            "GOBLIN LIFE",
            "GOBLIN STRENGH",
            "GOBLIN AGILITY",
            "GOBLIN LUCK",
            "ORC LIFE",
            "ORC STRENGH",
            "ORC AGILITY",
            "ORC LUCK",
            "DAMAGE"
        ]
    def validation_config_type(self,config):
        if not isinstance(config,dict):
            raise ConfigValidationsError("config file is not set correctly")
              
    def validations_exists(self,config):
        for key in self.needed_config_valuse:
            if key not  in config:
                raise ConfigValidationsError (f"{key} is not exists")
    def validations_int(self,config):
        for key in self.needed_config_valuse[3:]:
            if not isinstance(config[key],int):
                        raise ConfigValidationsError (f"{key} must be int number!")
    def validations_str(self,config):
        for key in self.needed_config_valuse[:2]:
                    if not isinstance(config[key],str) or not config[key].strip():
                                raise ConfigValidationsError (f"{key} must be str!")
         
    def run_validations(self,config):
          self.validation_config_type(config)
          self.validations_exists(config)
          self.validations_int(config)
          self.validations_str(config)
     