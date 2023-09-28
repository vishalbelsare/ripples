#!/usr/bin/env python

from conans import ConanFile, CMake, tools

class LibtrngConan(ConanFile):
    name = "libtrng"
    license = "BSD"
    version = "4.22"
    author = "Heiko Bauke"
    version= "basic_hip_support"
    description = "Tina's Random Number Generator Library"
    topics = ("Pseudo-Random Number Generator")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    def source(self):
        tools.download('https://github.com/rabauke/trng4/archive/refs/tags/v' + self.version + '.tar.gz', 'trng-' + self.version + '.tar.gz')
        tools.unzip('trng-' + self.version + '.tar.gz')
        tools.replace_in_file(
            'trng4-' + self.version + '/CMakeLists.txt',
            'add_subdirectory(examples)',
            ''
        )
        return 'trng4-' + self.version

    def build(self):
        cmake = CMake(self)
        cmake.definitions['TRNG_ENABLE_EXAMPLES'] = False
        cmake.definitions['TRNG_ENABLE_TESTS'] = False
        cmake.configure(source_folder='trng')
        cmake.parallel = False
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["trng4"]
