# TEAM — Ngày 12

Mã bộ ảnh: **G09** · Hình thức: cá nhân (review chéo với bạn cùng mã G09)

| Họ tên | MSSV | Đã gán đủ 22 ảnh? | Review chéo với (peer diff) | Số dòng disagreement đã xử lý |
|---|---|---|---|---|
| Nguyễn Xuân Lâm | 2A202604051 | có | Lê Quang Vinh (2A202604059) | 67 / 67 |

Ca hai bạn vẫn không thống nhất và đã hỏi coach (ghi tên ảnh + đối tượng):

- G09 S02_rgb, S02_ir · `child_seat` ở ghế rear_left có trẻ em ngồi. Coach cho thêm giá trị `occupied = yes` và xác nhận sửa `scripts/cabin_schema.py` để `cabin_check` chấp nhận `yes`. Không vẽ thêm `person` cho trẻ.

## Cá nhân

### NguyenXuanLam-2A202604051
- Phần mình làm (ngoài 22 ảnh của mình): chạy `cabin_check diff` giữa bài của mình và bài của Lê Quang Vinh, cùng Vinh xử lý 67 dòng khác nhau trong `disagreement_log.csv`, sửa bài và export `export_final_v2.zip`; hỏi coach ca S02.
- Điều mình học được hôm nay: Ghế phải gọi theo xe chứ không theo ảnh, trái/phải mắt và tay gọi theo người kể cả khi ảnh xoay 90°; không thấy thì ghi `unknown` thay vì đoán; và hai người gán giống nhau chỉ chứng tỏ nhất quán, không chứng tỏ đúng (cả hai đã cùng vẽ thừa `object` ở D04, D06).
