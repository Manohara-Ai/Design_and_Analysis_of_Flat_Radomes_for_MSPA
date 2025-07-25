import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

data_path = "./data"
save_path = "./overlay_results"
os.makedirs(save_path, exist_ok=True)

def plot_polar(files: dict, phi_filter=0, column="dB(GainTotal) []", title="Radiation Pattern", filename="plot.png"):
    fig, ax = plt.subplots(subplot_kw={"polar": True}, figsize=(8, 6))
    for label, fname in files.items():
        filepath = os.path.join(data_path, fname)
        df = pd.read_csv(filepath)
        df["Phi [deg]"] = pd.to_numeric(df["Phi [deg]"], errors="coerce")
        df["Theta [deg]"] = pd.to_numeric(df["Theta [deg]"], errors="coerce")
        df[column] = pd.to_numeric(df[column], errors="coerce")
        df = df[df["Phi [deg]"] == phi_filter]
        theta_rad = np.deg2rad(df["Theta [deg]"].values)
        values = df[column].values
        display_label = "Without Flat Radome" if label == "W" else "With Flat Radome"
        ax.plot(theta_rad, values, label=display_label)
    ax.set_title(f"{title} (phi={phi_filter}°)")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.grid(True)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2))
    plt.tight_layout()
    plt.savefig(os.path.join(save_path, filename), dpi=300)
    plt.close()

def plot_rectangular(files: dict, x_column, y_column, x_label, y_label, title, filename):
    fig, ax = plt.subplots(figsize=(8, 6))
    for label, fname in files.items():
        filepath = os.path.join(data_path, fname)
        df = pd.read_csv(filepath)
        df[x_column] = pd.to_numeric(df[x_column], errors="coerce")
        df[y_column] = pd.to_numeric(df[y_column], errors="coerce")
        x = df[x_column].values
        y = df[y_column].values
        display_label = "Without Flat Radome" if label == "W" else "With Flat Radome"
        ax.plot(x, y, label=display_label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(save_path, filename), dpi=300)
    plt.close()

if __name__ == "__main__":

    # 1. Gain patterns (polar, multiple frequencies)
    compare_files = {
        "3 GHz": {"R": "with_radome/GPE3R.csv", "W": "without_radome/GPE3W.csv"},
        "6 GHz": {"R": "with_radome/GPE6R.csv", "W": "without_radome/GPE6W.csv"},
        "9 GHz": {"R": "with_radome/GPE9R.csv", "W": "without_radome/GPE9W.csv"},
    }
    for freq, fileset in compare_files.items():
        plot_polar(
            fileset,
            phi_filter=0,
            column="dB(GainTotal) []",
            title=f"Gain Pattern at {freq} (E-plane)",
            filename=f"gainE_{freq.replace(' ', '_')}.png"
        )

    compare_files = {
        "3 GHz": {"R": "with_radome/GPH3R.csv", "W": "without_radome/GPH3W.csv"},
        "6 GHz": {"R": "with_radome/GPH6R.csv", "W": "without_radome/GPH6W.csv"},
        "9 GHz": {"R": "with_radome/GPH9R.csv", "W": "without_radome/GPH9W.csv"},
    }
    for freq, fileset in compare_files.items():
        plot_polar(
            fileset,
            phi_filter=90,  # <-- Corrected!
            column="dB(GainTotal) []",
            title=f"Gain Pattern at {freq} (H-plane)",
            filename=f"gainH_{freq.replace(' ', '_')}.png"
        )

    # 2. E-plane gain
    plot_polar(
        {"W": "without_radome/Gain_E.csv", "R": "with_radome/Gain_E.csv"},
        phi_filter=0,
        column="dB(GainTotal) []",
        title="E-plane Gain Pattern",
        filename="gain_E_polar.png"
    )

    # 3. H-plane gain
    plot_polar(
        {"W": "without_radome/Gain_H.csv", "R": "with_radome/Gain_H.csv"},
        phi_filter=90,
        column="dB(GainTotal) []",
        title="H-plane Gain Pattern",
        filename="gain_H_polar.png"
    )

    # 8. S11 rectangular
    plot_rectangular(
        {"W": "without_radome/S11.csv", "R": "with_radome/S11.csv"},
        x_column="Freq [GHz]",
        y_column="dB(S(1,1)) []",
        x_label="Frequency (GHz)",
        y_label="S11 (dB)",
        title="S11 Parameter vs Frequency",
        filename="s11.png"
    )

    # 9. VSWR rectangular
    plot_rectangular(
        {"W": "without_radome/VSWR.csv", "R": "with_radome/VSWR.csv"},
        x_column="Freq [GHz]",
        y_column="dB(VSWR(1)) []",
        x_label="Frequency (GHz)",
        y_label="VSWR",
        title="VSWR vs Frequency",
        filename="vswr.png"
    )
