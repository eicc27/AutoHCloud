import time
import json
import pyautogui as pag
import pyperclip as pclip
from PIL import ImageGrab
from PIL import Image
import pyzbar.pyzbar as pyzbar

from strformat import StrFormat
import personal_info_reader

T = 1.3
T1 = 0.6

class HCloudDesktopClicker:
    """
    *Make sure the miniprogram is on the very left of the screen!*

    Clicks and inputs the information for registration.
    Refreshes every time when an input is complete.
    
    -----
    Utils: 
    
    pyautogui for clicking & sending keys
    
    pyperclip for copying and pasting

    pandas for reading xlsx

    pyzbar for recognizing QR code
    """

    def __init__(self, path: str) -> None:
        print("Please ensure that the miniprogram is open.")
        print("Please ensure that the miniprogram is on the very left of the screen.")
        print("Please ensure the miniprogram is visible.")
        print("You have 5 secs to prepare...")
        print("reading config...")
        self.config = self.read_conf("position.json") 
        StrFormat.info("reading data...")
        self.data = self.read_data(path)
        time.sleep(5)
        StrFormat.info("Starting...")
        
    @staticmethod
    def read_conf(path: str) -> dict:
        return json.load(open(path, 'r', encoding='utf-8'))
    
    @staticmethod
    def sleep_default(t=T) -> None:
        time.sleep(t)
    
    @staticmethod
    def read_data(path: str) -> list[list[str]]:
        return personal_info_reader.PersonalInfoReader(path).get_rows()

    @staticmethod
    def click_default(pos: list[int], t=T) -> None:
        pag.click(pos)
        HCloudDesktopClicker.sleep_default(t)
    
    @staticmethod
    def cpy_pst_default(content: str, t=T1) -> None:
        pclip.copy(content)
        pag.hotkey("ctrl", "v")
        HCloudDesktopClicker.sleep_default(t)

    def click_to_serv(self):
        self.click_default(self.config["serv"])
        return self
    
    def click_to_reg(self):
        self.click_default(self.config["reg"])
        return self
    
    def reg_main(self, row: list[str]):
        """
        *Ensure that the row is in id-name-addr-tel form!*
        """
        main = self.config["main"]
        id, name, addr, tel = row
        # firstly choose "non-self"
        self.click_default(main["non-self"])
        # then "id"
        self.click_default(main["id"])
        self.cpy_pst_default(id)
        self.click_default(main["name"])
        self.cpy_pst_default(name)
        self.click_default(main["addr"])
        self.cpy_pst_default(addr)
        self.click_default(main["tel"])
        self.cpy_pst_default("11111111111" if not tel else tel)
        self.click_default(main["job"]["self"])
        self.click_default(main["job"]["input"])
        self.cpy_pst_default("无")
        self.click_default(main["job"]["confirm"])
        self.click_default(main["eula"])
        self.click_default(main["forward"])
        time.sleep(5)
        return self
    
    def save_screenshot(self):
        '''
        *Make index number go first in `name`, like 22_chensihan.jpg.*
        '''
        # screenshot with PIL
        x, y = self.config["upleft"]
        w, h = self.config["downright"]
        img = ImageGrab.grab(bbox=(x, y, w, h))
        return img, self
    
    def go_back(self):
        '''
        If successful, after saving screenshot, call this function twice.
        Otherwise once.
        '''
        self.click_default(self.config["back"])
        return self
    
 
    @staticmethod
    def check_qr_code(img: Image.Image) ->bool:
        if not pyzbar.decode(img):
            return False
        return True





