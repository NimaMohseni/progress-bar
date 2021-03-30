import time
import sys

class progressbar():
  def __init__(self):
    self.time1 = time.process_time()
    self.time2 = 0
    self.itert = 0
  def prgb(self, value=0, endvalue=0, bar_length=20):
    if (value==0):
      self.time1 = time.process_time()
      self.starttime = self.time1
      self.itert = 0
      avgiter = 0
    self.time2 = time.process_time()
    itertime = self.time2 - self.time1
    self.itert += itertime
    self.time1 = self.time2
    elapsedt = self.time2 - self.starttime
    avgiter = self.itert/(value+1)
    percent = float(value) / endvalue
    if (percent >= (1-(1 / endvalue))):
      percent = 1
    remainigt = int(((endvalue - value - 1)*avgiter)/60)
    remainigts = int(((endvalue - value - 1)*avgiter)%60)
    elapsedtm = int(elapsedt/60)
    elapsedts = int(elapsedt%60)
    if (value%16 in [0,1,2,3]):
      stri='◐'
    if (value%16 in [4,5,6,7]):
      stri='◓'
    if (value%16 in [8,9,10,11]):
      stri='◑'
    if (value%16 in [12,13,14,15]):
      stri='◒'    
    arrow = '❚' * int(round(percent * bar_length)-1) + '➤'
    spaces = '=' * (bar_length - len(arrow))
    sys.stdout.write("\r evaluating process: |{0}| {1}% ↹avg iteration time↹ : {2} sec, elapsed time {3} : {4}, est remainig time {5} : {6} {7}".\
                     format(arrow + spaces, round((percent * 100),2), round(avgiter, 4),elapsedtm ,elapsedts , remainigt, remainigts, stri))
    sys.stdout.flush()
