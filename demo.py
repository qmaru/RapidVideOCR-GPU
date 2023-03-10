# -*- encoding: utf-8 -*-
# @Author: SWHL
# @Contact: liekkaskono@163.com

from rapid_videocr import RapidVideOCR

extractor = RapidVideOCR(is_single_res=True)

import time

s = time.time()
rgb_dir = 'tests/test_files/RGBImage'
save_dir = 'result'
extractor(rgb_dir, save_dir)

elapse = time.time() - s
print(elapse)
