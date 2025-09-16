import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create a figure with subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# ------------------- Layered Cloud Architecture -------------------
layers = [
    "Application Layer\n(User-facing apps)",
    "Service Layer\n(IaaS, PaaS, SaaS)",
    "Management Layer\n(Monitoring, Security, Billing)",
    "Virtualization Layer\n(VMs, Containers, Virtual Storage)",
    "Physical Layer\n(Hardware: Servers, Network, Storage)"
]

# Draw layers as rectangles
for i, layer in enumerate(layers):
    rect = mpatches.Rectangle((0.2, i), 1.6, 0.9, facecolor="skyblue", edgecolor="black")
    axs[0].add_patch(rect)
    axs[0].text(1, i + 0.45, layer, ha="center", va="center", fontsize=10, weight="bold")

axs[0].set_xlim(0, 2)
axs[0].set_ylim(0, len(layers))
axs[0].axis("off")
axs[0].set_title("Layered Cloud Architecture", fontsize=14, weight="bold")


# ------------------- NIST Cloud Reference Model -------------------
entities = [
    ("Cloud Consumer", (1, 5)),
    ("Cloud Provider", (4, 5)),
    ("Cloud Broker", (2.5, 3.5)),
    ("Cloud Auditor", (1, 2)),
    ("Cloud Carrier", (4, 2))
]

# Draw entities as ellipses
for name, (x, y) in entities:
    ellipse = mpatches.Ellipse((x, y), 1.8, 0.9, facecolor="lightgreen", edgecolor="black")
    axs[1].add_patch(ellipse)
    axs[1].text(x, y, name, ha="center", va="center", fontsize=10, weight="bold")

# Draw arrows showing interactions
connections = [
    ((1, 5), (4, 5)),   # Consumer <-> Provider
    ((1, 5), (2.5, 3.5)),
    ((4, 5), (2.5, 3.5)),
    ((1, 5), (1, 2)),
    ((4, 5), (4, 2))
]

for start, end in connections:
    axs[1].arrow(start[0], start[1], (end[0]-start[0])*0.8, (end[1]-start[1])*0.8,
                 head_width=0.1, head_length=0.1, fc="black", ec="black", length_includes_head=True)

axs[1].set_xlim(0, 5)
axs[1].set_ylim(1, 6)
axs[1].axis("off")
axs[1].set_title("NIST Cloud Computing Reference Architecture", fontsize=14, weight="bold")

plt.tight_layout()
plt.show()
