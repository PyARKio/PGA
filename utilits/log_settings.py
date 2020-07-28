# -- coding: utf-8 --
from __future__ import unicode_literals
import logging
import logging.handlers
import traceback
import platform
import sys


__author__ = "PyARKio"
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


def linux_distribution():
  try:
    return platform.linux_distribution()
  except:
    return "N/A"


trace_pattern = logging.Formatter("[%(asctime)s] %(levelname)s %(module)s:%(lineno)d:%(funcName)s: %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(trace_pattern)

log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.addHandler(stream_handler)

if platform.system() == 'Linux':
    file_handler = logging.handlers.RotatingFileHandler('/home/qwerty/LOGS/PersonalGovernmentAssistant.log', 'a', 10 * 1024 * 1024, 10)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(trace_pattern)
    log.addHandler(file_handler)
elif platform.system() == 'Windows':
    file_handler = logging.handlers.RotatingFileHandler('d:/LOGS/PersonalGovernmentAssistant.log', 'a', 10 * 1024 * 1024, 10)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(trace_pattern)
    log.addHandler(file_handler)


log.info("""Python version: %s
linux_distribution: %s
system: %s
machine: %s
platform: %s
uname: %s
version: %s
mac_ver: %s
""" % (
sys.version.split('\n'),
linux_distribution(),
platform.system(),
platform.machine(),
platform.platform(),
platform.uname(),
platform.version(),
platform.mac_ver(),
))


