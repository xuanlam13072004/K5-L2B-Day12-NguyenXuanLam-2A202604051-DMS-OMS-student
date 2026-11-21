"""Guideline Cabin v1.0 label schema, shared by cabin_check.py and the CVAT label JSON.

Source of truth: lab_day_12.html, section "Label và thuộc tính".
Edit here only; regenerate the CVAT label JSON with:  python3 cabin_schema.py > ../cvat/labels_cabin_v1.json
"""
import json

SEATS = ["driver", "front_passenger", "rear_left", "rear_middle", "rear_right"]
# SVIRO cars with only two rear seats (sviro.kl.dfki.de/data: "some cars have only two rear seats").
TWO_REAR_SEAT_CARS = {"i3", "zoe"}

FACE13_POINTS = [
    "left_eye_outer", "left_eye_inner", "left_eye_upper", "left_eye_lower",
    "right_eye_outer", "right_eye_inner", "right_eye_upper", "right_eye_lower",
    "nose_tip", "mouth_left", "mouth_right", "lip_upper", "lip_lower",
]
# Edges: each eye corner -> upper and lower lid; each mouth corner -> both lips; nose_tip -> lip_upper.
FACE13_EDGES = [
    ("left_eye_outer", "left_eye_upper"), ("left_eye_outer", "left_eye_lower"),
    ("left_eye_inner", "left_eye_upper"), ("left_eye_inner", "left_eye_lower"),
    ("right_eye_outer", "right_eye_upper"), ("right_eye_outer", "right_eye_lower"),
    ("right_eye_inner", "right_eye_upper"), ("right_eye_inner", "right_eye_lower"),
    ("mouth_left", "lip_upper"), ("mouth_left", "lip_lower"),
    ("mouth_right", "lip_upper"), ("mouth_right", "lip_lower"),
    ("nose_tip", "lip_upper"),
]
MIN_FACE13_WIDTH_PX = 60  # lab rule: face box narrower than 60 px gets no face13

# label -> (cvat type, {attribute: [allowed values]}); first value of each list is the CVAT default.
LABELS = {
    "face": ("rectangle", {
        "eye_left": ["unknown", "open", "closed"],
        "eye_right": ["unknown", "open", "closed"],
        "glasses": ["unknown", "none", "clear", "sun"],
        "gaze_zone": ["other", "road", "mirror_l", "mirror_r", "mirror_c", "cluster", "center", "lap"],
    }),
    "face13": ("skeleton", {}),
    "hand": ("rectangle", {
        "whose": ["driver", "passenger"],
        "side": ["left", "right"],
        "on_wheel": ["unknown", "yes", "no"],
    }),
    "phone": ("rectangle", {"state": ["held", "mounted", "lap"]}),
    "person": ("rectangle", {
        "seat": SEATS,
        "seatbelt": ["unknown", "worn_correct", "worn_incorrect", "not_worn"],
    }),
    "child_seat": ("rectangle", {"seat": SEATS, "occupied": ["unknown", "no", "yes"]}),
    "infant_seat": ("rectangle", {"seat": SEATS, "facing": ["rear", "front"]}),
    "object": ("rectangle", {"seat": SEATS, "type": ["other", "bag", "box", "cup"]}),
    "frame_meta": ("tag", {
        "modality": ["ir", "rgb"],
        "light": ["unknown", "day", "night"],
        "camera_blocked": ["no", "yes"],
    }),
}
SEATED_LABELS = {"person", "child_seat", "infant_seat", "object"}


def _skeleton_svg():
    """SVG layout CVAT's skeleton constructor stores (points on a 0..100 canvas)."""
    pos = {
        "left_eye_outer": (80, 30), "left_eye_inner": (60, 30), "left_eye_upper": (70, 25), "left_eye_lower": (70, 35),
        "right_eye_outer": (20, 30), "right_eye_inner": (40, 30), "right_eye_upper": (30, 25), "right_eye_lower": (30, 35),
        "nose_tip": (50, 55), "mouth_left": (65, 75), "mouth_right": (35, 75), "lip_upper": (50, 70), "lip_lower": (50, 82),
    }
    ids = {n: i + 1 for i, n in enumerate(FACE13_POINTS)}
    parts = []
    for a, b in FACE13_EDGES:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="black" data-type="edge" '
                     f'data-node-from="{ids[a]}" data-node-to="{ids[b]}"></line>')
    for n in FACE13_POINTS:
        x, y = pos[n]
        parts.append(f'<circle r="1.5" stroke="black" fill="#b3b3b3" cx="{x}" cy="{y}" data-type="element node" '
                     f'data-element-id="{ids[n]}" data-node-id="{ids[n]}" data-label-name="{n}"></circle>')
    return "".join(parts)


def cvat_labels_json():
    """Label list for CVAT's Raw label constructor (Project > Labels > Raw)."""
    out = []
    for name, (kind, attrs) in LABELS.items():
        entry = {"name": name, "type": kind, "attributes": [
            {"name": a, "mutable": False, "input_type": "select", "default_value": v[0], "values": v}
            for a, v in attrs.items()]}
        if kind == "skeleton":
            entry["sublabels"] = [{"name": p, "type": "points", "attributes": []} for p in FACE13_POINTS]
            entry["svg"] = _skeleton_svg()
        out.append(entry)
    return out


if __name__ == "__main__":
    print(json.dumps(cvat_labels_json(), indent=2, ensure_ascii=False))
