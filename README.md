# File Downloader
A helper to download files from urls, support protocols: HTTP, FTP.
# Installation
Requires:
- Python >= 3.6

Install using pip: it is best to install in a python virtual environment.

```
cd path/to/project
source venv/bin/activae
pip install .
```

# Usage

```
>> download --help

Usage: download [OPTIONS]

  File Downloader: a helper to download files from urls,  support protocols:
  HTTP, FTP

Options:
  -s, --source TEXT      A text file contain urls to be downloaded, separated
                         by newline  [required]

  -d, --dest TEXT        Destination folder  [required]
  -r, --refresh BOOLEAN  Re-download if file exists  [default: False]
  --help                 Show this message and exit.

```

Example:
```
cd path/to/project
download -s sample_source.txt -d tests/data
```

# Architecture
There 3 main packages:
- `agoda.downloader`: the core package.
- `agoda.log`: to support logging.
- `agoda.cli`: to support command line.

The main entry is the `Download` class which will prepare the urls (source) to be downloaded, file paths (destination) to be saved to, parallel processing and exception handling.
```
dest_path = 'tests/data'
download = Download(dest_path)
dest_file = download.download(`https://www.facebook.com/favicon.ico`)
print(dest_file)
```
You could download multiple urls in parallel using `download.download_urls(urls)`. It is IO bound tasks, so we use threads instead of processes here.

The core package `agoda.downloader` is implemented using the factory design pattern, the `DownloaderFactory` will decide which downloader (`FTPDownloader`, `HTTPDownloader`,...) to use, depending on the url's protocol.

The `DownloaderIF` is the main interface, which makes the code extendable by implementing downloader for different protocols: `FTPDownloader`, `HTTPDownloader`, `SFTPDownloader`,...
After implementing a new downloader (e.g `SFTPDownloader`), we will add it to the `DownloaderFactory`.

Handled exceptions are listed in `agoda.downloader.exceptions` package.


# Development
Install virtual environment:

```
cd path/to/project
virtualenv -p python3.6 venv
source venv/bin/activate
pip install -r requirements.txt
```

Config IDE (e.g PyCharm) to use the virtual environment `venv`: Go to File > Settings > Project Interpreter

# Test
Run unit tests in `tests/` folder:

```
python -m unittest
```

# Contributors
- Diep Dao (diepdaocs@gmail.com)