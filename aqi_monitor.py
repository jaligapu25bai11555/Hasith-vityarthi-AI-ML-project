import random
from datetime import date

readings = [
    (312, "Winter"), (287, "Winter"), (345, "Winter"), (260, "Winter"),
    (298, "Winter"), (330, "Winter"), (275, "Winter"), (310, "Winter"),
    (255, "Winter"), (290, "Winter"), (320, "Winter"), (268, "Winter"),

    (210, "Post-Monsoon"), (185, "Post-Monsoon"), (225, "Post-Monsoon"),
    (198, "Post-Monsoon"), (215, "Post-Monsoon"), (175, "Post-Monsoon"),
    (230, "Post-Monsoon"), (192, "Post-Monsoon"),

    (155, "Summer"), (140, "Summer"), (168, "Summer"), (132, "Summer"),
    (160, "Summer"), (145, "Summer"), (172, "Summer"), (138, "Summer"),

    (62, "Monsoon"), (48, "Monsoon"), (75, "Monsoon"), (55, "Monsoon"),
    (70, "Monsoon"), (44, "Monsoon"), (80, "Monsoon"), (58, "Monsoon"),
    (90, "Monsoon"), (66, "Monsoon"),
]

def get_info(aqi):
    if aqi <= 50:
        return (
            "Good",
            "Air quality is clean and safe.",
            [
                "Enjoy outdoor activities freely.",
                "Great day for exercise or a walk.",
                "No precautions needed.",
            ]
        )
    elif aqi <= 100:
        return (
            "Satisfactory",
            "Air quality is acceptable for most people.",
            [
                "Sensitive individuals (asthma, elderly) should limit long outdoor sessions.",
                "Fine for most healthy adults.",
                "Keep windows open — air circulation is good.",
            ]
        )
    elif aqi <= 200:
        return (
            "Moderate",
            "Air quality may cause discomfort for sensitive groups.",
            [
                "Children and elderly should reduce prolonged outdoor exposure.",
                "Avoid heavy outdoor exercise if you feel irritation.",
                "Consider wearing a mask if you have a respiratory condition.",
                "Keep indoor plants — they help filter indoor air.",
            ]
        )
    elif aqi <= 300:
        return (
            "Poor",
            "Everyone may begin to experience health effects.",
            [
                "Limit outdoor activity to short durations.",
                "Wear an N95 mask (cloth masks are not effective for PM2.5).",
                "Keep windows and doors closed.",
                "Use an air purifier indoors if available.",
                "Avoid burning trash or using incense — it worsens indoor air.",
            ]
        )
    elif aqi <= 400:
        return (
            "Very Poor",
            "Health warnings — serious effects for everyone.",
            [
                "Avoid all non-essential outdoor activity.",
                "Wear an N95 mask if you must go outside.",
                "Keep children and elderly strictly indoors.",
                "Seal gaps in windows and doors if possible.",
                "Stay hydrated — it helps your body clear pollutants.",
                "Visit a doctor if you experience breathing difficulty.",
            ]
        )
    else:
        return (
            "Severe / Hazardous",
            "Health emergency. Everyone is at serious risk.",
            [
                "Do NOT go outside unless absolutely necessary.",
                "Keep all windows shut. Turn off ventilation fans.",
                "Wear an N95 mask even indoors if air feels thick.",
                "Seek immediate medical help for any breathing issues.",
                "This level is comparable to the environmental crisis Bhopal has faced historically.",
            ]
        )

def line(char="─", width=52):
    print(char * width)

def run():
    today = date.today().strftime("%d %B %Y")

    aqi, season = random.choice(readings)
    aqi = max(10, aqi + random.randint(-15, 15))

    label, warning, tips = get_info(aqi)

    print()
    line("═")
    print("  BHOPAL AIR QUALITY REPORT")
    print(f"  Date   : {today}")
    print(f"  Season : {season}")
    line("═")

    print(f"\n  AQI Reading  :  {aqi}")
    print(f"  Category     :  {label}")
    print(f"\n  {warning}")

    print()
    line()
    print("  PRECAUTIONS")
    line()
    for i, tip in enumerate(tips, 1):
        print(f"  {i}. {tip}")

    print()
    line()
    print("  AQI SCALE REFERENCE")
    line()
    scale = [
        ("  0 – 50  ", "Good"),
        ("  51 – 100", "Satisfactory"),
        ("101 – 200 ", "Moderate"),
        ("201 – 300 ", "Poor"),
        ("301 – 400 ", "Very Poor"),
        ("401 – 500 ", "Severe / Hazardous"),
    ]
    for band, name in scale:
        marker = "  <<" if name == label else ""
        print(f"  {band}  {name}{marker}")

    print()
    line("═")
    print("  Data source: Simulated from Bhopal seasonal AQI profiles")
    print("  Real-time data: https://aqicn.org/city/bhopal/")
    line("═")
    print()

if __name__ == "__main__":
    run()
