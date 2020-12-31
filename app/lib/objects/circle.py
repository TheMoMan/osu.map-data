from .hitObject import HitObject

class Circle(HitObject):
  def __init__(self, objectNumber, mapId, time, x, y, newCombo):
    super(Circle, self).__init__(objectNumber, mapId, time, x, y, newCombo)

  def toString(self):
    return 'objectNumber: {}, mapId: {}, time: {}, x: {}, y: {}, newCombo: {}'.format(self.objectNumber, self.mapId, self.time, self.x, self.y, self.newCombo)

  def toSqlRow(self):
    return (self.objectNumber, self.mapId, 'circle', self.time, self.x, self.y, self.newCombo)
