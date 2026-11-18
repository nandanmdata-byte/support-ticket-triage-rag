import os
from datasets import load_dataset


def main():
  os.makedirs("data", exist_ok=True)
  df = load_dataset("Tobi-Bueck/customer-support-tickets", split="train").to_pandas()

  df_en = df[df["language"].str.lower() == "en"][["subject", "body", "answer", "queue", "priority"]].copy()
  df_en.to_csv("data/support_tickets_en.csv", index=False, encoding="utf-8")

  print(f"Saved {len(df_en)} English tickets")
  print(df_en["queue"].value_counts().head(10))
  print(df_en["priority"].value_counts())


if __name__ == "__main__":
    main()