import configparser


def repeat(config_file_name):
    """Вывести повторенную count раз строку str (см. _legend.md)"""
    cnfg = configparser.ConfigParser()
    cnfg.read(config_file_name)
    return cnfg['DEFAULT']['str'] * int(cnfg['DEFAULT']['count'])


def get_connection_info(config_file_name, username):
    """Вывести пару строк (ip, port) для username или для DEFAULT."""
    cnfg = configparser.ConfigParser()
    cnfg.read(config_file_name)
    if username in cnfg:
        return cnfg[username]['ip'], cnfg[username]['port']
    return cnfg['DEFAULT']['ip'], cnfg['DEFAULT']['port']
