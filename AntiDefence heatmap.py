import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the file
df = pd.read_csv("modified-durham-defense.csv", sep=",")

# Clean up: drop accidental header rows
df = df[df["subtype"] != "subtype"]
df = df[df["type"] != "type"]

# If needed: also remove accidental 'type' from other columns
df = df[df["sys_id"] != "type"]
df = df[df["sys_id"] != "subtype"]

# Extract genome ID from sys_id
df["genome"] = df["sys_id"].apply(lambda x: "_".join(x.split("_")[:-2]))

# Group by 'type' and 'genome' (or 'subtype' if you prefer)
presence_df = df.groupby(["type", "genome"]).size().unstack(fill_value=0)

# Convert to binary matrix
presence_df = (presence_df > 0).astype(int)

# Remove index/column names to avoid extra labels
presence_df.index.name = None
presence_df.columns.name = None

# Export the matrix
presence_df.to_csv("presence_absence_matrix_type.tsv", sep="\t", index=True)

# Plot heatmap
plt.figure(figsize=(8, 8))  # Adjust the figure size to a square
sns.heatmap(presence_df, cmap="Blues", cbar=True, linewidths=2, linecolor='black', square=True,
            cbar_kws={"shrink": 0.4})  # Adjust the shrink factor for the colorbar

plt.title("Presence/Absence Heatmap", fontsize=14)
plt.xlabel("Phages",fontsize=14)
plt.ylabel("AntiDefense type",fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig("presence_absence_heatmap_bytype.png", dpi=300)
plt.show()
