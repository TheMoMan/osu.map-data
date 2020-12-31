class SliderAnchor(object):
  def __init__(self, x, y, linear = False):
    self.x = x
    self.y = y
    self.linear = linear

  def toString(self):
    return 'x: {}, y: {}, linear: {}'.format(self.x, self.y, self.linear)
  
  def toSqlField(self):
    return '{},{},{}'.format(self.x, self.y, self.linear)
