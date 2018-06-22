# >>> import sys
# >>>
# >>> try:
# ...     1/0
# ... except:
# ...     print(sys.exc_info())
# ...
# (<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero',), <traceback object at 0x101acb1c8>)
# None

# >>> import logging
# >>> logging.basicConfig()
# >>> logger = logging.getLogger(__name__)
# >>>
# >>> logger.critical('logging is easier than I was expecting')
# CRITICAL:__main__:logging is easier than I was expecting

# -- Logging Levels --
# >>> logger.critical("this better be bad")
# CRITICAL:root:this better be bad
# >>> logger.error("more serious problem")
# ERROR:root:more serious problem
# >>> logger.warning("an unexpected event")
# WARNING:root:an unexpected event
# >>> logger.info("show user flow through program")
# >>> logger.debug("used to track variables when coding")

# -- Formatting the Logs --
# >>> import logging
# >>> logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
# >>> logging.basicConfig(format=logFormatter, level=logging.DEBUG)
# >>> logger = logging.getLogger(__name__)
# >>> logger.info("test")
# 2018-06-19 17:42:38,134 - INFO - test

# -- Adding Context --
# >>> import logging
# >>> logFormatter = '%(asctime)s - %(user)s - %(levelname)s - %(message)s'
# >>> logging.basicConfig(format=logFormatter, level=logging.DEBUG)
# >>> logger = logging.getLogger(__name__)
# >>> logger.info('purchase completed', extra={'user': 'Sid Panjwani'})
# 2018-06-19 17:44:10,276 - Sid Panjwani - INFO - purchase completed

# -- Logging to File --
# >>> import logging
# >>> logger = logging.getLogger(__name__)
# >>>
# >>> handler = logging.FileHandler('myLogs.log')
# >>> handler.setLevel(logging.INFO)
# >>>
# >>> logger.addHandler(handler)
# >>> logger.info('You can find this written in myLogs.log')
