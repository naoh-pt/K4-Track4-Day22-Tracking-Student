# Minh chứng thử tracker và ngưỡng

Ngày chạy: 08/10/2026. Mỗi lượt dùng đúng 80 frame đầu; detector `yolo26n.pt`, ảnh 640 px, lớp người; BoTSORT dùng `osnet_x0_25_msmt17.pt`. Bộ thư viện ở [phien_ban.json](minh_chung/phien_ban.json).

So sánh tracker tại cùng conf=0,30 và iou=0,50. Sau đó giữ tracker để quét conf ở iou=0,50; giữ conf đã chọn để quét iou. Các cấu hình còn lại của tracker dùng mặc định của BoxMOT 10.0.42. Hộp detector cho hai tracker tại cùng conf/iou được tính một lần và dùng lại để so sánh cùng đầu vào.

Số dòng, số ID và số track xuất hiện ít nhất 40 frame là thống kê đầu ra, không phải điểm chất lượng. Preview được lưu tại máy trong `runs/thu_bo_sung/`; Git không lưu preview hoặc trọng số.

| Video | Tracker | conf | iou | Dòng MOT | ID | Track ≥40 frame | Preview |
|---|---|---:|---:|---:|---:|---:|---|
| video_1 | bytetrack | 0.30 | 0.50 | 380 | 7 | 5 | [Xem](../runs/thu_bo_sung/video_1_bytetrack_conf0.30_iou0.50/video_1_preview.mp4) |
| video_1 | botsort | 0.30 | 0.50 | 441 | 11 | 6 | [Xem](../runs/thu_bo_sung/video_1_botsort_conf0.30_iou0.50/video_1_preview.mp4) |
| video_1 | bytetrack | 0.15 | 0.50 | 386 | 7 | 5 | [Xem](../runs/thu_bo_sung/video_1_bytetrack_conf0.15_iou0.50/video_1_preview.mp4) |
| video_1 | bytetrack | 0.50 | 0.50 | 330 | 8 | 4 | [Xem](../runs/thu_bo_sung/video_1_bytetrack_conf0.50_iou0.50/video_1_preview.mp4) |
| video_1 | bytetrack | 0.30 | 0.40 | 380 | 7 | 5 | [Xem](../runs/thu_bo_sung/video_1_bytetrack_conf0.30_iou0.40/video_1_preview.mp4) |
| video_1 | bytetrack | 0.30 | 0.70 | 380 | 7 | 5 | [Xem](../runs/thu_bo_sung/video_1_bytetrack_conf0.30_iou0.70/video_1_preview.mp4) |
| video_2 | bytetrack | 0.30 | 0.50 | 682 | 14 | 8 | [Xem](../runs/thu_bo_sung/video_2_bytetrack_conf0.30_iou0.50/video_2_preview.mp4) |
| video_2 | botsort | 0.30 | 0.50 | 857 | 18 | 10 | [Xem](../runs/thu_bo_sung/video_2_botsort_conf0.30_iou0.50/video_2_preview.mp4) |
| video_2 | bytetrack | 0.15 | 0.50 | 743 | 12 | 10 | [Xem](../runs/thu_bo_sung/video_2_bytetrack_conf0.15_iou0.50/video_2_preview.mp4) |
| video_2 | bytetrack | 0.50 | 0.50 | 586 | 14 | 7 | [Xem](../runs/thu_bo_sung/video_2_bytetrack_conf0.50_iou0.50/video_2_preview.mp4) |
| video_2 | bytetrack | 0.15 | 0.40 | 741 | 12 | 10 | [Xem](../runs/thu_bo_sung/video_2_bytetrack_conf0.15_iou0.40/video_2_preview.mp4) |
| video_2 | bytetrack | 0.15 | 0.70 | 761 | 12 | 10 | [Xem](../runs/thu_bo_sung/video_2_bytetrack_conf0.15_iou0.70/video_2_preview.mp4) |
| video_3 | bytetrack | 0.30 | 0.50 | 301 | 15 | 3 | [Xem](../runs/thu_bo_sung/video_3_bytetrack_conf0.30_iou0.50/video_3_preview.mp4) |
| video_3 | botsort | 0.30 | 0.50 | 392 | 16 | 3 | [Xem](../runs/thu_bo_sung/video_3_botsort_conf0.30_iou0.50/video_3_preview.mp4) |
| video_3 | botsort | 0.15 | 0.50 | 406 | 14 | 3 | [Xem](../runs/thu_bo_sung/video_3_botsort_conf0.15_iou0.50/video_3_preview.mp4) |
| video_3 | botsort | 0.50 | 0.50 | 294 | 14 | 3 | [Xem](../runs/thu_bo_sung/video_3_botsort_conf0.50_iou0.50/video_3_preview.mp4) |
| video_3 | botsort | 0.15 | 0.40 | 406 | 14 | 3 | [Xem](../runs/thu_bo_sung/video_3_botsort_conf0.15_iou0.40/video_3_preview.mp4) |
| video_3 | botsort | 0.15 | 0.70 | 459 | 15 | 3 | [Xem](../runs/thu_bo_sung/video_3_botsort_conf0.15_iou0.70/video_3_preview.mp4) |
| video_4 | bytetrack | 0.30 | 0.50 | 419 | 11 | 4 | [Xem](../runs/thu_bo_sung/video_4_bytetrack_conf0.30_iou0.50/video_4_preview.mp4) |
| video_4 | botsort | 0.30 | 0.50 | 509 | 13 | 6 | [Xem](../runs/thu_bo_sung/video_4_botsort_conf0.30_iou0.50/video_4_preview.mp4) |
| video_4 | botsort | 0.15 | 0.50 | 547 | 12 | 6 | [Xem](../runs/thu_bo_sung/video_4_botsort_conf0.15_iou0.50/video_4_preview.mp4) |
| video_4 | botsort | 0.50 | 0.50 | 402 | 10 | 4 | [Xem](../runs/thu_bo_sung/video_4_botsort_conf0.50_iou0.50/video_4_preview.mp4) |
| video_4 | botsort | 0.15 | 0.40 | 547 | 12 | 6 | [Xem](../runs/thu_bo_sung/video_4_botsort_conf0.15_iou0.40/video_4_preview.mp4) |
| video_4 | botsort | 0.15 | 0.70 | 547 | 12 | 6 | [Xem](../runs/thu_bo_sung/video_4_botsort_conf0.15_iou0.70/video_4_preview.mp4) |
| video_5 | bytetrack | 0.30 | 0.50 | 347 | 11 | 5 | [Xem](../runs/thu_bo_sung/video_5_bytetrack_conf0.30_iou0.50/video_5_preview.mp4) |
| video_5 | botsort | 0.30 | 0.50 | 449 | 17 | 5 | [Xem](../runs/thu_bo_sung/video_5_botsort_conf0.30_iou0.50/video_5_preview.mp4) |
| video_5 | botsort | 0.15 | 0.50 | 496 | 17 | 5 | [Xem](../runs/thu_bo_sung/video_5_botsort_conf0.15_iou0.50/video_5_preview.mp4) |
| video_5 | botsort | 0.50 | 0.50 | 269 | 10 | 2 | [Xem](../runs/thu_bo_sung/video_5_botsort_conf0.50_iou0.50/video_5_preview.mp4) |
| video_5 | botsort | 0.15 | 0.40 | 496 | 17 | 5 | [Xem](../runs/thu_bo_sung/video_5_botsort_conf0.15_iou0.40/video_5_preview.mp4) |
| video_5 | botsort | 0.15 | 0.70 | 496 | 17 | 5 | [Xem](../runs/thu_bo_sung/video_5_botsort_conf0.15_iou0.70/video_5_preview.mp4) |

