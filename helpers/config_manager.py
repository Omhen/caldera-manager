import ConfigParser

es_en = {
    'Tiempo_de_barrido': 'cleanup_time',
    'Tiempo_de_encendido': 'max_start_time',
    'Tiempo_carga_plena': 'full_load_time',
    'Duracion_ciclo_minima': 'min_cycle_time'
}

en_es = {value: key for key, value in es_en.iteritems()}

class ConfigManager(object):

    def __init__(self, config_file):
        self.config_file = config_file
        self.config = ConfigParser.SafeConfigParser()
        self.config.read(config_file)

    def flush(self):
        with open(self.config_file, 'wb') as f:
            self.config.write(f)

    def get(self, section, name, type=str):
        key = es_en.get(name, name)
        value = self.config.get(section, key)
        return type(value)

    def put(self, section, name, value):
        key = es_en.get(name, name)
        self.config.set(section, key, value)

    def get_all(self, section):
        result = {}
        for pair in self.config.items(section):
            result[en_es.get(pair[0], pair[0])] = pair[1]
        return result
