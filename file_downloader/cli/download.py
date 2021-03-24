import argparse
import os

import click

from file_downloader.downloader.download import Download
from file_downloader.log.log import setup_logging


@click.command('file-downloader',
               help='File Downloader: a helper to download files from urls, \nsupport protocols: HTTP, FTP')
@click.option('--source', '-s', help='A text file contain urls to be downloaded, separate by newline', required=True)
@click.option('--dest', '-d', help='Destination folder', required=True)
@click.option('--refresh', '-r', help='Re-download if file exists', type=bool, default=False, show_default=True)
def file_downloader(source, dest, refresh):
    download_urls(source, dest, refresh)


def download_urls(source_path, dest_path, refresh):
    if not os.path.exists(source_path):
        print('Source file does not exist!!!', source_path)
        exit()

    if not os.path.exists(dest_path):
        print('Destination folder does not exist!!!', dest_path)
        exit()

    setup_logging()
    with open(source_path, 'r') as f:
        urls = [url.strip() for url in f.readlines()]

    download = Download(dest_path)
    download.download_urls(urls, refresh)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='File Downloader: a helper to download files from urls, support protocol: HTTP, FTP')
    parser.add_argument('--source', '-s', dest='source',
                        help='A text file contain urls to be downloaded, separated by newline', required=True)
    parser.add_argument('--dest', '-d', dest='dest', help='Destination folder', required=True)
    parser.add_argument('--refresh', '-r', dest='refresh', help='Re-download if file exists', type=bool, default=False)
    args = parser.parse_args()
    download_urls(args.source, args.dest, args.refresh)
