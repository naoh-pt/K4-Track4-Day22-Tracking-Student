# Đối chiếu checkpoint bài lab

Ngày kiểm tra: 08/10/2026. Đối chiếu theo các bước C–F và mục “Nộp bài” trong [HUONG_DAN.md](../HUONG_DAN.md); repo không có một bảng CP được đánh số riêng.

## Kết quả

| Yêu cầu | Trạng thái sau bổ sung | Minh chứng |
|---|---|---|
| C: môi trường Python 3.11 và thư viện lab | Hoàn thành | Dùng override NumPy/OpenCV/setuptools để giữ BoxMOT `10.0.42`; phiên bản kiểm chứng trong `minh_chung/phien_ban.json` |
| C: dữ liệu đủ 5 video, chỉ video_1 có nhãn | Đạt | 600 / 1.050 / 837 / 900 / 750 ảnh; `check_data.py` báo OK cả 5 |
| Ôn metric: điền và chạy câu hỏi | Đạt | [Notebook đã chạy](minh_chung/on_tap_metrics_da_chay.ipynb): cả 3 câu đúng |
| YOLO trên một ảnh và đổi conf | Đạt | Notebook lưu ảnh và 14 / 6 / 5 hộp với conf 0,15 / 0,30 / 0,50 |
| D: baseline ByteTrack 150 frame | Đạt | [Preview baseline](../runs/thu_nhanh/video_1_preview.mp4), `runs/thu_nhanh/video_1.txt` |
| E: ít nhất hai tracker cho mỗi video | Đạt | ByteTrack và BoTSORT ở conf 0,30, iou 0,50 trên 80 frame đầu của từng video |
| E: thử ngưỡng, mỗi lần đổi một số | Đạt | [30 lượt thử](THU_NGHIEM_BO_SUNG.md): conf 0,15 / 0,30 / 0,50; iou 0,40 / 0,50 / 0,70 |
| E: đủ 5 file nộp, đúng định dạng | Đạt | Mỗi dòng 10 cột hữu hạn, frame/ID nguyên dương, hộp có kích thước dương, confidence trong [0,1], ba cột cuối -1; không trùng cặp frame–ID |
| E: kết quả đến hết chuỗi | Đạt | Cả 5 file có kết quả ở mọi frame, từ 1 đến 600 / 1.050 / 837 / 900 / 750 |
| F: chấm chỉ video_1 | Đạt | HOTA 26,912; MOTA 17,292; IDF1 25,713; [kết quả TrackEval](minh_chung/video_1_summary.txt) |
| F: báo cáo cấu hình, lý do và quan sát | Đạt | [Báo cáo](BAO_CAO_mau.md) đủ 5 video; có phân tích từng cảnh và trường hợp phân mảnh sau che khuất ở video_4 |
| Bộ kiểm tra không dùng GPU, ảnh lab hay mạng | Đạt | 13 unit test đạt; có kiểm tra từ chối chấm video_2–video_5 |

## Các phần đã bổ sung

- Sửa hướng dẫn cài đặt do BoxMOT ghim NumPy không tương thích Python 3.11/OpenCV; bổ sung thư viện notebook.
- Tạo `lab_data/video_1/eval_config.json` còn thiếu từ [cấu hình lab](eval_config.json), chấm lại và lưu kết quả gốc.
- Chạy và lưu output của cả 4 ô code trong notebook.
- Chạy baseline và 30 lượt thử ngắn; bổ sung phần thử iou chưa có minh chứng trước đó.
- Dựng lại preview đầy đủ từ các file MOT đã nộp và ảnh đầu vào; kiểm tra số frame của từng preview.
- Làm rõ đoạn người áo đỏ ở video_4: ID 2 kết thúc tại frame 709, ID 93 bắt đầu tại frame 759 sau đoạn che khuất/mất hộp.
- Sửa thư mục chuẩn bị chấm để tôn trọng `split` trong cấu hình; thêm unit test.

## Bài nộp và chạy lại

Bài nộp gồm năm file trong [runs/nop_bai](../runs/nop_bai/) và [BAO_CAO_mau.md](BAO_CAO_mau.md). Các preview và trọng số nằm tại máy, được Git bỏ qua. Minh chứng thống kê có thể lưu cùng báo cáo tại [minh_chung/](minh_chung/).

Trong PowerShell tại repo root, dùng Python của env `cv_robotics_lab21`:

```powershell
conda activate cv_robotics_lab21
$env:LAB_DATA = (Resolve-Path lab_data).Path
$env:PYTHONIOENCODING = "utf-8"
python -m pytest
python scripts/check_data.py --lab-data-root "$env:LAB_DATA"
python scripts/evaluate_practice.py --trackeval-root TrackEval --lab-data-root "$env:LAB_DATA" --submission runs/nop_bai/video_1.txt --run-name TH001_kiem_tra
```

Trong VS Code, chọn kernel **Python 3.11 (Tracking lab)** (`cv_robotics_lab21`) cho `on_tap_metrics.ipynb`. Kernel `base` trên máy chưa có thư viện notebook/lab. Bản lưu riêng trong `minh_chung/on_tap_metrics_da_chay.ipynb` giữ toàn bộ kết quả đã chạy thành công.

Các checkpoint kỹ thuật và nội dung nộp trong repo đã đủ. Phần thảo luận trực tiếp với giảng viên và việc gửi bài lên hệ thống lớp là hoạt động ngoài repo, chưa được xác nhận ở đây. Điểm tracking còn thấp do bỏ sót người; đạt đủ yêu cầu nộp không đồng nghĩa chất lượng tracking tối ưu.