## Đọc kết quả

- `video_1`: ByteTrack giảm 380 xuống 330 hộp khi tăng conf từ 0,30 lên 0,50. Ba mức iou cùng cho 380 hộp trong đoạn thử; giữ iou=0,50.
- `video_2`: hạ conf từ 0,30 xuống 0,15 tăng 682 lên 743 hộp, số ID giảm 14 xuống 12. Ở conf=0,15, iou 0,40 / 0,50 / 0,70 cho 741 / 743 / 761 hộp. Giữ iou=0,50; thêm hộp ở 0,70 chưa đủ chứng minh danh tính ổn định hơn trong cảnh đông.
- `video_3`: BoTSORT conf=0,15 cho 406 hộp so với 392 ở conf=0,30. Iou=0,70 tăng lên 459 hộp và 15 ID, trong khi iou=0,40 / 0,50 cho 406 hộp và 14 ID. Giữ iou=0,50 trong cấu hình nộp vì chưa có bằng chứng rõ rằng các hộp thêm giúp giữ ID tốt hơn khi camera đổi góc.
- `video_4`: BoTSORT conf=0,15 cho 547 hộp so với 509 ở conf=0,30. Ba mức iou cùng cho 547 hộp và 12 ID ở conf=0,15; giữ iou=0,50. Đoạn che khuất ở frame 690–770 của bản đủ frame vẫn cho thấy phân mảnh ID.
- `video_5`: BoTSORT conf=0,15 cho 496 hộp so với 449 ở conf=0,30 và 269 ở conf=0,50. Ba mức iou cùng cho 496 hộp và 17 ID; giữ iou=0,50. Người nhỏ ở xa vẫn khó phát hiện.

Bản nộp đầy đủ vẫn dùng các cấu hình trong [báo cáo](BAO_CAO_mau.md). Không chấm HOTA/MOTA/IDF1 cho video_2–video_5.

## Chạy lại một lượt

Ví dụ trong PowerShell tại repo root sau khi activate env:

```powershell
python scripts/run_tracking.py --source lab_data/video_3/img1 --seq-name video_3 --tracker botsort --conf 0.15 --iou 0.7 --out runs/thu_bo_sung/video_3_botsort_conf0.15_iou0.70 --max-frames 80 --save-video --device cpu
```

Đổi video/tracker/conf/iou theo từng dòng của bảng để chạy lại các cấu hình. Dữ liệu thống kê có cấu trúc: [thu_nghiem.json](minh_chung/thu_nghiem.json).
