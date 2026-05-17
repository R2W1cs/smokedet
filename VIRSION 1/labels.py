import os

def clean_labels(path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)

                new_lines = []
                with open(file_path, "r") as f:
                    lines = f.readlines()

                for line in lines:
                    parts = line.strip().split()

                    # لازم يكون bbox فقط (5 عناصر)
                    if len(parts) == 5:
                        parts[0] = "0"  # خلي كلشي class 0
                        new_lines.append(" ".join(parts) + "\n")

                with open(file_path, "w") as f:
                    f.writelines(new_lines)

# 👇 غير المسار حسب عندك
clean_labels("D:/VIRSION 1/datasets/dataset smoke 4961/labels")