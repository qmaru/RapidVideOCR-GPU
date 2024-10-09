# -*- encoding: utf-8 -*-
import os

import pytest

from rapid_videocr import RapidVideOCR, RapidVideOCRError, RapidVideoSubFinderOCR
from rapid_videocr.utils import read_txt

work_dir = os.path.dirname(os.path.abspath(__file__))
tests_dir = os.path.join(work_dir, "tests")

output_dir = os.path.join(tests_dir, "test_files", "outputs")
test_video = os.path.join(tests_dir, "test_files", "test.mp4")

vsf_exe = r"C:\Users\Lenovo\Downloads\VideoSubFinder_6.10_x64\Release_x64\VideoSubFinderWXW.exe"

vsf_results = os.path.join(output_dir, "test", "VSF_Results")
rgb_files = os.path.join(vsf_results, "RGBImages")
txt_files = os.path.join(vsf_results, "TXTImages")
sub_output = os.path.join(output_dir, "test")
srt_path = os.path.join(sub_output, "test.srt")
txt_path = os.path.join(sub_output, "test.txt")


# SubExportAndOCR
# vsf_exe: VideoSubFinderWXW.exe 的绝对路径
# video_path: 视频的路径或者目录
# save_dir: 输出的目录
def SubExportAndOCR(vsf_exe, video_path, save_dir):
    extractor = RapidVideoSubFinderOCR(vsf_exe_path=vsf_exe, is_concat_rec=True)
    extractor(video_path, save_dir)


# SubOnlyOCR
# img_dir: VideoSubFinderWXW 输出的 RGBImages / TXTImages 目录
# save_dir: 字幕输出的目录
# save_name: 字幕的文件名
def SubOnlyOCR(img_dir, save_dir, save_name, is_concat_rec=False):
    extractor = RapidVideOCR(is_concat_rec=is_concat_rec)
    with pytest.raises(RapidVideOCRError):
        extractor(img_dir, save_dir, save_name=save_name)
    pytest.raises(RapidVideOCRError)


def test_video_export_and_ocr():
    SubExportAndOCR(vsf_exe, test_video, output_dir)


@pytest.mark.parametrize(
    "img_dir",
    [
        rgb_files,
        txt_files,
    ],
)
def test_single_rec(img_dir):
    SubOnlyOCR(img_dir, sub_output, "test")

    srt_data = read_txt(srt_path)
    txt_data = read_txt(txt_path)

    if "RGBImages" in img_dir:
        print("RGBImages")

        assert len(srt_data) == 20
        assert srt_data[2] == "空间里面他绝对赢不了的"
        assert srt_data[-6] == "你们接着善后"

        assert len(txt_data) == 10
        assert txt_data[-4] == "你们接着善后"
    elif "TXTImages" in img_dir:
        print("TXTImages")

        assert len(srt_data) == 12
        assert srt_data[2] == "空间里面他绝对赢不了的"
        assert srt_data[-2] == "你们接着善后"

        assert len(txt_data) == 6
        assert txt_data[-2] == "你们接着善后"


@pytest.mark.parametrize(
    "img_dir",
    [
        rgb_files,
    ],
)
def test_concat_rec(img_dir):
    SubOnlyOCR(img_dir, sub_output, "test", True)

    srt_data = read_txt(srt_path)
    txt_data = read_txt(txt_path)

    assert len(srt_data) == 20
    assert srt_data[2] == "空间里面他绝对赢不了的"
    assert srt_data[-6] == "你们接着善后"

    assert len(txt_data) == 10
    assert txt_data[-4] == "你们接着善后"


@pytest.mark.parametrize(
    "img_dir",
    [
        rgb_files,
        txt_files,
    ],
)
def test_ocr_core(img_dir):
    SubOnlyOCR(img_dir, sub_output, "test", True)
