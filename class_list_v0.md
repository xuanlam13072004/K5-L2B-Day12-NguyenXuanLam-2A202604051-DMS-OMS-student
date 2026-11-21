# Danh sách lớp v0 — Nguyễn Xuân Lâm · G09

Viết tiếp từ slide 54 bài giảng. Mỗi lớp trả lời: **model cần nhận ra cái này để làm gì?**

## DMS (theo dõi tài xế)

| # | Lớp / thuộc tính | Giá trị | Để làm gì (chức năng DMS) | Nhìn thấy được trên IR? |
|---|---|---|---|---|
| 1 | eye_left / eye_right (trạng thái từng mắt) | open / closed / unknown | Phát hiện buồn ngủ: mắt nhắm kéo dài qua nhiều khung hình (PERCLOS) | Có; nhưng kính cận bị lóa đèn LED có thể che mắt, khi đó ghi unknown |
| 2 | gaze_zone (vùng nhìn) | road / mirror_l / mirror_r / mirror_c / cluster / center / lap / other | Phát hiện mất tập trung: nhìn ngoài đường quá lâu (ví dụ nhìn xuống đùi, nhìn màn hình) | Có, dựa vào hướng đầu và mắt; khó hơn khi mắt bị lóa |
| 3 | glasses (kính) | none / clear / sun / unknown | Biết khi nào trạng thái mắt kém tin cậy (kính lóa, kính râm) để model không kết luận sai là nhắm mắt | Một phần: trên NIR kính râm có thể trông trong suốt |
| 4 | face13 (13 điểm mặt) | 13 điểm, cờ occluded / outside | Đo độ mở mắt, ngáp (độ mở miệng), ước lượng hướng đầu | Có; điểm bị lóa hoặc bị tay che phải có cờ |
| 5 | hand + on_wheel (tay, có trên vô lăng) | whose, side, on_wheel: yes / no / unknown | Cảnh báo bỏ tay khỏi vô lăng khi xe không ở chế độ tự lái; biết tay đang làm việc khác | Có (hình dạng tay) |
| 6 | phone + state (điện thoại) | held / mounted / lap | Phát hiện dùng điện thoại khi lái (cầm tay, áp tai, để trên đùi) | Có nếu thấy cạnh, góc hoặc màn hình máy; vật tối áp tai thì khó |
| 7 | seatbelt của tài xế | worn_correct / worn_incorrect / not_worn / unknown | Nhắc thắt dây an toàn, phát hiện thắt sai (dây dưới nách) | Có, trừ khi dây chìm trong vùng tối |

## OMS (theo dõi hành khách)

| # | Lớp / thuộc tính | Giá trị | Để làm gì (chức năng OMS) | Nhìn thấy được trên IR? |
|---|---|---|---|---|
| 1 | person + seat (người, theo ghế) | driver / front_passenger / rear_left / rear_middle / rear_right | Đếm người trên xe, biết ghế nào có người để nhắc dây an toàn và điều chỉnh túi khí | Có (hình dạng người) |
| 2 | seatbelt theo ghế | worn_correct / worn_incorrect / not_worn / unknown | Nhắc thắt dây an toàn cho từng ghế sau | Một phần: dây trên áo tối hoặc vùng tối khó thấy |
| 3 | child_seat + occupied (ghế trẻ em) | occupied: no / unknown (coach cho thêm yes) | Nhắc quên trẻ trong xe; tắt túi khí nếu ghế trẻ em ở ghế trước | Có (hình dạng ghế) |
| 4 | infant_seat + facing (nôi em bé, hướng quay) | rear / front | Nôi quay ra sau đặt ở ghế trước thì bắt buộc tắt túi khí; nhắc quên em bé | Có (hình dạng), nhưng khó biết hướng nếu ảnh tối |
| 5 | object + type (đồ vật) | bag / box / cup / other | Nhắc quên đồ khi rời xe; không nhầm đồ vật là người khi đếm người | Có theo hình dạng; mất màu nên khó phân biệt loại vật giống nhau |
| 6 | face (box mặt người ngồi sau) | box | Xác nhận đúng là người thật (không phải đồ vật), hỗ trợ ước lượng tầm vóc người lớn/trẻ em | Có |
| 7 | frame_meta: camera_blocked | yes / no | Báo camera bị che để hệ thống không đưa ra kết luận sai (ví dụ báo "ghế trống" khi thật ra không nhìn thấy) | Có |

## 2 câu hỏi leo thang

1. Câu hỏi: Trẻ em đang ngồi trong ghế trẻ em thì gán thế nào? Guideline v1.0 chỉ cho `child_seat` trống (`occupied` không có `yes`) và yêu cầu "thấy trẻ em thì báo coach, không gán". Có cần vẽ thêm `person` cho trẻ không, và có nên thêm giá trị `yes` chính thức vào guideline không?
   Khung ví dụ: G09 S02_rgb, S02_ir (ghế rear_left)
   Bạn tạm gán thế nào và vì sao: Gán `child_seat`, `occupied = yes`, không vẽ `person` cho trẻ, theo chỉ dẫn của coach trong buổi (coach cho thêm giá trị `yes` và sửa script `cabin_check` để chấp nhận).
2. Câu hỏi: Tài xế cầm chai nước hoặc cốc trên tay thì có cần gán vật đó không? Guideline 4.2 ghi DMS không vẽ `object`, nhưng chức năng DMS có thể cần phân biệt "uống nước" với "dùng điện thoại" để không báo động nhầm.
   Khung ví dụ: G09 D04, D06
   Bạn tạm gán thế nào và vì sao: Giữ box `object` (type `other`) cho chai trên tay ở D04, D06. Mình đã hỏi coach và coach xác nhận giữ, vì vật này có ích để phân biệt "uống nước" với "dùng điện thoại". Đề xuất cập nhật guideline 4.2 (bản 1.x) cho rõ: cho phép `object` ở DMS, hoặc thêm lớp `drink`.
