import os

from test_desktop import HCloudDesktopClicker
from strformat import StrFormat
from screen_scaler import *
from recheck import *


TARGET = "2支弄32号.xlsx"
LABELS = "./labels"

# create new folder
def create_new_folder(path: str) -> None:
    if not os.path.exists(f"./{path}"):
        os.mkdir(f"./{path}")

# pre-init
""" create_new_folder("labels")
w = StrFormat.query("Input the width of your screen(pixel):")
w = int(w)
set_positions(w) 
create_new_folder("post_labels")
"""


# instantiation
clicker = HCloudDesktopClicker(TARGET) \
        .click_to_serv()


for i, row in enumerate(clicker.data):
    name = row[1]
    img, clicker = clicker.click_to_reg() \
            .reg_main(row) \
            .save_screenshot()
    if clicker.check_qr_code(img):
        img.save(f"./labels/{i}_{name}.jpg")
        clicker.go_back().go_back()
        StrFormat.ok(f"Registration for {name} is successful!")
    else:
        clicker.go_back()
        StrFormat.warning(f"Registration for {name} failed because of duplication of registration!")

# post-processing
recheck(LABELS, clicker.data)
attch_addr(LABELS, clicker.data)
clear(LABELS)
StrFormat.ok("All done!")