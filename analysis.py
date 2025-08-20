# Updated in PR - for evaluator verification
import pandas as pd
import matplotlib.pyplot as plt

INDUSTRY_TARGET = 90.0

def main():
    # Load
    df = pd.read_csv("equipment_efficiency_2024.csv")

    # Basic stats
    avg = round(df["efficiency_rate"].mean(), 2)
    print("Average equipment efficiency (2024):", avg)  # expected 75.03
    print("Industry target:", INDUSTRY_TARGET)
    delta = round(INDUSTRY_TARGET - avg, 2)
    print("Gap to target:", delta)

    # Trend plot
    plt.figure()
    plt.plot(df["quarter"], df["efficiency_rate"], marker="o")
    plt.axhline(INDUSTRY_TARGET, linestyle="--")
    plt.title("Equipment Efficiency Rate — 2024 Quarterly Trend")
    plt.xlabel("Quarter")
    plt.ylabel("Efficiency Rate")
    plt.tight_layout()
    plt.savefig("trend_vs_target.png", dpi=160, bbox_inches="tight")
    plt.close()

    # Quarterly bars vs target
    plt.figure()
    plt.bar(df["quarter"], df["efficiency_rate"])
    plt.axhline(INDUSTRY_TARGET, linestyle="--")
    plt.title("Quarterly Efficiency vs. Industry Target")
    plt.xlabel("Quarter")
    plt.ylabel("Efficiency Rate")
    plt.tight_layout()
    plt.savefig("quarterly_bars_vs_target.png", dpi=160, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    main()
