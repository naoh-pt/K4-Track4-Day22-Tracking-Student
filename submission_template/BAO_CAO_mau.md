# Báo cáo lab: chọn tracker cho 5 video

**Nhóm:** TH001 **Thành viên:** Phan Trọng Hoàn (2A202602954), Nguyễn Văn Tứ (2A202602586)

Detector cố định: `yolo26n.pt`, ảnh 640 px, Re-ID `osnet_x0_25_msmt17`. Không đổi các mục này trong bài nộp chính.

## 1. Cấu hình đã chọn

Mỗi video: tracker bạn nộp, `conf`, `iou`, điều bạn **nhìn thấy** trên video, và một cấu hình đã thử rồi loại.

| Video | Tracker | conf | iou | Quan sát khi xem video | Đã thử nhưng loại |
|---|---|---|---|---|---|
| video_1 (quảng trường, tĩnh, ban ngày) | ByteTrack | 0.30 | 0.50 | Đã chạy đủ 600 frame. Trong 150 frame đầu, hai người gần camera giữ ID 2 và 3 xuyên suốt; ở các frame giữa/cuối vẫn có người nhỏ ở xa chưa được gán hộp. | BoTSORT (0.30, 0.50) tạo nhiều ID hơn và có dấu hiệu cấp lại ID cho người gần camera trong đoạn thử; ByteTrack `conf=0.50` bỏ bớt hộp. |
| video_2 (phố đêm, tĩnh, rất đông) | ByteTrack | 0.15 | 0.50 | Đã chạy đủ 1.050 frame. Ở các frame xem thử giữa/cuối, nhiều người rõ được gán hộp; người nhỏ, tối hoặc bị đám đông che vẫn dễ bị bỏ sót. | BoTSORT (0.30, 0.50) có thêm hộp nhưng nhiều ID hơn trong đoạn thử, chưa thấy giữ ID tốt hơn rõ rệt ở người gần camera; ByteTrack `conf=0.50` bỏ nhiều hộp. |
| video_3 (camera di động, ảnh nhỏ) | BoTSORT | 0.15 | 0.50 | Đã chạy đủ 837 frame. Ở các frame giữa/cuối, tracker vẫn gán hộp cho người khi camera đổi góc; nhiều ID mới xuất hiện khi người đi vào/ra hoặc bị che. | ByteTrack (0.30, 0.50) có ít hộp hơn trong đoạn thử; BoTSORT `conf=0.50` bỏ nhiều người. |
| video_4 (trong nhà, camera di chuyển) | BoTSORT | 0.15 | 0.50 | Đã chạy đủ 900 frame. Hộp chủ yếu bám vào người thật ở các frame đã xem. Người áo đỏ có ID 2 đến frame 709; sau đoạn bị người đi ngang che, ở frame 730/740 người này vẫn thấy nhưng không có hộp; từ frame 759 được gán ID 93. Track còn bị phân mảnh sau che khuất. | ByteTrack (0.30, 0.50) có ít hộp hơn trên đoạn thử; BoTSORT `conf=0.50` bỏ sót thêm người. |
| video_5 (trên xe bus, giao lộ đông) | BoTSORT | 0.15 | 0.50 | Đã chạy đủ 750 frame. Ở frame giữa, tracker bắt được một số người gần giao lộ; đến cuối video còn ít người và người nhỏ ở xa dễ bị bỏ sót. Góc nhìn từ xe thay đổi liên tục nên nhiều track mới xuất hiện. | ByteTrack (0.30, 0.50) có ít hộp hơn trong đoạn thử; BoTSORT `conf=0.50` bỏ nhiều người. |

Năm file `runs/nop_bai/video_1.txt` đến `video_5.txt` đã được tạo và kiểm tra đúng định dạng MOT. Các preview tương ứng có đủ 600, 1.050, 837, 900 và 750 frame.

## 2. Số liệu video_1

Chấm `runs/nop_bai/video_1.txt` bằng `scripts/evaluate_practice.py` với TrackEval, lớp `pedestrian`:

| HOTA | MOTA | IDF1 | DetA | AssA | IDSW | CLR_FN | CLR_FP |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 26,912 | 17,292 | 25,713 | 15,068 | 48,130 | 12 | 15.249 | 107 |

HOTA, MOTA, IDF1, DetA và AssA là điểm phần trăm. Số bỏ sót (`CLR_FN`) cao cho thấy nhiều người trong nhãn chưa được phát hiện; nhận xét này phù hợp với các người nhỏ ở xa đã thấy khi xem preview. Điểm số chỉ phản ánh cấu hình đã nộp cho `video_1`, không suy rộng sang các video khác.

`video_2` đến `video_5` không có nhãn trong gói lab. Không điền số cho các video đó.

## 3. Phân tích

