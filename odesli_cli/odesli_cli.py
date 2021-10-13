import argparse

from odesli.Odesli import Odesli
from odesli.song.Song import Song

INDENTATION_WIDTH = 4
PROPERTIES = ['all', 'artistName', 'id', 'link', 'thumbnailUrl', 'thumbnailWidth', 'thumbnailHeight', 'title', 'type']

def indentString(level, s):
    return ' '*INDENTATION_WIDTH*level+s

def getType(entity):
    if isinstance(entity, Song):
        return 'song'
    # elif isinstance(entity, Album.Album):
        # return 'album'

def main():
    parser = argparse.ArgumentParser(description='TODO.')
    parser.add_argument('url', metavar='url', type=str,
                        help='an url to some music content (e.g. song or album)')
    parser.add_argument('--provider', metavar='provider', type=str,
                        help='the api provider to use data of (default: provider used for the query)')
    parser.add_argument('property', metavar='property', type=str,
                        choices=PROPERTIES,
                        help='The property to output. Must be one of: '+', '.join(PROPERTIES))
    parser.add_argument('--platform', metavar='platform', type=str,
                        help='platform to print the link of (default: first link in list)')
    args = parser.parse_args()

    odesli = Odesli()
    entity = odesli.getByUrl(args.url)

    # use specified api provider for printing the data
    if args.provider == None:
        entity = entity.song
    else:
        entity = entity.songsByProvider[args.provider]

    # print out requested properties
    if args.property == 'link':
        if args.platform == None:
            # get first link if no platform specified
            print(next(iter(entity.linksByPlatform.values())))
        else:
            print(entity.linksByPlatform[args.platform])
    elif args.property == 'type':
        print(getType(entity))
    elif args.property == 'all':
        formatString = "{:<20}"*2
        print(formatString.format('id:', entity.id))
        print(formatString.format('type:', getType(entity)))
        print(formatString.format('title:', entity.title))
        print(formatString.format('artistName:', entity.artistName))
        print(formatString.format('thumbnailUrl:', entity.thumbnailUrl))
        print(formatString.format('thumbnailWidth:', entity.thumbnailWidth))
        print(formatString.format('thumbnailHeight:', entity.thumbnailHeight))
        print(formatString.format('provider:', entity.provider))
        print('links:')
        for platform in entity.linksByPlatform:
            print(formatString.format(indentString(1, platform)+':', entity.linksByPlatform[platform]))
    else:
        print(getattr(entity, args.property))
