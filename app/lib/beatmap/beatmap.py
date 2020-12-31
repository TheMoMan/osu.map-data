class Beatmap(object):
  def __init__(self, mapId, mapsetId, mode, diffName, hpDrain, circleSize, overallDifficulty, approachRate, sliderMultiplier, sliderTickRate, stackLeniency):
    self.beatmapId = mapId
    self.beatmapSetId = mapsetId
    self.mode = mode
    self.diffName = diffName
    self.hpDrain = hpDrain
    self.circleSize = circleSize
    self.overallDifficulty = overallDifficulty
    self.approachRate = approachRate
    self.sliderMultiplier = sliderMultiplier
    self.sliderTickRate = sliderTickRate
    self.stackLeniency = stackLeniency
  
  def toSqlRow(self):
    return (self.mapId, self.mapsetId, self.mode, self.diffName, self.hpDrain, self.circleSize, self.overallDifficulty, self.approachRate, self.sliderMultiplier, self.sliderTickRate, self.stackLeniency)
