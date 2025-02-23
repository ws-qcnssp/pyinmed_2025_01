import requests
import matplotlib
import numpy as np
import pandas as pd
import pydicom
import selenium
import flask

import os
import sys

if sys.version_info[:3] == (3,11,9) and os.path.join(os.getcwd(), '.venv').lower() in sys.executable.lower():
    print('Wszystko ustawione!')
else:
    print(f'Używasz wersji pythona {sys.version_info[:3]}, z lokalizacji {sys.executable}. Sprawdź to :)')



