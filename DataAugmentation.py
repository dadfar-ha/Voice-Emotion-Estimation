data = []

for path in tqdm(Path("/content/data/aesdd").glob("**/*.wav")):
    name = str(path).split('/')[-1].split('.')[0]
    label = str(path).split('/')[-2]
    
    try:
        # There are some broken files
        s = torchaudio.load(path)
        data.append({
            "name": name,
            "path": path,
            "emotion": label
        })
    except Exception as e:
        # print(str(path), e)
        pass



df = pd.DataFrame(data)
df.head()



# Filter broken and non-existed paths

print(f"Step 0: {len(df)}")

df["status"] = df["path"].apply(lambda path: True if os.path.exists(path) else None)
df = df.dropna(subset=["path"])
df = df.drop("status", 1)
print(f"Step 1: {len(df)}")

df = df.sample(frac=1)
df = df.reset_index(drop=True)
df.head()



print("Labels: ", df["emotion"].unique())
print()
df.groupby("emotion").count()[["path"]]