**video_1:** Camera đứng yên và người gần camera di chuyển tương đối đều, nên ByteTrack theo chuyển động đủ giữ ID 2 và 3 trong 150 frame đầu. BoTSORT cho nhiều hộp hơn nhưng cũng tạo thêm ID trong đoạn thử, có dấu hiệu phân mảnh ở người gần camera. Với `conf=0.50`, ByteTrack giảm từ 380 xuống 330 hộp trong 80 frame đầu và giảm số track dài; vì vậy chọn `conf=0.30`. Người nhỏ ở xa vẫn có thể bị bỏ sót.

**video_2:** Cảnh đêm đông người khiến nhiều người nhỏ hoặc bị che khó phát hiện. Hạ `conf` của ByteTrack từ 0.30 xuống 0.15 tăng từ 682 lên 743 hộp trong 80 frame đầu, đồng thời số ID trong đoạn này giảm từ 14 xuống 12; đó chỉ là thống kê đầu ra, không phải điểm chất lượng. Xem video giữa và cuối cho thấy nhiều người rõ vẫn được theo dõi, nhưng còn người tối hoặc ở xa bị bỏ sót. Camera đứng yên giúp việc ghép theo chuyển động dễ hơn, nên chọn ByteTrack cho bản đủ frame.

**video_3:** Camera chuyển động và ảnh nhỏ làm vị trí người thay đổi nhanh, nên BoTSORT có bước bù chuyển động camera và Re-ID đáng thử. Ở 80 frame đầu, hạ `conf` từ 0.30 xuống 0.15 tăng từ 392 lên 406 hộp. Bản đủ frame có nhiều ID mới; quan sát này cần được hiểu cùng với việc người liên tục vào/ra khung hình và bị che, không thể xem số ID là điểm chất lượng.

**video_4:** Camera tiến về phía trước nên vị trí và kích thước người thay đổi liên tục. Trong đoạn thử 80 frame, BoTSORT `conf=0.15` giữ 547 hộp, so với 509 hộp ở `conf=0.30`; xem frame mẫu cho thấy nhiều hộp thêm nằm trên người ở xa. Bản đủ 900 frame có 6.625 dòng kết quả và 70 ID; đây là thống kê đầu ra, không phải điểm chất lượng vì video này không có nhãn. Kiểm tra đoạn frame 690–770 cho thấy người áo đỏ mất track ID 2 sau frame 709 và được gán ID 93 từ frame 759 sau che khuất. Re-ID chưa nối lại danh tính cũ trong trường hợp này. Đây là nhận xét trực quan về phân mảnh, không phải số IDSW được chấm bằng nhãn.

**video_5:** Camera trên xe di chuyển và rung, còn người trên vỉa hè thường nhỏ trong ảnh. Ở 80 frame đầu, BoTSORT `conf=0.15` giữ 496 hộp so với 449 hộp ở `conf=0.30`; các frame mẫu cho thấy thêm hộp trên người ở hai bên đường. Bản đủ 750 frame có 3.333 dòng kết quả và 79 ID, nhưng nhiều người xa vẫn không có hộp. Vì không có nhãn, nhóm chỉ dùng preview để nhận xét việc bỏ sót và ID, không gán điểm HOTA/MOTA/IDF1 cho video này.

## 4. Nếu có thêm thời gian

Nhóm sẽ xem thêm những đoạn người bị che và xuất hiện lại ở `video_3` và `video_5` để phân biệt đổi ID với một track mới hợp lý. Với `video_1`, nhóm sẽ thử các mức `conf` giữa 0,15 và 0,30 rồi chấm lại bằng TrackEval để kiểm tra liệu số bỏ sót có giảm mà không làm tăng nhiều hộp sai hay không.

## 5. Minh chứng bổ sung khi rà soát checkpoint

Notebook đã chạy đủ 4 ô code; ba câu nhận định đều đúng. Trên ảnh đầu `video_1`, YOLO cho 14 / 6 / 5 hộp người với `conf` lần lượt 0,15 / 0,30 / 0,50 và `iou=0,50`.

Đã chạy lại baseline ByteTrack 150 frame và bổ sung 30 lượt thử, mỗi lượt 80 frame đầu: cả ByteTrack và BoTSORT cho từng video, quét `conf=0,15 / 0,30 / 0,50`, rồi giữ `conf` cố định để thử `iou=0,40 / 0,50 / 0,70`. Chi tiết và đường dẫn preview nằm trong [THU_NGHIEM_BO_SUNG.md](THU_NGHIEM_BO_SUNG.md). Các lượt thử này có thư mục riêng trong `runs/thu_bo_sung/`.

Đã chấm lại `video_1`: HOTA 26,912; MOTA 17,292; IDF1 25,713, khớp bảng ở mục 2. Kết quả gốc được lưu tại [video_1_summary.txt](minh_chung/video_1_summary.txt). Thống kê và mã SHA-256 của năm file nộp nằm trong [kiem_tra_file_nop.json](minh_chung/kiem_tra_file_nop.json). Preview đầy đủ được dựng lại từ file MOT đã nộp và toàn bộ ảnh đầu vào, với 600 / 1.050 / 837 / 900 / 750 frame.

Bảng đối chiếu yêu cầu và kết quả kiểm tra: [KIEM_TRA_CP.md](KIEM_TRA_CP.md).
