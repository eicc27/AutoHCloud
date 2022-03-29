import os

from test_desktop import HCloudDesktopClicker
from strformat import StrFormat
# instantiation
clicker = HCloudDesktopClicker() \
        .click_to_serv()

# create new folder
def create_new_folder(path: str) -> None:
    if not os.path.exists(f"./{path}"):
        os.mkdir(f"./{path}")

for i, row in enumerate(clicker.data):
    name = row[1]
    create_new_folder("labels")
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