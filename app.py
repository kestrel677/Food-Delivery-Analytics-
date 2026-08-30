# Add a fallback for delivery_speed if it doesn't exist in the CSV
    if "delivery_speed" not in df.columns:
        df["delivery_speed"] = pd.cut(
            df["Time_taken (min)"],
            bins=[0, 20, 30, 120],
            labels=["Fast", "Average", "Slow"]
        ).astype(str)
