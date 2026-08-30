"""
Script tinh toan chi so San sang Chuyen doi so (Digital Maturity Index - DMI)
theo khung danh gia 6 tru cot SHT / Vietduc AI.
"""

from typing import Dict, List, Tuple

PILLARS = {
    "van_hoa": "Văn hóa & Lãnh đạo số",
    "du_lieu": "Dữ liệu & Khả năng phân tích",
    "cong_nghe": "Hạ tầng & Công nghệ",
    "quy_trinh": "Quy trình & Tự động hóa",
    "con_nguoi": "Năng lực & Kỹ năng số",
    "khach_hang": "Trải nghiệm Khách hàng số"
}

LEVEL_LABELS = {
    1: "Cấp độ 1: Khởi động / Phân mảnh (Traditional)",
    2: "Cấp độ 2: Thử nghiệm / Cục bộ (Emerging)",
    3: "Cấp độ 3: Định hình / Chuẩn hóa (Standardized)",
    4: "Cấp độ 4: Tăng tốc / Tích hợp (Advanced)",
    5: "Cấp độ 5: Dẫn đầu / Tối ưu liên tục (Optimized)"
}

def calculate_dmi(scores: Dict[str, float]) -> Tuple[float, str, Dict[str, float]]:
    """
    Tinh diem DMI trung binh va phan cap truong thanh so.
    scores: dict { 'van_hoa': 2.5, 'du_lieu': 1.8, ... }
    """
    total = 0.0
    valid_count = 0
    pillar_gaps = {}
    
    for key, name in PILLARS.items():
        val = scores.get(key, 1.0)
        # Clamp score between 1.0 and 5.0
        val = max(1.0, min(5.0, float(val)))
        scores[key] = val
        total += val
        valid_count += 1
        # Gap compared to Target (Level 4 - Enterprise Standard)
        pillar_gaps[name] = round(max(0.0, 4.0 - val), 2)
        
    avg_score = round(total / valid_count, 2) if valid_count > 0 else 1.0
    
    if avg_score < 2.0:
        stage = LEVEL_LABELS[1]
    elif avg_score < 3.0:
        stage = LEVEL_LABELS[2]
    elif avg_score < 4.0:
        stage = LEVEL_LABELS[3]
    elif avg_score < 4.8:
        stage = LEVEL_LABELS[4]
    else:
        stage = LEVEL_LABELS[5]
        
    return avg_score, stage, pillar_gaps


def analyze_bottlenecks(process_list: List[Dict]) -> List[Dict]:
    """
    Xep hang cac diem nghen quy trinh theo thoi gian ton va rui ro sai sot.
    process_list: [ {'ten': '...', 'thoi_gian_phut': 60, 'ty_le_sai_pct': 5, 'muc_do': 'Cao'} ]
    """
    sorted_processes = sorted(
        process_list,
        key=lambda x: (x.get('ty_le_sai_pct', 0) * 0.4 + x.get('thoi_gian_phut', 0) * 0.6),
        reverse=True
    )
    return sorted_processes


if __name__ == "__main__":
    test_scores = {
        "van_hoa": 3.0,
        "du_lieu": 1.5,
        "cong_nghe": 2.0,
        "quy_trinh": 1.8,
        "con_nguoi": 2.2,
        "khach_hang": 2.5
    }
    score, stage, gaps = calculate_dmi(test_scores)
    print(f"[TEST] DMI Score: {score}/5.0")
    print(f"[TEST] Xep hang: {stage}")
    print("[TEST] Khoang cach den tieu chuan (Target Level 4):")
    for p, g in gaps.items():
        print(f"  - {p}: Thiếu {g} điểm")
