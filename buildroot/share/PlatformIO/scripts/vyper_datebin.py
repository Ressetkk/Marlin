#
# vyper_firmware_prepare.py
# Rename the binary file for Anycubic Vyper bootloader.
#

import pioutil
if pioutil.is_pio_build():
    from datetime import datetime
    Import("env")
    env['PROGNAME'] = datetime.now().strftime("main_board_%Y%m%d")