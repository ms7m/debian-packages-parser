# Debian APT Repository Packages Parser

![Test Python Module](https://github.com/ms7m/debian-packages-parser/workflows/Test%20Python%20Module/badge.svg)  ![PythonVersion](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)  ![PythonVersion](https://img.shields.io/badge/Formatting-Black-black.svg)

***

> This only supports Python 3.

A simple pure-python module to parse RFC822-like Debain data formats.

This can include:

- Packages Files
- Control Files
- Sources
- Changes

***
## Installation

- Latest stable build from master (PyPi)
    -   ```
        pip install debian_packages_parser
         ```
- Latest development build
    - Use the provided ``.whl`` files.

***
## Usage

*Packages File*
```
Package: com.spark.aionwidgets.weather
Name: Weather Aion Widget
Depends: mobilesubstrate, com.spark.Aion
Architecture: iphoneos-arm
Description: Weather Aion widget
Maintainer: Spark
Author: Spark
Section: Aion Widgets
Version: 1.0.0
Installed-Size: 136
SHA256: 6dcb8858474a16b90098a5b5bcb083e9876993c9b6f82b4fbcbe80c012e07369
SHA1: 53cd05fabc299d03b667595a6477bb507f89b96e
MD5sum: 39541c71228533fcd02a29f380c9c598
Depiction: https://www.sparkdev.me/package/com.spark.aionwidgets.weather
SileoDepiction: https://www.sparkdev.me/sileo/com.spark.aionwidgets.weather
Size: 6784
Filename: download/com.spark.aionwidgets.weather/1.0.0.deb
Icon: https://sparkdev.me/package-logo/com.spark.aionwidgets.weather
Tag: purpose::extension

Package: com.spark.airdropconfirm
Name: AirDropConfirm
Depends: mobilesubstrate
Architecture: iphoneos-arm
Description: An awesome MobileSubstrate tweak!
Maintainer: Spark
Author: Spark
Section: Tweaks
Version: 1.0.0
Installed-Size: 200
SHA256: 77cae709321740627124780ef5633ec322c9ba85f2d76e5956c75d8d92f8417a
SHA1: 44af8ad9d78874702772a158b199aaedb8314fb4
MD5sum: 7c9772f33ca571b8512f842100ceb6da
Depiction: https://www.sparkdev.me/package/com.spark.airdropconfirm
SileoDepiction: https://www.sparkdev.me/sileo/com.spark.airdropconfirm
Size: 8760
Filename: download/com.spark.airdropconfirm/1.0.0.deb
Icon: https://sparkdev.me/package-logo/com.spark.airdropconfirm
Tag: purpose::extension
```



*Code*
```python
from debian_package_parse import PackagesParser

sample_packages_file = open("Packages", "r").read()

parser = PackagesParser(sample_pacakges_file)
data = parser.parse()
```

```json
[
    [
        {
            "tag": "Package",
            "value": "com.spark.aionwidgets.weather"
        },
        {
            "tag": "Name",
            "value": "Weather Aion Widget"
        },
        {
            "tag": "Depends",
            "value": "mobilesubstrate, com.spark.Aion"
        },
        {
            "tag": "Architecture",
            "value": "iphoneos-arm"
        },
        {
            "tag": "Description",
            "value": "Weather Aion widget"
        },
        {
            "tag": "Maintainer",
            "value": "Spark"
        },
        {
            "tag": "Author",
            "value": "Spark"
        },
        {
            "tag": "Section",
            "value": "Aion Widgets"
        },
        {
            "tag": "Version",
            "value": "1.0.0"
        },
        {
            "tag": "Installed-Size",
            "value": "136"
        },
        {
            "tag": "SHA256",
            "value": "6dcb8858474a16b90098a5b5bcb083e9876993c9b6f82b4fbcbe80c012e07369"
        },
        {
            "tag": "SHA1",
            "value": "53cd05fabc299d03b667595a6477bb507f89b96e"
        },
        {
            "tag": "MD5sum",
            "value": "39541c71228533fcd02a29f380c9c598"
        },
        {
            "tag": "Depiction",
            "value": "https://www.sparkdev.me/package/com.spark.aionwidgets.weather"
        },
        {
            "tag": "SileoDepiction",
            "value": "https://www.sparkdev.me/sileo/com.spark.aionwidgets.weather"
        },
        {
            "tag": "Size",
            "value": "6784"
        },
        {
            "tag": "Filename",
            "value": "download/com.spark.aionwidgets.weather/1.0.0.deb"
        },
        {
            "tag": "Icon",
            "value": "https://sparkdev.me/package-logo/com.spark.aionwidgets.weather"
        },
        {
            "tag": "Tag",
            "value": "purpose::extension"
        }
    ],
    [
        {
            "tag": "Package",
            "value": "com.spark.airdropconfirm"
        },
        {
            "tag": "Name",
            "value": "AirDropConfirm"
        },
        {
            "tag": "Depends",
            "value": "mobilesubstrate"
        },
        {
            "tag": "Architecture",
            "value": "iphoneos-arm"
        },
        {
            "tag": "Description",
            "value": "An awesome MobileSubstrate tweak!"
        },
        {
            "tag": "Maintainer",
            "value": "Spark"
        },
        {
            "tag": "Author",
            "value": "Spark"
        },
        {
            "tag": "Section",
            "value": "Tweaks"
        },
        {
            "tag": "Version",
            "value": "1.0.0"
        },
        {
            "tag": "Installed-Size",
            "value": "200"
        },
        {
            "tag": "SHA256",
            "value": "77cae709321740627124780ef5633ec322c9ba85f2d76e5956c75d8d92f8417a"
        },
        {
            "tag": "SHA1",
            "value": "44af8ad9d78874702772a158b199aaedb8314fb4"
        },
        {
            "tag": "MD5sum",
            "value": "7c9772f33ca571b8512f842100ceb6da"
        },
        {
            "tag": "Depiction",
            "value": "https://www.sparkdev.me/package/com.spark.airdropconfirm"
        },
        {
            "tag": "SileoDepiction",
            "value": "https://www.sparkdev.me/sileo/com.spark.airdropconfirm"
        },
        {
            "tag": "Size",
            "value": "8760"
        },
        {
            "tag": "Filename",
            "value": "download/com.spark.airdropconfirm/1.0.0.deb"
        },
        {
            "tag": "Icon",
            "value": "https://sparkdev.me/package-logo/com.spark.airdropconfirm"
        },
        {
            "tag": "Tag",
            "value": "purpose::extension"
        }
    ]
]

```


***
## Should I use This?

It depends, if you need an a simple module to *read* and act upon RFC822-like Debain data formats, this might be a good alternative as compared to ``python-debian`` pacakge. 

If you need manuiplate the data, or need more extensibility. It's probably best not to use this.

This module will **not** "verify" if the file provided is valid. Meaning it can fail catastrophically if invalid. Please ensure verification of the data before.. 
***

## Development

All PRs are welcome. **Please remember to use black formatting when opening**.
