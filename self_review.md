# Tự đánh giá — Nguyễn Xuân Lâm · G09

## 1. Tự rà soát 4 cảnh

Loại lỗi: `seat_flip`, `wrong_class`, `guess`, `box`, `missing`, `extra`, `lr_flip` (trái/phải mặt), `flag` (thiếu cờ điểm), `ok`.

| Ảnh | Đối tượng | Loại lỗi | Ghi chú | Đã sửa? |
|---|---|---|---|---|
| S02_ir | frame_meta | guess | `modality` để `rgb` cho ảnh `_ir` (quên đổi khi copy từ ảnh RGB sang). Script `cabin_check` không bắt được, review chéo mới phát hiện | Có (v2) |
| S04_rgb | infant_seat | guess | `facing` để giá trị mặc định `rear`, thực tế lòng nôi hướng về camera nên là `front` (cùng lỗi ở S01, S03, S04 cả rgb và ir) | Có (v2) |
| D04 | object, face | ok | Có box `object` cho chai nước trên tay tài xế. Guideline 4.2 ghi DMS không vẽ `object`, mình đã hỏi coach và coach xác nhận giữ. Mắt (`unknown` do lóa kính) và `gaze_zone` xem lại thấy đúng | Không cần sửa (coach xác nhận) |
| D06 | face | box | Box mặt ban đầu ôm cả đầu và tóc (rộng 280 px), đúng ra chỉ từ trán đến cằm, tai đến tai. Đã thu lại còn 177 px | Có (v2) |

## 2. Lỗi mình lặp lại nhiều nhất hôm nay

Lỗi: Quên đổi giá trị mà CVAT tự điền sẵn (ví dụ `modality = rgb` còn sót ở S02_ir sau khi copy, `infant_seat.facing = rear` ở S01–S04).

Vì sao mình mắc: CVAT tự điền giá trị đầu danh sách cho mọi thuộc tính, mình vẽ box xong chuyển ảnh luôn mà không mở DETAILS kiểm lại từng thuộc tính. Mình cũng không chạy Checkpoint A, B giữa buổi nên lỗi lặp lại qua nhiều ảnh mà không biết.

Lần sau tránh bằng cách: Vẽ xong box nào thì mở DETAILS chọn lại từng thuộc tính ngay; khi copy shape từ `_rgb` sang `_ir`, kiểm lại `frame_meta` theo tên file; chạy checkpoint đúng giờ để phát hiện lỗi sớm; không tin hoàn toàn vào script vì script không kiểm `modality` theo tên file.

## 3. Ghi chú về disagreement_log

Một dòng bạn của mình đúng và mình sai: D01, `glasses` — mình ghi `none` nhưng tài xế đeo kính cận (`clear`).

Mình học được gì từ dòng đó: Không được chọn `none` cho nhanh khi chưa nhìn kỹ vùng mắt. Ghi `none` cho người đang đeo kính là dạy model rằng người đeo kính không có kính (guideline 4.5); không chắc thì chọn `unknown`.
