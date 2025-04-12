# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# ファイルパスの設定
input_path = "/Users/yamaguchitaisei/wave data.xlsx"
output_path = "/Users/yamaguchitaisei/20250119.png"
sheet_name = "20250119"

# Excelファイルの読み込み
df = pd.read_excel(input_path, sheet_name=sheet_name)

# 数値データに変換
df["Current speed (wave cell) [m/sec]"] = pd.to_numeric(df["Current speed (wave cell) [m/sec]"], errors='coerce')
df["Current direction (wave cell) [deg]"] = pd.to_numeric(df["Current direction (wave cell) [deg]"], errors='coerce')

# フィルタ（Current speedが0以上、Current directionが欠損でない）
df_clean = df[
    (df["Current speed (wave cell) [m/sec]"] >= 0) 
    ].dropna(subset=["Current speed (wave cell) [m/sec]"])

# データ抽出
r = df_clean["Current speed (wave cell) [m/sec]"]
theta_deg = df_clean["Current direction (wave cell) [deg]"]
theta_rad = np.deg2rad((270 - theta_deg) % 360)

# プロット
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.scatter(theta_rad, r, color='blue', marker='o')

# 放射ラベルを 0.02〜0.18 に固定（0.00 は表示しない）
r_ticks = np.arange(0.02, 0.18, 0.02)
r_labels = [f"{tick:.2f}" for tick in r_ticks]
ax.set_yticks(r_ticks)
ax.set_yticklabels(r_labels, ha='left', va='bottom')
ax.set_rlabel_position(22.5)
ax.tick_params(axis='y', labelsize=10)

# 極座標の設定（上が北、時計回り）
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

# タイトル
ax.set_title("Polar Scatter Plot of Current Data (20250119)", va='bottom', y=1.15)

# 保存＆表示
plt.tight_layout()
plt.savefig(output_path, dpi=300)
plt.show()
