import hashlib
from app import utils

sliderCurveTypes = {
  'B' : 'bezier',
  'C' : 'catmull',
  'L' : 'linear',
  'P' : 'circle',
}

def getMetadataValue(beatmapLines: [str], field: str):
  return utils.getRightOfColon(utils.getElementFromPartial(beatmapLines, field))

def hashMetadata(beatmapLines: [str]):
  # Old .osu formats don't stop beatmapSetId, so when this happens
  # we use the hash of artist + title + creator as a substitute.
  # Note this creates inaccuracies if a creator has two mapsets with the same artist + title.

  artist = getMetadataValue(beatmapLines, 'Artist')
  title = getMetadataValue(beatmapLines, 'Title')
  creator = getMetadataValue(beatmapLines, 'Creator')

  a = artist + title + creator;

  return hashlib.md5(a.encode()).hexdigest()

def parseMapsetData(beatmapLines: [str]):
  title = getMetadataValue(beatmapLines, 'Title')
  titleUnicode = getMetadataValue(beatmapLines, 'TitleUnicode')
  artist = getMetadataValue(beatmapLines, 'Artist')
  artistUnicode = getMetadataValue(beatmapLines, 'ArtistUnicode')
  creator = getMetadataValue(beatmapLines, 'Creator')
  source = getMetadataValue(beatmapLines, 'Source')
  tags = getMetadataValue(beatmapLines, 'Tags')

  beatmapSetId = getMetadataValue(beatmapLines, 'BeatmapSetID')
  if str(beatmapSetId) in ['', '-1']:
    beatmapSetId = hashMetadata(beatmapLines)

  return (beatmapSetId, title, titleUnicode, artist, artistUnicode, creator, source, tags)

def parseMapData(beatmapLines: [str], fileName: str):
  # Old .osu formats don't store beatmapId, take it from file name instead.
  # Means we can only use data from data.ppy.sh though.
  beatmapId = utils.getFileNameNoExt(fileName)

  mode = getMetadataValue(beatmapLines, 'Mode')
  version = getMetadataValue(beatmapLines, 'Version')
  hpDrain = getMetadataValue(beatmapLines, 'HPDrainRate')
  circleSize = getMetadataValue(beatmapLines, 'CircleSize')
  overallDifficulty = getMetadataValue(beatmapLines, 'OverallDifficulty')
  approachRate = getMetadataValue(beatmapLines, 'ApproachRate')
  sliderMultiplier = getMetadataValue(beatmapLines, 'SliderMultiplier')
  sliderTickRate = getMetadataValue(beatmapLines, 'SliderTickRate')
  stackLeniency = getMetadataValue(beatmapLines, 'StackLeniency')

  beatmapSetId = getMetadataValue(beatmapLines, 'BeatmapSetID')
  if str(beatmapSetId) in ['', '-1']:
    beatmapSetId = hashMetadata(beatmapLines)

  return (beatmapId, beatmapSetId, mode, version, hpDrain, circleSize, overallDifficulty, approachRate, sliderMultiplier, sliderTickRate, stackLeniency)

def getMode(beatmapLines: [str]):
  return getMetadataValue(beatmapLines, 'Mode') or '0'

def getObjectType(objectProps: [str]):
  objectTypeBin = '{0:07b}'.format(int(objectProps[3]))

  objectType = 'circle' if objectTypeBin[6] == '1' else 'slider' if objectTypeBin[5] == '1' else 'spinner' if objectTypeBin[3] == '1' else '?'
  newCombo = '1' if objectTypeBin[4] == '1' else '0'

  return (objectType, newCombo)

def parseSliderAnchors(anchors: str):
  curveType = sliderCurveTypes[anchors[0]]

  return (curveType, anchors[2:])

def parseObject(objectLine: str, objectNumber: int, beatmapId: int):
  objectProps = objectLine.split(',')
  objectType = getObjectType(objectProps)

  if objectType[0] == 'circle':
    # x,y,time,type,hitSound,objectParams,hitSample

    return (objectNumber, beatmapId, 'circle', objectProps[2], objectProps[0], objectProps[1], objectType[1])

  elif objectType[0] == 'slider':
    # x,y,time,type,hitSound,curveType|curvePoints,slides,length,edgeSounds,edgeSets,hitSample

    anchorProps = parseSliderAnchors(objectProps[5])

    return (objectNumber, beatmapId, 'slider', objectProps[2], objectProps[0], objectProps[1], objectType[1], anchorProps[1], objectProps[7], anchorProps[0], objectProps[6])
  
  elif objectType[0] == 'spinner':
    # x,y,time,type,hitSound,endTime,hitSample

    spinnerLength = str(int(objectProps[5]) - int(objectProps[2]))

    return (objectNumber, beatmapId, 'spinner', objectProps[2], objectProps[0], objectProps[1], objectType[1], spinnerLength)
