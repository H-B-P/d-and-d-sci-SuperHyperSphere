import numpy as np
import pandas as pd

import random

random.seed(1)
np.random.seed(1)

smell_effects = {"No":1, "Somewhat":0.757, "EXTREMELY":0.9422}
taste_effects = {"Apples":0.731, "Copper":0.922, "Burning":1.043, "Mint":1, "Nothing In Particular":0.525}
feng_effects = {"Disharmonious": 0.8412, "Adequate":1, "Exceptional":1.051}
sound_effects = {"Unearthly Squelching":0.5, "Unnatural Buzzing":0.7484, "Otherworldly Skittering":0.9611, "Impossible Humming":0.2323}

Longs = []
Lats = []
Shorts = []
Delts = []

Smells = []
Tastes = []
Fengs = []

SoundLists = []

Pis = []
Murphs = []

Perfs = []
PerfMeans = []

theDict = {}

def gen_row():
 Long = random.uniform(-180, 180)
 Lat = np.degrees(np.arccos(random.random()**(1/3)))*random.choice([1,-1])
 Short = np.degrees(np.arccos(random.random()**(1/3)))*random.choice([1,-1])
 Delt = np.degrees(np.arccos(random.random()**(1/3)))*random.choice([1,-1])
 
 Smell = random.choice(["No"]*3881+["Somewhat"]*5713+["EXTREMELY"]*406)
 Taste = random.choice(["Apples"]*2274+["Copper"]*412+["Burning"]*674+["Mint"]*4041+["Nothing In Particular"]*2599)
 Feng = random.choice(["Disharmonious"]*2521+["Adequate"]*7121+["Exceptional"]*358)
 
 SoundList = []
  
 if random.random()<0.1875:
  SoundList.append("Unearthly Squelching")
 if random.random()<0.5722:
  SoundList.append("Unnatural Buzzing")
 if random.random()<0.2885:
  SoundList.append("Otherworldly Skittering")
  if "Unnatural Buzzing" in SoundList:
   SoundList.remove("Unnatural Buzzing")
 if random.random()<0.1754:
  SoundList.append("Impossible Humming")
 if len(SoundList)==0:
  SoundList.append("Eerie Silence")
 
 Pi = 3.1408 + random.uniform(-0.02, 0.02)+random.uniform(-0.02, 0.02)
 Murph = max([random.uniform(0, 6), random.uniform(0,5), random.uniform(-3,4)])
 
 #Performance!
 
 Perf = 1
 
 Perf = Perf * (1 + 0.121*np.cos(np.radians(52.46-Long)))
 if (Lat<36) and (-36<Lat):
  Perf = Perf*0.621
 if Short>45:
  Perf = Perf*0.967
 
 Perf = Perf*smell_effects[Smell]
 Perf = Perf*taste_effects[Taste]
 Perf = Perf*feng_effects[Feng]
 
 for sound in sound_effects:
  if sound in SoundList:
   Perf = Perf*sound_effects[sound]
 
 Perf = Perf*(1-abs(3.15-Pi)/0.1)
 Perf = Perf*(1-0.004*Murph**3)
 
 PerfMean = Perf*100
 Perf = Perf*np.random.normal(100, 0.57)
 
 #List em
 
 Longs.append(round(Long,3))
 Lats.append(round(Lat,3))
 Shorts.append(round(Short,3))
 Delts.append(round(Delt,3))
 
 Smells.append(Smell)
 Tastes.append(Taste)
 Fengs.append(Feng)
 
 SoundLists.append(str(SoundList))
 
 Pis.append(round(Pi,4))
 Murphs.append(round(Murph,2))
 
 Perfs.append(str(round(Perf,3))+"%")
 PerfMeans.append(str(round(PerfMean,3))+"%")
 
for i in range(110809):
 gen_row()
 theDict[i]=float(Perfs[-1].split("%")[0])

df = pd.DataFrame({
 "Longitude":Longs,
 "Latitude":Lats,
 "Shortitude": Shorts,
 "Deltitude": Delts,
 
 "Strange Smell?": Smells,
 "Air Tastes Like": Tastes,
 "Feng Shui of Surrounding Area": Fengs,
 
 "Weird Sounds": SoundLists,
 
 "Local Value of Pi": Pis,
 "Murphy's Constant": Murphs,
 "ZPPG Performance": Perfs,
 "ZPPG Performance Mean": PerfMeans})

df.to_csv("deployment_data.csv")

print(theDict)