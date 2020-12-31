from .hitObject import HitObject

class Spinner(HitObject):
  def __init__(self, objectNumber, mapId, time, x, y, length: int):
    super(Spinner, self).__init__(objectNumber, mapId, time, x, y)
    self.length = length

  def toString(self):
    return 'objectNumber: {}, mapId: {}, time: {}, x: {}, y: {}, length: {}'.format(self.objectNumber, self.mapId, self.time, self.x, self.y, self.length)

  def toSqlRow(self):
    return (self.objectNumber, self.mapId, 'spinner', self.time, self.x, self.y, self.length)