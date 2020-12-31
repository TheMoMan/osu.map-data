from .hitObject import HitObject
from .sliderAnchor import SliderAnchor

class Slider(HitObject):
  def __init__(self, objectNumber, mapId, time, x, y, newCombo, anchors: list, length: float, curveType: str, slides: int):
    super().__init__(objectNumber, mapId, time, x, y, newCombo)
    self.anchors = anchors
    self.length = length
    self.curveType = curveType
    self.slides = slides

  def toString(self):
    return 'objectNumber: {}, mapId: {}, time: {}, x: {}, y: {}, newCombo: {}, length: {}, anchors: {}, curveType: {}, slides: {}'.format(self.objectNumber, self.mapId, self.time, self.x, self.y, self.newCombo, self.length, self.anchors, self.curveType, self.slides)

  def toSqlRow(self):
    return (self.objectNumber, self.mapId, 'slider', self.time, self.x, self.y, '|'.join(self.anchors.toSqlField()), self.length, self.curveType, self.slides, self.newCombo)
