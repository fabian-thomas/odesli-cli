import argparse

from odesli import Odesli
from odesli import Song

parser = argparse.ArgumentParser(description='TODO.')
parser.add_argument('url', metavar='url', type=str,
                    help='an url to some music content (e.g. song or album)')
parser.add_argument('--provider', metavar='provider', type=str,
                    help='the api provider to use data of (default: provider used for the query)')
parser.add_argument('property', metavar='property', type=str,
                    choices=['artistName', 'id', 'link', 'thumbnailUrl', 'thumbnailWidth', 'thumbnailHeight', 'title', 'type'],
                    help='property')
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
    if isinstance(entity, Song.Song):
        print('song');
    # elif isinstance(entity, Album.Album):
    #     print('album')
else:
    print(getattr(entity, args.property))
