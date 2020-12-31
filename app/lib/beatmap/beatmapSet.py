class BeatmapSet(object):
  def __init__(self, mapsetId, title, titleUnicode, artist, artistUnicode, creator, source, tags):
    self.beatmapSetId = mapsetId
    self.title = title
    self.titleUnicode = titleUnicode
    self.artist = artist
    self.artistUnicode = artistUnicode
    self.creator = creator
    self.source = source
    self.tags = tags

  def toSqlRow(self):
    return (self.mapsetId, self.title, self.titleUnicode, self.artist, self.artistUnicode, self.creator, self.source, self.tags)
