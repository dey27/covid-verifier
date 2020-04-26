import logging, logging.config, os
from django.conf import settings

"""
Add the following in settings.py
1. 'utility' in INSTALLED_APPS
2. from utility.logging.logging import Logging
3. LOGGING = Logging.LOG_CONFIGURATION
"""


class LogProject:
    """
    Add in settings.py - 
    from utility.logging.logging import LogManager
    LogManager.get_logger()
    """
    def get_log_filepath():
        if not os.path.exists(str(settings.BASE_DIR) + '/logs'):
            os.makedirs(str(settings.BASE_DIR) + '/logs')
        return str(settings.BASE_DIR) + '/logs/logs.log'

    def init_logger(log_class=__name__):
        config_file = str(settings.BASE_DIR) + '/utility/logging/log_config.conf'
        log_path = LogProject.get_log_filepath()
        logging.config.fileConfig(config_file, defaults={'logfilename': log_path},
                                  disable_existing_loggers=False)
        return logging.getLogger("SABAR")
