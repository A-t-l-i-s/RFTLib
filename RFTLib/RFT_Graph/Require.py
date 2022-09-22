import os
import cv2
import math
import time
import ntpath
import random
import collections

import numpy as np

from typing import *
from dataclasses import dataclass

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import QApplication, QWidget

app=QApplication([])



Number=NewType("Number",Union[int,float,complex])


