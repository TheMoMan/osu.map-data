from app import utils

sliderCurveTypes = {
  'B' : 'bezier',
  'C' : 'catmull',
  'L' : 'linear',
  'P' : 'circle',
}

def getMetadataValue(beatmapLines: [str], field: str):
  return utils.getRightOfColon(utils.getElementFromPartial(beatmapLines, field))

def parseMapsetData(beatmapLines: [str]):
  beatmapSetId = getMetadataValue(beatmapLines, 'BeatmapSetID')
  title = getMetadataValue(beatmapLines, 'Title')
  titleUnicode = getMetadataValue(beatmapLines, 'TitleUnicode')
  artist = getMetadataValue(beatmapLines, 'Artist')
  artistUnicode = getMetadataValue(beatmapLines, 'ArtistUnicode')
  creator = getMetadataValue(beatmapLines, 'Creator')
  source = getMetadataValue(beatmapLines, 'Source')
  tags = getMetadataValue(beatmapLines, 'Tags')

  return (beatmapSetId, title, titleUnicode, artist, artistUnicode, creator, source, tags)

def parseMapData(beatmapLines: [str]):
  beatmapId = getMetadataValue(beatmapLines, 'BeatmapID')
  beatmapSetId = getMetadataValue(beatmapLines, 'BeatmapSetID')
  mode = getMetadataValue(beatmapLines, 'Mode')
  version = getMetadataValue(beatmapLines, 'Version')
  hpDrain = getMetadataValue(beatmapLines, 'HPDrainRate')
  circleSize = getMetadataValue(beatmapLines, 'CircleSize')
  overallDifficulty = getMetadataValue(beatmapLines, 'OverallDifficulty')
  approachRate = getMetadataValue(beatmapLines, 'ApproachRate')
  sliderMultiplier = getMetadataValue(beatmapLines, 'SliderMultiplier')
  sliderTickRate = getMetadataValue(beatmapLines, 'SliderTickRate')
  stackLeniency = getMetadataValue(beatmapLines, 'StackLeniency')

  return (beatmapId, beatmapSetId, mode, version, hpDrain, circleSize, overallDifficulty, approachRate, sliderMultiplier, sliderTickRate, stackLeniency)

def getMode(beatmapLines: [str]):
  return getMetadataValue(beatmapLines, 'Mode')

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
