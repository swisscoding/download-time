#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Calculate download time | ----\n", fg("red")))

# class
class DownloadTime:
    def __init__(self, size, speed):
        self.size = size
        self.speed = speed

    # output magic method
    def __repr__(self):
        time = stylize(self.calculate(self.size, self.speed), fg("red"))
        return f"\nDownloading a file of the size {self.size} megabytes with\n{self.speed} megabits/second takes {time} seconds.\n"

    # methods
    def calculate(self, fsize, dspeed):
        return fsize / (dspeed / 8)

# main execution
if __name__ == "__main__":
    # user interaction
    file_size = float(input("File size in megabytes: "))
    download_speed = float(input("Download speed in megabits/second: "))

    print(DownloadTime(file_size, download_speed))
