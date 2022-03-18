from conans import ConanFile, CMake, tools
import os

class TinyformatConan(ConanFile):
    name = "tinyformat"
    description = "A minimal type safe printf() replacement"
    topics = ("format", "printf")
    homepage = "https://github.com/c42f/tinyformat"
    license = "Boost Software License - Version 1.0. http://www.boost.org/LICENSE_1_0.txt"
    author = "stgatilov <stgatilov@gmail.com>"
    url = "https://github.com/stgatilov/conan-tinyformat"

    def source(self):
        # Download and extract tag tarball from github
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = "tinyformat-" + self.version
        os.rename(extracted_dir, "sources");

    def package(self):
        self.copy("tinyformat.h", dst="include", src=self.source_folder+"/sources")
        # extract license from header
        tmp = tools.load(self.source_folder + "/sources/tinyformat.h")
        license_contents = tmp[0:tmp.find("\n\n", 1)]
        license_contents = '\n'.join(line[3:] for line in license_contents.splitlines()) + '\n'
        tools.save("LICENSE.txt", license_contents)
        self.copy("*LICENSE.txt", dst="licenses", keep_path=False)

    def package_id(self):
        self.info.header_only()
