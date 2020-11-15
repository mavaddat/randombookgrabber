from calibre.customize import FileTypePlugin
import os


class RandomBookGrabber(FileTypePlugin):

    name = 'Random Book Grabber'  # Name of the plugin
    description = 'Options to get a random book, randomize sort'
    supported_platforms = ['windows', 'osx', 'linux']  # Platforms this plugin
    # will run on
    author = 'Mav Jav Education'  # The author of this plugin
    version = (1, 0, 0)   # The version number of this plugin
    file_types = set(
        ['epub', 'mobi', 'txt', 'pdf', 'doc', 'docx']
        )  # File types this plugin will be applied to
    on_postprocess = True  # Run this plugin after conversion is complete
    minimum_calibre_version = (5, 1, 0)

    def run(self, path_to_ebook):
        from calibre.ebooks.metadata.meta import get_metadata, set_metadata
        file = open(path_to_ebook, 'r+b')
        ext = os.path.splitext(path_to_ebook)[-1][1:].lower()
        mi = get_metadata(file, ext)
        mi.publisher = 'Hello World'
        set_metadata(file, mi, ext)
        return path_to_ebook
