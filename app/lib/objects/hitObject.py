import abc

class HitObject(object):
  def __init__(self, objectNumber: int, mapId: int, time: int, x: int, y: int, newCombo: int):
    self.objectNumber = objectNumber
    self.mapId = mapId
    self.time = time
    self.x = x
    self.y = y
    self.newCombo = True if newCombo == 1 else False

  @abc.abstractmethod
  def toString(self):
    pass

  @abc.abstractmethod
  def toSqlRow(self):
    pass
