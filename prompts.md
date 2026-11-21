# Khai báo dùng AI — Nguyễn Xuân Lâm

Nhắc lại: không đưa ảnh cabin hay ảnh tài xế (kể cả ảnh chụp màn hình) cho bất kỳ công cụ AI nào. Mình chỉ gửi chữ (câu hỏi, kết quả script, file nhãn JSON); AI chỉ đọc file export (tọa độ, thuộc tính), không xem ảnh.

| # | Công cụ | Bạn hỏi gì (tóm tắt) | Bạn dùng kết quả thế nào | Bạn có kiểm lại không? Bằng gì? |
|---|---|---|---|---|
| 1 | Claude | Đọc repo lab, hướng dẫn tổng quan các bước làm | Làm theo thứ tự: cài CVAT, tạo project/task, gán, kiểm, review chéo, nộp | Có, đối chiếu README, GUIDE, CHECKPOINTS |
| 2 | Claude | Ảnh màu và ảnh xám trong `oms/` có cần đưa lên cả không; nhóm 2 người tạo task bao nhiêu ảnh; vì sao bỏ S09–S10 | Tạo task 22 ảnh (cả rgb và ir), không chia ảnh, không làm S09–S10 | Có, đối chiếu GUIDE Task 0, RULES §1 |
| 3 | Claude | Guideline quy định gán gì, cách chọn thuộc tính từng label, giải thích bằng tiếng Việt | Dùng làm bảng tra khi gán | Có, đối chiếu GUIDE §4 |
| 4 | Claude | Các ca cụ thể: tay gán từ đâu đến đâu, hình người dựng (hình nộm) có gán không, có gán face/hand ở ảnh S## không, face có lấy tóc không, vì sao `light = unknown` cho S01–S08 | Áp dụng khi gán | Có, đối chiếu GUIDE §4.1, 4.5, 4.7, §3 |
| 5 | Claude | So danh sách nhãn mới coach phát với bản gốc; trẻ em ngồi ghế trẻ em gán thế nào | Biết điểm khác là `occupied = yes`; hỏi coach ca S02 | Có, hỏi coach |
| 6 | Claude | Lỗi FileNotFoundError `manifest.csv`; giải thích 2 lỗi `occupied='yes'` trong `check_final` | Sửa đường dẫn, hỏi coach | Có, chạy lại script |
| 7 | Claude | Sửa `scripts/cabin_schema.py` cho chấp nhận `occupied = yes` (sau khi coach xác nhận) | Claude sửa dòng 48, giữ bản gốc `.bak`; chạy lại ra 0 lỗi | Có, chạy lại `cabin_check` |
| 8 | Claude | Hướng dẫn commit lên GitHub | Tự chạy `git add`, `commit`, `push` | Có, xem trên GitHub |
| 9 | Claude | Chạy `cabin_check diff` với bài của Lê Quang Vinh, gợi ý ai đúng theo mục guideline nào | Mình tự mở ảnh trên CVAT xem lại các dòng cần nhìn ảnh, quyết định verdict, sửa bài và export v2 | Có, xem ảnh trên CVAT, đối chiếu GUIDE |
| 10 | Claude | Gợi ý nháp `ir_log.csv`, `class_list_v0.md`, `self_review.md`, `TEAM.md`, file `check_*.txt` từ câu trả lời của mình | Đọc lại, sửa theo quan sát của mình rồi mới nộp | Có, đối chiếu ảnh trên CVAT và GUIDE |
